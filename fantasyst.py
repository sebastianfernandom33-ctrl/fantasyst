import json

def lambda_handler(event, context):

    response = {
        "user": "sebastian",
        "subscription": "active"
    	"region": "sa-east-1"
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
