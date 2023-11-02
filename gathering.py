import openai
import sys

if len(sys.argv) < 2:
    sys.exit(1)

apiKey = sys.argv[1]
openai.api_key = apiKey


messages = [
        {"role": "system", "content": "test"},
]

message = "Give me 100 examples like this but with different input and output according to the input. Name then accordingly Input1... Output1..., Input2... Output2... . Input: Keep searching a list until an item with the highest value is found. Remove the item. Output: A[Start] --> B[Search the list] B --> C{Item with the highest value found?} C -- No --> B C -- Yes --> D[Remove the item] D --> E[End]"
if message:
    messages.append(
            {"role": "user", "content": message},
    )
    chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
    )
print("This might take a couple of minutes...")
answer = chat_completion.choices[0].message.content
print(f"ChatGPT: {answer}")
messages.append({"role": "assistant", "content": answer})

# Save the conversation to a file
with open("conversation2.txt", "w") as file:
    for msg in messages:
        file.write(f"{msg['role']}: {msg['content']}\n")