import time
from src.utils.crypto.crypto import CryptoUtils
from src.constants.environments import Environments

class Run:
  __slots__ = ['token', 'crypto']

  def __init__(self):
    self.token = ""
    self.crypto = CryptoUtils(Environments.token_secret)

  def run_process(self, token: str):
    try:
      self.token = token
      print('Executing process...')
      token_decode = self.crypto.decrypt_token(self.token)
      if 'exp' not in token_decode or token_decode['exp'] < time.time():
        raise ValueError("Token has expired or is invalid")
      print({
        'status': 'success',
        'message': 'Token decrypted successfully'
      })

      return token_decode
    except Exception as e:
      print(f"An error occurred: {e}")
      raise
