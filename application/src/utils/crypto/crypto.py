import jwt
from jwt.exceptions import InvalidTokenError

class CryptoUtils:
  def __init__(self, secret_key, algorithms=None):
    self.secret_key = secret_key
    self.algorithms = algorithms or ["HS256"]

  def validate_token(self, token):
    """
    Validates the given JWT token.

    :param token: The JWT token to validate.
    :return: Decoded payload if valid, raises InvalidTokenError otherwise.
    """
    try:
      decoded = jwt.decode(token, self.secret_key, algorithms=self.algorithms, options={"verify_signature": True})
      return decoded
    except InvalidTokenError as e:
      raise InvalidTokenError(f"Invalid token: {e}")

  def decrypt_token(self, token):
    """
    Decrypts the given JWT token.

    :param token: The JWT token to decrypt.
    :return: Decoded payload if valid, raises InvalidTokenError otherwise.
    """
    return self.validate_token(token)