import jwt

Class ValidateToken():
    def __init__(self, token):
        self.token = token
        
    def validate_token(self):
            try:
                decoded_payload = jwt.decode(
                    self.token,
                    settings.SECRET_KEY,  # Your secret key
                    algorithms=["HS256"]  # The algorithm used for signing the token
                )
                return True
            except jwt.ExpiredSignatureError:
                # Token has expired
                return False
            except jwt.DecodeError:
                # Token is invalid
                return False