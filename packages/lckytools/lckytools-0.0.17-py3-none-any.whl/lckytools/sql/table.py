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


def create_table(
    table_name,
    schema_input,
    ignore_if_exist=False,
    schema_name=None,
    catalog_name=None,
    with_option=None,
):
    # Construct full table name
    full_table_name = table_name
    if schema_name:
        full_table_name = f"{schema_name}.{full_table_name}"
    if catalog_name:
        if schema_name:
            raise ValueError("Cannot specify both schema_name and catalog_name")
        full_table_name = f"{catalog_name}.{full_table_name}"

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


def drop_table(table_name, ignore_if_not_exist=False):
    if ignore_if_not_exist:
        sql = f"DROP TABLE IF EXISTS {table_name}"
    else:
        sql = f"DROP TABLE {table_name}"

    return sql
