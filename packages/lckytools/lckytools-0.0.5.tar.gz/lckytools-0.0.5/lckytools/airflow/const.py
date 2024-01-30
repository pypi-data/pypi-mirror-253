default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["test@email.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
}


lckyn_args = {
    "owner": "LCKYN",
    "depends_on_past": False,
    "email": ["t.pawarit@lckyn.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
}

work_args = {
    "owner": "T.Pawarit",
    "depends_on_past": False,
    "email": ["pawarit.t@avlgb.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
}
