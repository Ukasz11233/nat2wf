import openai
import sys

if len(sys.argv) < 2:
    print("Add api key as arg")
    sys.exit(1)

apiKey = sys.argv[1]
openai.api_key = apiKey




for i in range(120, 130):
    messages = [
        {"role": "system", "content": "test"},
    ]
    message =    "Give me 20 examples like this but with different input and output according to the input. Name then accordingly Input1... Output1..., Input2... Output2... . Input: Immerse yourself in different language learning resources. Practice speaking, writing, and listening in each language. Attain fluency and communicate confidently in various language Output: B --> C[Fluency in multiple languages achieved?] C -- No --> B C -- Yes --> D[Immerse yourself in different language learning resources] D --> E[Practice speaking, writing, and listening ineach language] E --> F[Attain fluency and communicate confidently in various languages] F --> G[End] .Remember to create various length graphs"
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
    messages.append({"role": "assistant", "content": answer})
    print(f"Patch: {i}")
    # Save the conversation to a file
    with open(f"conversation{i}_20_examples.txt", "w") as file:
        for msg in messages:
            file.write(f"{msg['role']}: {msg['content']}\n")
