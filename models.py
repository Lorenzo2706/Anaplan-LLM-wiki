from os import getenv

fsp = {
    "customer_id": getenv("CUSTOMER_ID"),
    "workspace_id": getenv("DEV_POLARIS"),
    "model_id": getenv("FSP_MODEL_ID"),
}

umd = {
    "customer_id": getenv("CUSTOMER_ID"),
    "workspace_id": getenv("UMD_PROD"),
    "model_id": getenv("UMD_PROD_MODEL_ID"),
}
