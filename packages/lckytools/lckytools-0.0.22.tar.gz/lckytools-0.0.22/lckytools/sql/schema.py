def create_schema(catalog_name, schema_name, ignore_if_exist=False):
    if ignore_if_exist:
        return f"CREATE SCHEMA IF NOT EXISTS {catalog_name}.{schema_name}"
    else:
        return f"CREATE SCHEMA {catalog_name}.{schema_name}"


def drop_schema(catalog_name, schema_name, ignore_if_not_exist=False, cascade=False):
    if ignore_if_not_exist:
        sql = f"DROP SCHEMA IF EXISTS {catalog_name}.{schema_name}"
    else:
        sql = f"DROP SCHEMA {catalog_name}.{schema_name}"

    if cascade:
        sql += " CASCADE"
    else:
        sql += " RESTRICT"

    return sql


def show_schemas(catalog_name):
    return f"SHOW SCHEMAS FROM {catalog_name}"
