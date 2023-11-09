import openai
import sys

if len(sys.argv) < 2:
    print("Add api key as arg")
    sys.exit(1)

apiKey = sys.argv[1]
openai.api_key = apiKey




for i in range(77, 82):
    messages = [
        {"role": "system", "content": "test"},
    ]
    message =   "Give me 20 examples like this but with different input and output according to the input. Name then accordingly Input1... Output1..., Input2... Output2... . Input: Turn on the computer. Enter the username and password to log in. Open the desired software or application. Perform the required tasks. Save any changes made. Shut down the computer. Output: A[Start] --> B[Turn on the computer] B --> C[Enter username and password to log in] C --> D[Open desired software or application] D --> E[Perform required tasks] E --> F[Save any changes made] F --> G[Shut down the computer] G --> H[End]. Remember to create various length graphs"
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
