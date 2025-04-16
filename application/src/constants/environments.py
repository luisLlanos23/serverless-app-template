import os
import json

class __EnvironmentClass:
  __slots__ = []

  @property
  def cloud_config(self):
    cloud_config = os.getenv("CLOUD_ACCESS")
    if cloud_config is None: return None
    return json.loads(cloud_config)

  @property
  def token_secret(self):
    token_secret = os.getenv("TOKEN_SECRET")
    if token_secret is None: return None
    return token_secret

Environments = __EnvironmentClass()