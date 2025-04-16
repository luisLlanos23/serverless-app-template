from main import execute_main_process, get_correct_payload

def function_handler(event, context):
  try:
    """
    AWS Lambda function handler
    :param event: AWS Lambda event
    :param context: AWS Lambda context
    :return: response
    """
    print('Running Lambda function...')
    result = execute_main_process(get_correct_payload(event))
    print('Finishing Lambda function...')
    return {
      'statusCode': 200,
      'body': result
    }
  except Exception as e:
    print(f"An error occurred: {e}")
    return { 'code': 500, 'message': str(e) }
