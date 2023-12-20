from openai import OpenAI


client = OpenAI(api_key='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')

workflow_to_be_converted = input("Enter the workflow to be converted:\n")
print('\n\n\n')
query = "Create a mermaid TD graph that describes provided workflow. Do not label edges (except for the if block), all necessary information should be included in nodes. Please include the code only. Use proper block shapes."


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": query + workflow_to_be_converted + "\n"}
  ]
)

print(completion.choices[0].message.content)