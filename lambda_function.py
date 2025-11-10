import json
import boto3
import logging
from urllib.parse import parse_qs

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    try:
        logger.info("Received event: %s", json.dumps(event))
        
        if event['httpMethod'] == 'GET':
            with open('order.html', 'r') as f:
                return {
                    'statusCode': 200,
                    'headers': {'Content-Type': 'text/html'},
                    'body': f.read()
                }
                
        elif event['httpMethod'] == 'POST':
            parsed_data = parse_qs(event['body'])
            order_data = {
                'pizza_type': parsed_data['pizza_type'][0],
                'quantity': parsed_data['quantity'][0],
                'customer_name': parsed_data['customer_name'][0],
                'customer_email': parsed_data['customer_email'][0]
            }
            
            dynamodb.put_item(
                TableName='pizza_orders',
                Item={
                    'order_id': {'S': context.aws_request_id},
                    'pizza_type': {'S': order_data['pizza_type']},
                    'quantity': {'N': order_data['quantity']},
                    'customer_name': {'S': order_data['customer_name']},
                    'customer_email': {'S': order_data['customer_email']},
                    'order_status': {'S': 'RECEIVED'}
                }
            )
            
            with open('success.html', 'r') as f:
                return {
                    'statusCode': 200,
                    'headers': {'Content-Type': 'text/html'},
                    'body': f.read()
                }
                
        return {
            'statusCode': 405,
            'body': json.dumps({'error': 'Method not allowed'})
        }
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }