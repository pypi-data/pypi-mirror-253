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


def create_table(table_name, schema_input, ignore_if_exist=False):
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

    columns_str = ", ".join(columns)
    if ignore_if_exist:
        return f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"
    else:
        return f"CREATE TABLE {table_name} ({columns_str})"


def drop_table(table_name, ignore_if_not_exist=False):
    if ignore_if_not_exist:
        sql = f"DROP TABLE IF EXISTS {table_name}"
    else:
        sql = f"DROP TABLE {table_name}"

    return sql
