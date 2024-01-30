def create_schema(schema_name, ignore_if_exist=False):
    if ignore_if_exist:
        return f"CREATE SCHEMA IF NOT EXISTS {schema_name};"
    else:
        return f"CREATE SCHEMA {schema_name};"


def drop_schema(schema_name, ignore_if_not_exist=False, cascade=False):
    if ignore_if_not_exist:
        sql = f"DROP SCHEMA IF EXISTS {schema_name}"
    else:
        sql = f"DROP SCHEMA {schema_name}"

    if cascade:
        sql += " CASCADE"
    else:
        sql += " RESTRICT"

    return f"{sql};"
