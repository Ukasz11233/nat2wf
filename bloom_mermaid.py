import requests

API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
API_TOKEN='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'
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

workflow="Check if a given year is a leap year or not"

output = query({
	"inputs": "Create a mermaid TD graph that describes provided workflow. Do not label edges (except for the if block), all necessary information should be included in nodes. Please include the code only. Use proper block shapes." + workflow
,
})
print(output)