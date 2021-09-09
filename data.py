import requests
import json 
data=requests.get("https://opentdb.com/api.php?amount=20&type=boolean").text
parsed_data=json.loads(data)
question_data = parsed_data["results"]