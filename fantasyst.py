import json

def lambda_handler(event, context):

    response = {
        "user": "sebastian",
        "subscription_status": "active"
	"cicd": "working"
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
