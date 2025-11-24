import json
# Agregando comentario nuevo version
def lambda_handler(event, context):
    """
    Handler principal de la función Lambda.
    """
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello Sebas — tu Lambda está viva!",
            "event": event
        })
    }