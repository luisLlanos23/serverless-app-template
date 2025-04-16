import os
import sys
import json
from main import execute_main_process, get_correct_payload

if __name__ == "__main__":
  print('Initializing task...')
  payload = get_correct_payload(json.loads(os.environ.get('payload', '{}')))
  print('Payload:', payload)
  execute_main_process(payload)
  print('Finishing task...')
  sys.exit(0)