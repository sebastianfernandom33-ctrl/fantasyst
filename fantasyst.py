import json

def lambda_handler(event, context):

    users = {
        "sebastian": {
            "plan": "premium",
            "region": "sa-east-1",
            "status": "active"
        },
        "marina": {
            "plan": "basic",
            "region": "us-east-1",
            "status": "active"
        },
        "angelica": {
            "plan": "premium",
            "region": "us-east-1",
            "status": "active"
        },
        "samuel": {
            "plan": "basic",
            "region": "sa-east-1",
            "status": "active"
        },
        "miguel": {
            "plan": "basic",
            "region": "us-west-1",
            "status": "inactive"
        },
        "northon": {
            "plan": "premium",
            "region": "us-east-2",
            "status": "active"
        },
        "sergio": {
            "plan": "premium",
            "region": "us-east-1",
            "status": "inactive"
        }
    }

    user = event.get("queryStringParameters", {}).get("user", "sebastian")

    response = users.get(
        user,
        {
            "error": "user not found"
        }
    )

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response)
    }
