import json

def lambda_handler(event, context):

    response = {
        "user": "sebastian",
        "subscription": "active"
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
