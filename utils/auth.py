from fastapi import Header, HTTPException

def token_auth(x_token: str = Header(...)):
    if x_token != "work123":
        raise HTTPException(status_code=403, detail="Invalid token")

