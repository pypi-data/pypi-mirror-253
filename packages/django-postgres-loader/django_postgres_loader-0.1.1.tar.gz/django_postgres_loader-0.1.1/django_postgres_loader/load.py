"""Handlers for loading data into the database."""

# standard library imports
import csv
import inspect
import io
import os
from pathlib import Path
import random
import string
from typing import Callable, Dict, List, Optional, Set, Type, Union

# third-party imports
from django.db import models
from django.db import connections, NotSupportedError, router

# local imports
from .core import definitions, field_updaters


class CopyLoader:
    """Load data from a CSV object into PostgreSQL database."""

    def __init__(
        self,
        model: Type[models.Model],
        data: Union[str, io.StringIO],
        operation: str,
        conflict_target: Optional[List[str]] = None,
        update_operation: Optional[
            Union[str, Callable, Dict[str, Optional[Union[str, Callable]]]]
        ] = None,
        field_mapping: Optional[Dict[str, str]] = None,
        delimiter: Optional[str] = None,
        null_string: Optional[str] = None,
        quote_character: Optional[str] = None,
        force_not_null: Optional[List[str]] = None,
        force_null: Optional[List[str]] = None,
        encoding: Optional[str] = None,
        temp_table_name: Optional[str] = None,
    ):
        """Instantiate a CopyLoader instance.

        Create an object that can be used to load [data] into [model] using the
        specified [operation] and [update_operation] and using provided
        configuration details.

        Supported operations:
            "append":       Add [data] without performing any conflict check.
            "safe_append":  Add [data], but do not add rows where
                            [conflict_target] matches that of an existing row.
            "update":       If [conflict_target] matches that of an existing
                            row, then update the row using [update_operation].
                            Otherwise, do nothing.
            "upsert":       If [conflict_target] matches that of an existing
                            row, then update the row using [update_operation].
                            Otherwise, insert a new row.

        Supported update operations ([old] = existing value; [new] = new value):
            "add":          [old] + [new]
            "subtract_new": [old] - [new]
            "subtract_old": [new] - [old]
            "multiply":     [old] * [new]
            "divide_new":   [old] / [new]
            "divide_old":   [new] / [old]
            "replace":      [new]
            "coalesce_new": COALESCE([new], [old])
            "coalesce_old": COALESCE([old], [new])
            "greatest":     GREATEST([old], [new])
            "least":        LEAST([old], [new])
            None:           Do not update

        Args:
            model (models.Model):
                The model into which data will be loaded
            data (StringIO):
                The data to load into [model]. If a StringIO object, then must
                be CSV-formatted data. If a string, then must be a path to an
                existing CSV file.
            operation (str):
                The type of load to perform. See above for permissible values
                and descriptions.
            conflict_target ([list[str]]):
                The set of columns to use as the conflict target in the
                "ON CONFLICT" clause of the insert. Must be provided if
                [operation] is "safe_append", "update", or "upsert"; will not be
                used if [operation] is "append" or "replace". If provided, must
                be a subset of [model]'s columns.
            update_operation ([str|Callable|dict[str, [str|Callable]]:
                The operation to use when updating records. Must be provided if
                [operation] is "update" or "upsert"; will not be used if
                [operation] is "append", "safe_append", or "replace".

                May be provided as a string, function, or a dictionary whose
                keys are names of columns in [data] and whose values are
                operations. If a string is provided, the provided operation will
                be used to update all columns other than those specified in
                [conflict_target]. If a dictionary is provided, then its keys
                must be a subset of [data]'s columns (any excluded columns will
                not be updated) and its values must be valid update operations.
                If a function (Callable) is provided, then it must have three
                parameters: field_name, model_table_name, temp_table_name; it
                must also return a string (this is NOT validated).

                See above for permissible values and descriptions.
            field_mapping ([dict]):
                The mapping of columns in [data] (keys) to columns in [model]
                (values). If provided, keys must be subset of [data]'s columns
                and values must be columns in [model]. Keys and values must be
                unique. Any field in [data] that is not included as a key is
                assumed to map to the corresponding field of [model].
            delimiter ([str]):
                The character used to separate columns within each row of the
                file. If not provided, then the PostgreSQL default (",") will
                be used.
            null_string ([str]):
                The string that represents a null value. If not provided, then
                the PostgreSQL default ("") will be used.
            quote_character ([str]):
                The quoting character to be used when a data value is quoted.
                If not provided, then the PostgreSQL default ('"') will be used.
            force_not_null ([list[str]):
                The columns for which [null_string] is not to be cast to NULL.
            force_null ([list[str]]):
                The columns for which [null_string] should be cast to NULL, even
                if it has been quoted.
            encoding ([str]):
                The encoding method used in the file. If not provided, then the
                PostgreSQL default (client encoding) will be used.
            temp_table_name ([str]):
                The name to give the temporary table storing [data] before it
                is loaded into [model]'s database table. If not provided, then
                a name will be randomly generated.
        """
        # Step 1
        if issubclass(model, models.Model):
            self.model = model
            self.model_table = self.model._meta.db_table
        else:
            raise TypeError("Model must be a Django model.")

        # Step 2
        self.db_connection = connections[router.db_for_write(self.model)]
        if (self.db_connection.vendor != "postgresql") or (
            self.db_connection.pg_version < 90500
        ):
            raise NotSupportedError(
                "Backend must be PostgreSQL version 9.5 or higher."
            )

        # Step 3
        if isinstance(data, io.StringIO):
            self.data = data
            data.seek(0)
        elif isinstance(data, str):
            if not os.path.isfile(data):
                raise FileNotFoundError(f"File {data} does not exist.")

            with open(file=data, mode="r") as file:
                self.data = io.StringIO(file.read())
                self.data.seek(0)
        elif hasattr(data, "to_csv"):
            string_io_data = io.StringIO()
            data.to_csv(string_io_data, index=False)
            string_io_data.seek(0)
            self.data = string_io_data
        else:
            raise TypeError(
                "Data must be a StringIO object or a path to a CSV file."
            )

        # Step 4
        if delimiter is None:
            self.delimiter = ","
        elif isinstance(delimiter, str):
            if len(delimiter) == 1:
                self.delimiter = delimiter
            else:
                raise ValueError("Delimiter must be a single character.")
        else:
            raise TypeError("Delimiter must be a string.")

        # Step 5
        if (null_string is None) or (isinstance(null_string, str)):
            self.null_string = null_string
        else:
            raise TypeError("NULL string must be a string or None.")

        # Step 6
        if quote_character is None:
            self.quote_character = quote_character
        elif isinstance(quote_character, str):
            if len(quote_character) == 1:
                self.quote_character = quote_character
            else:
                raise ValueError("Quote character must be a single character.")
        else:
            raise TypeError("Quote character must be a string.")

        # Step 7
        if (encoding is None) or (isinstance(encoding, str)):
            self.encoding = encoding
        else:
            raise TypeError("Encoding method must be a string or None.")

        # Step 8
        self.data_columns = self.get_data_columns()
        self.model_columns = self.get_model_columns()

        # Step 9
        self.field_mapping = (
            field_mapping if field_mapping is not None else dict()
        )
        self.validate_field_mapping()
        self.complete_field_mapping()
        self.validate_field_mapping()
        self.apply_field_mapping()

        # Step 10
        self.force_null = force_null
        self.validate_force_null()

        # Step 11
        self.force_not_null = force_not_null
        self.validate_force_not_null()

        # Step 12
        if temp_table_name is None:
            self.temp_table_name = self.generate_temp_table_name()
        elif isinstance(temp_table_name, str):
            self.temp_table_name = temp_table_name
            self.validate_temp_table_name()
        else:
            raise TypeError("Temp table name must be a string.")

        # Step 13
        self.operation = operation
        self.validate_operation()

        # Step 14
        self.conflict_target = conflict_target
        self.validate_conflict_target()

        # Step 15
        self.update_operation = update_operation
        self.validate_update_operation()

    def apply_field_mapping(self) -> None:
        """Apply [self].field_mapping to [self].data.

        Steps:
            1.  Extract the header row from [self].data
            2.  Replace old header name with new header name using
                [self].field_mapping.
            3.  Rebuild [self].data using the updated header row.

        Returns:
            None
        """
        # Step 1
        data_rows = self.data.readlines()
        header_row = data_rows[0]

        # Step 2
        n_updates = 0
        for old, new in self.field_mapping.items():
            if old != new:
                header_row = header_row.replace(old, new)
                n_updates += 1

        # Step 3
        data_rows[0] = header_row
        data = "".join(data_rows)
        self.data = io.StringIO(data)
        self.data.seek(0)

        # Step 4
        if n_updates > 0:
            self.data_columns = self.get_data_columns()

    def complete_field_mapping(self) -> None:
        """Ensure that [self].field_mapping is complete.

        Returns:
            None
        """
        # Step 1
        for col in self.data_columns:
            if col not in self.field_mapping.keys():
                self.field_mapping.update({col: col})

    def generate_temp_table_name(self) -> str:
        """Create a randomly-generated name for a PostgreSQL temp table.

        Steps:
            1.  Create the prefix for the temp table name (value is "tmp_").
            2.  Create the suffix for the temp tabel name (value is 20 random
                letters/digits).
            3.  Combine the prefix and suffix to form the full table name.

        Returns (str):
            Randomly-generated name for a PostgreSQL temp table.
        """
        # Step 1
        prefix = "tmp_"

        # Step 2
        valid_characters = string.ascii_letters + string.digits
        suffix = "".join(random.choices(valid_characters, k=20))

        # Step 3
        return prefix + suffix

    def get_data_columns(self) -> List[str]:
        """Get column names from [self].data.

        Steps:
            1.  Create a CSV reader object.
            2.  Extract the column names from [self].data.
            3.  Return the cursor to the top of [self].data.
            4.  Return.

        Returns (list[str]):
            The names of the columns found in [self].data.
        """
        # Step 1
        reader = csv.reader(self.data, delimiter=self.delimiter)

        # Step 2
        columns = next(reader)

        # Step 3
        self.data.seek(0)

        # Step 4
        return columns

    def get_model_columns(self) -> List[str]:
        """Get column names from [self].model.

        Steps:
            1.  Extract column names from [self].model.
            2.  Return.

        Returns (list[str]):
            The names of the columns found in [self].model.
        """
        # Step 1
        columns = [f.get_attname_column()[1] for f in self.model._meta.fields]

        # Step 2
        return columns

    def get_valid_conflict_targets(self) -> List[Set[str]]:
        """Get a list of all permissible values of [self].conflict_target.

        A set of columns in a valid conflict target if the columns are required
        to be unique within [self].model. This can be met in the following ways:
            *   The column that serves as the model's primary key
            *   Any column in the model for which unique=True
            *   Any column(s) for which a UniqueConstraint is defined
            *

        This function checks each of these conditions, returning list of all
        columns and/or combinations of columns meeting at least one.

        Returns (list[set[str]]:
            All permissible values of [self].conflict_target.
        """
        # Step 1
        valid_conflict_targets = []

        # Step 2
        primary_key_target = self.model._meta.pk.get_attname_column()[1]
        valid_conflict_targets.append({primary_key_target})

        # Step 3
        for f in self.model._meta.get_fields():
            if (hasattr(f, "unique")) and (f.unique) and (not f.primary_key):
                field_name = f.get_attname_column()[1]
                valid_conflict_targets.append({field_name})

        # Step 4
        for c in self.model._meta.constraints:
            if isinstance(c, models.UniqueConstraint):
                valid_conflict_targets.append(set(c.fields))

        # Step 5
        if self.model._meta.unique_together:
            valid_conflict_targets.append(set(self.model._meta.unique_together))

        # Step 5
        return valid_conflict_targets

    def validate_conflict_target(self) -> None:
        """Ensure that [self].conflict_target is valid.

        In order for a conflict target to be valid, it must meet the following
        conditions:
            *   Type is list of strings
            *   Value(s) form subset of columns of [self].model
            *   Value(s) form a unique constraint on [self].model
                *   Primary key
                *   unique_together
                *   UniqueConstraint

        Returns:
            None
        """
        # Step 1
        if self.conflict_target is None:
            pass

        # Step 2
        elif isinstance(self.conflict_target, list):
            # Step 2.1
            is_valid = False

            # Step 2.1
            valid_conflict_targets = self.get_valid_conflict_targets()

            # Step 2.2
            for ct in valid_conflict_targets:
                if set(self.conflict_target) == ct:
                    is_valid = True
                    break

            # Step 2.3
            if not is_valid:
                raise ValueError(
                    "Column(s) in conflict target must have unique constraint."
                )

        # Step 3
        else:
            raise TypeError("Conflict target must be a list or None.")

    def validate_field_mapping(self) -> None:
        """Ensure [self].field_mapping is a valid column mapping.

        Steps:
            1.  If field mapping is None, then it is valid.
            2.  If field mapping is dictionary, then validate it.
                2.1.    Ensure that each key is the name of a column in
                        [self].data.
                2.2.    Ensure that each value is the name of a column in
                        [self].model.

        Returns:
            None
        """
        # Step 1
        if self.field_mapping is None:
            pass

        # Step 2
        elif isinstance(self.field_mapping, dict):
            # Step 2.1
            for k in self.field_mapping.keys():
                if not isinstance(k, str):
                    raise TypeError(
                        "All keys of field mapping must be strings."
                    )
                elif k not in self.data_columns:
                    raise ValueError(f"Column {k} not found in CSV data.")

            # Step 2.2
            if len(list(self.field_mapping.values())) != len(
                set(self.field_mapping.values())
            ):
                raise ValueError(
                    "Each column in the field mapping must map to a unique model column."
                )
            for v in self.field_mapping.values():
                if not isinstance(v, str):
                    raise TypeError(
                        "All values of field mapping must be strings."
                    )
                elif v not in self.model_columns:
                    raise ValueError(f"Column {v} not found in model.")

        else:
            raise TypeError("Field mapping must be a dictionary or None.")

    def validate_force_not_null(self) -> None:
        """Confirm that [self].force_not_null is a valid list of columns.

        Returns:
            None
        """
        # Step 1
        if self.force_not_null is None:
            pass

        # Step 2
        elif isinstance(self.force_not_null, list):
            for column in self.force_not_null:
                # Step 2.1
                if not isinstance(column, str):
                    raise TypeError(
                        "FORCE NOT NULL column names must be strings."
                    )

                # Step 2.2
                elif column not in self.model_columns:
                    raise ValueError(
                        f"FORCE NOT NULL column {column} not found in model."
                    )

        # Step 3
        else:
            raise TypeError(
                f"FORCE NOT NULL must be a list of database columns."
            )

    def validate_force_null(self) -> None:
        """Confirm that [self].force_null is a valid list of columns.

        Returns:
            None
        """
        # Step 1
        if self.force_null is None:
            pass

        # Step 2
        elif isinstance(self.force_null, list):
            for column in self.force_null:
                # Step 2.1
                if not isinstance(column, str):
                    raise TypeError("FORCE NULL column names must be strings.")

                # Step 2.2
                elif column not in self.model_columns:
                    raise ValueError(
                        f"FORCE NULL column {column} not found in model."
                    )

        # Step 3
        else:
            raise TypeError(f"FORCE NULL must be a list of database columns.")

    def validate_operation(self) -> None:
        """Confirm that value of [self].operation is valid.

        Steps:
            1.  If [self].operation is one of the permitted operations, then it
                is valid.
            2.  If [self].operation is a string but not one of the permitted
                operations, then raise an error stating the permitted options.
            3.  If [self].operations is not a string, then raise an error
                stating that it must be a string.

        Returns:
            None
        """
        # Step 1
        if self.operation in definitions.INCLUDED_OPERATIONS:
            pass

        # Step 2
        elif isinstance(self.operation, str):
            raise ValueError(
                "Operation must be one of: append, replace, safe_append, update, upsert"
            )

        # Step 3
        else:
            raise TypeError("Operation must be a string.")

    def validate_temp_table_name(self) -> None:
        """Confirm that [self].temp_table_name is a valid PostgreSQL table name.

        Steps:
            1.  If table name is a string, then validate it.
                1.1.    Confirm that name is not empty.
                1.2.    Confirm that name is no longer than 31 characters.
                1.3.    Confirm that name starts with letter or underscore.
                1.4.    Confirm that subsequent characters in name are letters,
                        digits, or underscores.

        Returns:
            None
        """
        # Step 1
        if isinstance(self.temp_table_name, str):
            # Step 1.1
            if len(self.temp_table_name) == 0:
                raise ValueError(
                    "Temp table name must contain at least one character."
                )

            # Step 1.2
            elif len(self.temp_table_name) > 31:
                raise ValueError(
                    "Temp table name must be no longer than 31 characters."
                )

            # Step 1.3
            valid_start_characters = string.ascii_letters + "_"
            if self.temp_table_name[0] not in valid_start_characters:
                raise ValueError(
                    "Temp table name must begin with a letter or underscore."
                )

            # Step 1.4
            valid_characters = string.ascii_letters + string.digits + "_"
            if not set(self.temp_table_name).issubset(valid_characters):
                raise ValueError(
                    "Temp table name must only contain letters, digits, and underscores."
                )

        # Step 2
        else:
            raise TypeError("Temp table name must be a string.")

    def validate_update_operation(self) -> None:
        """Confirm that [self].update_operation is valid.

        Returns:
            None
        """
        # Step 1
        if isinstance(self.update_operation, str):
            if (
                self.update_operation
                not in definitions.INCLUDED_UPDATE_OPERATIONS
            ):
                raise ValueError(
                    f"Update operation must be one of: {', '.join(definitions.INCLUDED_UPDATE_OPERATIONS)}."
                )

        # Step 2
        elif isinstance(self.update_operation, Callable):
            signature = inspect.signature(self.update_operation)
            parameters = set(list(signature.parameters))
            expected_parameters = {
                "field_name",
                "target_table_name",
            }
            if parameters != expected_parameters:
                raise ValueError(
                    f"If update operation is a function, then it must include precisely the following parameters: {', '.join(expected_parameters)}."
                )

        # Step 3
        elif isinstance(self.update_operation, dict):
            for column, operation in self.update_operation.items():
                # Step 3.1
                if column in self.conflict_target:
                    raise ValueError(
                        f"Column {column} is part of the conflict target and cannot be updated."
                    )

                # Step 3.2
                elif column not in self.model_columns:
                    raise ValueError(
                        f"Column {column} not found in model {self.model.__name__}."
                    )

                # Step 3.3
                elif isinstance(operation, Callable):
                    signature = inspect.signature(operation)
                    parameters = set(list(signature.parameters))
                    expected_parameters = {
                        "field_name",
                        "target_table_name",
                    }
                    if parameters != expected_parameters:
                        raise ValueError(
                            f"Update operation for {column} is a function, but does not include precisely the following parameters: {', '.join(expected_parameters)}."
                        )

                # Step 3.3
                elif not isinstance(operation, str):
                    raise TypeError(
                        f"Update operation for column {column} must be a string."
                    )

                # Step 3.4
                elif operation not in definitions.INCLUDED_UPDATE_OPERATIONS:
                    raise ValueError(
                        f"Update operation for column {column} must be one of: {', '.join(definitions.INCLUDED_UPDATE_OPERATIONS)}"
                    )

        # Step 4
        elif self.update_operation is None:
            if self.operation in ["update", "upsert"]:
                raise ValueError(
                    f"If performing load operation {self.operation}, then an update operation must be provided."
                )

        # Step 5
        else:
            raise TypeError(
                "Update operation definition must be a string or dictionary."
            )

    def pre_create(self, cursor) -> None:
        """Pre-create hook.

        This function does nothing, but serves as a placeholder in case users wish
        to use a custom pre-create hook.

        Args:
            self:
                CopyLoader instance.
            cursor:
                Cursor.

        Returns:
            None
        """
        pass

    def build_create_query(self) -> str:
        """Build the query used to create a temp table on the database.

        Steps:
            1.  Use template to build the create query.
            2.  Dynamically populate the temp table name.
            3.  Generate list of field definitions based on the data's columns.
            4.  Format (3) for inclusion in the template and update the template
                to include field definitions.
            5.  Return.

        Returns (str):
            The query used to create a temp table on the database.
        """
        # Step 1
        create_query_path = os.path.join(
            definitions.SQL_TEMPLATE_DIR,
            "create.sql",
        )
        create_query = Path(create_query_path).read_text()

        # Step 2
        create_query = create_query.replace(
            "{temp_table_name}",
            self.temp_table_name,
        )

        # Step 3
        field_definitions = []
        for field in self.data_columns:
            field_type = self.model._meta.get_field(field).db_type(
                self.db_connection
            )
            field_definition = f'"{field}" {field_type.upper()}'
            field_definitions.append(field_definition)

        # Step 4
        field_definitions = ",\n\t".join(field_definitions)
        create_query = create_query.replace(
            "{field_definitions}",
            field_definitions,
        )

        # Step 5
        return create_query

    def post_create(self, cursor) -> None:
        """Post-create hook.

        This function does nothing, but serves as a placeholder in case users wish
        to use a custom post-create hook.

        Args:
            self:
                CopyLoader instance.
            cursor:
                Cursor.

        Returns:
            None
        """
        pass

    def create(self, cursor) -> None:
        """Create a temp table to store new data.

        Steps:
            1.  Run the pre-create hook.
            2.  Build the query used to create the temp table.
            3.  Execute the query and create the temp table.
            4.  Run the post-create hook.

        Args:
            cursor:
                Cursor.

        Returns:
            None
        """
        # Step 1
        self.pre_create(cursor)

        # Step 2
        create_query = self.build_create_query()

        # Step 3
        cursor.execute(create_query)

        # Step 4
        self.post_create(cursor)

    def pre_copy(self, cursor) -> None:
        """Pre-copy hook.

        This function does nothing, but serves as a placeholder in case users wish
        to use a custom pre-copy hook.

        Args:
            self:
                CopyLoader instance.
            cursor:
                Cursor.

        Returns:
            None
        """
        pass

    def build_copy_query(self) -> str:
        """Build the query used to copy data into the temp table.

        Returns (str):
            The query used to copy data into the temp table.
        """
        # Step 1
        copy_query_path = os.path.join(
            definitions.SQL_TEMPLATE_DIR,
            "copy.sql",
        )
        copy_query = Path(copy_query_path).read_text()

        # Step 2
        copy_query = copy_query.replace(
            "{temp_table_name}",
            self.temp_table_name,
        )

        # Step 3
        columns = ",\n\t".join(self.data_columns)
        copy_query = copy_query.replace("{columns}", columns)

        # Step 4
        header_options = []
        if self.quote_character is not None:
            header_options.append(f"QUOTE {self.quote_character}")
        header_options.append(f"DELIMITER '{self.delimiter}'")
        if self.null_string is not None:
            header_options.append(f"NULL '{self.null_string}'")
        if self.force_null is not None:
            force_null = ", ".join(f'"{col}' for col in self.force_null)
            header_options.append(f"FORCE_NULL {force_null}")
        if self.force_not_null is not None:
            force_not_null = ", ".join(f'"{col}' for col in self.force_not_null)
            header_options.append(f"FORCE_NOT_NULL {force_not_null}")
        if self.encoding is not None:
            header_options.append(f"ENCODING {self.encoding}")

        # Step 5
        header_options = "\n\t".join(header_options)
        copy_query = copy_query.replace("{header_options}", header_options)

        # Step 6
        return copy_query

    def post_copy(self, cursor) -> None:
        """Post-copy hook.

        This function does nothing, but serves as a placeholder in case users wish
        to use a custom post-copy hook.

        Args:
            self:
                CopyLoader instance.
            cursor:
                Cursor.

        Returns:
            None
        """
        pass

    def copy(self, cursor) -> None:
        """Populate the temp table with data from STDIN.

        Steps:
            1.  Run the pre-copy hook.
            2.  Build the query used to populate the temp table.
            3.  Execute the query and populate the temp table.
            4.  Run the post-copy hook.

        Args:
            cursor:
                Cursor.

        Returns:
            None
        """
        # Step 1
        self.pre_copy(cursor)

        # Step 2
        copy_query = self.build_copy_query()

        # Step 3
        cursor.copy_expert(copy_query, self.data)

        # Step 4
        self.post_copy(cursor)

    def pre_insert(self, cursor) -> None:
        """Pre-insert hook.

        This function does nothing, but serves as a placeholder in case users wish
        to use a custom pre-insert hook.

        Args:
            self:
                CopyLoader instance.
            cursor:
                Cursor.

        Returns:
            None
        """
        pass

    def build_insert_query(self) -> str:
        """Build the query used to insert temp table data into model table.

        Returns (str):
            The query used to insert temp table data into model table.
        """
        # Step 1
        insert_query_path = os.path.join(
            definitions.SQL_TEMPLATE_DIR,
            f"insert__{self.operation}.sql",
        )
        insert_query = Path(insert_query_path).read_text()

        # Step 2
        model_table_name = self.model_table
        insert_query = insert_query.replace(
            "{model_table_name}",
            model_table_name,
        )

        # Step 3
        insert_query = insert_query.replace(
            "{temp_table_name}",
            self.temp_table_name,
        )

        # Step 4
        columns = ",\n\t".join(f'"{col}"' for col in self.data_columns)
        insert_query = insert_query.replace("{columns}", columns)

        # Step 5
        if self.conflict_target is not None:
            conflict_target = ", ".join(
                f'"{col}"' for col in self.conflict_target
            )
            insert_query = insert_query.replace(
                "{conflict_target}",
                conflict_target,
            )

        # Step 6
        if self.update_operation is not None:
            # Step 6.1
            update_operations = []

            # Step 6.2
            if isinstance(self.update_operation, str):
                # Step 6.2.1
                data_column_set = set(self.data_columns)
                conflict_target_set = set(self.conflict_target)
                non_conflict_target = list(
                    data_column_set.difference(conflict_target_set)
                )
                updater = getattr(field_updaters, self.update_operation)

                # Step 6.2.2
                for field in non_conflict_target:
                    update_snippet = updater(field, model_table_name)
                    update_operations.append(update_snippet)

                # Step 6.2.3
                update_operations = ",\n\t".join(update_operations)

            # Step 6.3
            elif isinstance(self.update_operation, Callable):
                # Step 6.3.1
                data_column_set = set(self.data_columns)
                conflict_target_set = set(self.conflict_target)
                non_conflict_target = list(
                    data_column_set.difference(conflict_target_set)
                )
                updater = self.update_operation

                # Step 6.3.2
                for field in non_conflict_target:
                    update_snippet = updater(field, model_table_name)
                    update_operations.append(update_snippet)

                # Step 6.3.3
                update_operations = ",\n\t".join(update_operations)

            # Step 6.4
            else:
                # Step 6.4.1
                for field, operation in self.update_operation.items():
                    if isinstance(operation, str):
                        updater = getattr(field_updaters, operation)
                    else:
                        updater = operation

                    update_snippet = updater(field, model_table_name)
                    update_operations.append(update_snippet)

                # Step 6.4.2
                update_operations = ",\n\t".join(update_operations)

            # Step 6.5
            insert_query = insert_query.replace(
                "{update_operations}",
                update_operations,
            )

        # Step 7
        if self.operation == "update":
            # Step 7.1
            update_join_conditions = []

            # Step 7.2
            for field in self.conflict_target:
                old_field = f'"{model_table_name}"."{field}"'
                new_field = f'"{self.temp_table_name}"."{field}"'
                join_condition = f"""{old_field} = {new_field}"""
                update_join_conditions.append(join_condition)

            # Step 7.3
            update_join_conditions = "\n\t\t\tAND ".join(update_join_conditions)
            insert_query = insert_query.replace(
                "{update_join_conditions}",
                update_join_conditions,
            )

        # Step 8
        return insert_query

    def post_insert(self, cursor) -> None:
        """Post-insert hook.

        This function does nothing, but serves as a placeholder in case users wish
        to use a custom post-insert hook.

        Args:
            self:
                CopyLoader instance.
            cursor:
                Cursor.

        Returns:
            None
        """
        pass

    def insert(self, cursor) -> int:
        """Perform the insert required to apply the desired update.

        Steps:
            1.  Run the pre-insert hook.
            2.  Build the query used to perform the update.
            3.  Execute the query and perform the update and get row count.
            4.  Run the post-insert hook.
            5.  Return.

        Args:
            cursor:
                Cursor.

        Returns (int):
            The number of rows affected by the update.
        """
        # Step 1
        self.pre_insert(cursor)

        # Step 2
        insert_query = self.build_insert_query()

        # Step 3
        cursor.execute(insert_query)
        n_rows_affected = cursor.rowcount

        # Step 4
        self.post_insert(cursor)

        # Step 5
        return n_rows_affected

    def pre_drop(self, cursor) -> None:
        """Pre-drop hook.

        This function does nothing, but serves as a placeholder in case users wish
        to use a custom pre-drop hook.

        Args:
            self:
                CopyLoader instance.
            cursor:
                Cursor.

        Returns:
            None
        """
        pass

    def build_drop_query(self) -> str:
        """Build the query used to drop the temp table.

        Steps:
            1.  Use template to build the drop query.
            2.  Dynamically populate the temp table name.
            3.  Return.

        Returns (str):
            The query used to drop the temp table from the database.
        """
        # Step 1
        drop_query_path = os.path.join(
            definitions.SQL_TEMPLATE_DIR,
            "drop.sql",
        )
        drop_query = Path(drop_query_path).read_text()

        # Step 2
        drop_query = drop_query.replace(
            "{temp_table_name}",
            self.temp_table_name,
        )

        # Step 3
        return drop_query

    def post_drop(self, cursor) -> None:
        """Post-drop hook.

        This function does nothing, but serves as a placeholder in case users wish
        to use a custom post-drop hook.

        Args:
            self:
                CopyLoader instance.
            cursor:
                Cursor.

        Returns:
            None
        """
        pass

    def drop(self, cursor) -> None:
        """Remove the temp table from the database.

        Steps:
            1.  Run the pre-drop hook.
            2.  Build the query to drop the temp table.
            3.  Execute the query and drop the temp table.
            4.  Run the post-drop hook.

        Args:
            cursor:
                Cursor.

        Returns:
            None
        """
        # Step 1
        self.pre_drop(cursor)

        # Step 2
        drop_query = self.build_drop_query()

        # Step 3
        cursor.execute(drop_query)

        # Step 4
        self.post_drop(cursor)

    def load(self) -> int:
        """Perform the full update pipeline.

        Returns (int):
            The number of rows affected by the update.
        """
        # Step 1
        with self.db_connection.cursor() as cursor:
            self.create(cursor=cursor)
            self.copy(cursor=cursor)
            n_rows_affected = self.insert(cursor=cursor)
            self.drop(cursor=cursor)

        # Step 2
        return n_rows_affected
