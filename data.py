from requests import *

# CONSTANTS
TOTAL_QUESTIONS = 20
API_ENDPOINT = 'https://opentdb.com/api.php'
PARAMS = {
    "amount": TOTAL_QUESTIONS,
    "type": "boolean"
}
# GETTING DATA FROM API
response = get(API_ENDPOINT, params=PARAMS)
response.raise_for_status()
api_data = response.json()['results']
question_data = api_data
