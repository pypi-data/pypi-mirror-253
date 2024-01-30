DEFAULT_ARGS = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["test@email.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
}


LCKYN_ARGS = {
    "owner": "LCKYN",
    "depends_on_past": False,
    "email": ["t.pawarit@lckyn.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
}

WORK_ARGS = {
    "owner": "T.Pawarit",
    "depends_on_past": False,
    "email": ["pawarit.t@avlgb.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
}
