import json

def lambda_handler(event, context):

    response = {
        "user": "sebastian",
        "subscription_status": "active",
	"cicd": "working",
    	"plan": "premium",
    	"region": "sa-east-1",
        "version": "1.1.0"
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
