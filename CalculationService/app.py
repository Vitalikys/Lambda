import json
import requests

from calculate import CalculationService


def lambda_handler(event, context):
    """Sample pure Lambda function
    how to RUN:
    send get request to url:
    https://yhqc2dlu23.execute-api.us-east-1.amazonaws.com/Prod/hello?arr1=1-2-3&arr2=4-5-6
    Returns     API Gateway Lambda Proxy Output Format: dict
   """
    try:
        # get IP address
        ip = requests.get("http://checkip.amazonaws.com/")

        # get parameter array 1,2 from url (example: '1-2-3' )
        arr1 = event['queryStringParameters']['arr1']
        arr2 = event['queryStringParameters']['arr2']

        # convert array to list  (example: [1,2,3] )
        arr1 = list(map(int, arr1.split('-')))
        arr2 = list(map(int, arr2.split('-')))

        # get results
        cs = CalculationService()
        result_array = cs.transpose_matrix([arr1, arr2])
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "hello Lambda World",
                "about API": "convert two lists: [[1,2,3], [4,5,6]] to [[1, 4], [2, 5], [3, 6]]",
                "location": ip.text.replace("\n", ""),
                "numpy_array": result_array.tolist(),
                "author": "Vitaliy K."
            }),
        }

    except Exception as e:
        # Send some context about this error to Lambda Logs
        print(str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "hello Lambda World",
                "error": str(e),
                "about API": "convert two lists: [[1,2,3], [4,5,6]] to [[1, 4], [2, 5], [3, 6]]",
                "location": ip.text.replace("\n", ""),
                "author": "Vitaliy K."
            })
        }
