import jwt

def encoded_token (data: dict):
    print(data)
    token: str = jwt.encode(payload=data, key="secret", algorithm="HS256")
    return token

def decoded_token (token: str):
    data: dict = jwt.decode(token, key="secret", algorithms=["HS256"])
    return data