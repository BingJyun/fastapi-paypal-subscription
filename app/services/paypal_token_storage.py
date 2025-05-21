paypal_token_storage = {
    "access_token": None,
}

def set_access_token(access_token: str):
    paypal_token_storage["access_token"] = access_token