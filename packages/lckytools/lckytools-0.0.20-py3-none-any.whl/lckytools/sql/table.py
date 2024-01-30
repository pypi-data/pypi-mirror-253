import pandas as pd

TYPE_MAPPING = {
    "int": "INT",
    "int32": "INT",
    "int64": "INT",
    "string": "VARCHAR",
    "float": "FLOAT",
    "float32": "FLOAT",
    "float64": "DOUBLE",
}


def _get_table_name(table_name, schema_name=None, catalog_name=None):
    # Construct full table name
    full_table_name = table_name
    if schema_name:
        full_table_name = f"{schema_name}.{full_table_name}"
    if catalog_name:
        if not schema_name:
            raise ValueError("schema_name must be specified if catalog_name is given.")
        full_table_name = f"{catalog_name}.{full_table_name}"

    return full_table_name


def create_table(
    table_name,
    schema_input,
    ignore_if_exist=False,
    schema_name=None,
    catalog_name=None,
    with_option=None,
):
    # Construct full table name
    full_table_name = _get_table_name(table_name, schema_name, catalog_name)

    # Validate and process schema_input
    if isinstance(schema_input, list):
        columns = [
            f"{col_name} {TYPE_MAPPING.get(data_type, data_type)}"
            for col_name, data_type in schema_input
        ]
    elif isinstance(schema_input, pd.DataFrame):
        columns = [
            f"{col_name} {TYPE_MAPPING.get(str(dtype), str(dtype))}"
            for col_name, dtype in zip(schema_input.columns, schema_input.dtypes)
        ]
    else:
        raise ValueError("Invalid schema_input format")

    # Construct and return SQL statement
    columns_str = ", ".join(columns)

    sql_command = "CREATE TABLE "
    if ignore_if_exist:
        sql_command += "IF NOT EXISTS "
    sql_command += f"{full_table_name} ({columns_str})"

    if with_option:
        sql_command += f" WITH ({with_option})"

    return sql_command


def drop_table(
    table_name,
    schema_name=None,
    catalog_name=None,
    ignore_if_not_exist=False,
):
    full_table_name = _get_table_name(table_name, schema_name, catalog_name)

    if ignore_if_not_exist:
        return f"DROP TABLE IF EXISTS {full_table_name}"
    return f"DROP TABLE {full_table_name}"


def show_tables(schema_name, catalog_name=None):
    if catalog_name:
        return f"SHOW TABLES FROM {catalog_name}.{schema_name}"
    return f"SHOW TABLES FROM {schema_name}"


def count_rows(table_name, schema_name=None, catalog_name=None):
    full_table_name = _get_table_name(table_name, schema_name, catalog_name)

    return f"SELECT COUNT(*) FROM {full_table_name}"
