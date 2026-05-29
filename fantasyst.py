import json

def lambda_handler(event, context):

    users = {
        "sebastian": {
            "plan": "premium",
            "region": "sa-east-1",
            "status": "active",
            "tier": "enterprise"
        },
        "marina": {
            "plan": "basic",
            "region": "us-east-1",
            "status": "active",
            "tier": "enterprise"
        },
        "angelica": {
            "plan": "premium",
            "region": "us-east-1",
            "status": "active",
            "tier": "enterprise"
        },
        "samuel": {
            "plan": "basic",
            "region": "sa-east-1",
            "status": "active",
            "tier": "enterprise"
        },
        "miguel": {
            "plan": "basic",
            "region": "us-west-1",
            "status": "inactive",
            "tier": "enterprise"
        },
        "northon": {
            "plan": "premium",
            "region": "us-east-2",
            "status": "active",
            "tier": "enterprise"
        },
        "sergio": {
            "plan": "premium",
            "region": "us-east-1",
            "status": "inactive",
            "tier": "enterprise"
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
