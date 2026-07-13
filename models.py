from os import getenv

fsp = {
    "name": "FSP",
    "customer_id": getenv("CUSTOMER_ID"),
    "workspace_id": getenv("DEV_POLARIS"),
    "model_id": getenv("FSP_MODEL_ID"),
}

umd = {
    "name": "UMD",
    "customer_id": getenv("CUSTOMER_ID"),
    "workspace_id": getenv("UMD_PROD"),
    "model_id": getenv("UMD_PROD_MODEL_ID"),
}

mjp = {
    "name": "MJP",
    "customer_id": getenv("CUSTOMER_ID"),
    "workspace_id": getenv("MJP_PROD"),
    "model_id": getenv("MJP_MODEL_ID"),
}

MODELS = {
    "fsp": fsp,
    "umd": umd,
    "mjp": mjp,
}
