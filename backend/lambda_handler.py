import json
from app.agent_core import agent_execute

def lambda_handler(event, context):
    user_query = event.get("query", "")
    response = agent_execute(user_query)

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
