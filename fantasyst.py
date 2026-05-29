import json

def lambda_handler(event, context):

    response = {
        "user": "sebastian",
        "subscription": "active"
    	"plan": "premium"
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
