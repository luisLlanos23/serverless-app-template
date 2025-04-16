from typing import Dict
from src.configurations import configure_directories, configure_boto
from src.use_cases.process.run import Run

def execute_main_process(data: Dict[str, any]):
  try:
    configure_directories()
    configure_boto()
    print('Executing main process...')
    result = Run().run_process(token=data['token'])
    print('Process executed successfully.')
    return result
  except Exception as e:
    print(f"An error occurred while executing the main process: {e}")
    return {
      'code': 500,
      'message': str(e)
    }

def get_correct_payload(data: Dict[str, any]):
  return {
    "token": data["token"],
  }
