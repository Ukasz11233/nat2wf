import pandas as pd
import re
import glob

file_pattern = f"data/conve*.txt"
matching_files = glob.glob(file_pattern)

# def format_mermaid_code(input_text):
#     formatted_code = re.sub(r']\s([A-Z])', r']\n\t\1', input_text)
#     formatted_code = re.sub(r'([A-Z])\s([A-Z])', r'\1\n\t\2', formatted_code)        
#     formatted_code = re.sub(r'}\s([A-Z])', r'}\n\t\1', formatted_code)
#     return formatted_code
    
input_texts = []
output_texts = []
df = pd.DataFrame()
for file_path in matching_files:
    with open(file_path, "r") as file:
        content = file.read()

    examples = content.split("assistant: ")

    inputs = []
    outputs = []

    i = 1
    for example in examples[1:]:
        for _ in range(100):
            input_match = re.search(f"Input{i}: (.+?)\n", example)
            output_match = re.search(f"Output{i}: (.+?)\n", example)

            if input_match and output_match:
                # outputs_value = "flowchart TD \n\t" + output_match.group(1)
                outputs_value = output_match.group(1)
                # outputs_value = format_mermaid_code(outputs_value)
                inputs_value = re.sub(r'Output.*', r'', input_match.group(1))
                inputs.append(inputs_value)
                outputs.append(outputs_value)
                output_texts.append(outputs_value)
                input_texts.append(inputs_value)
            i += 1  
    newDf = pd.DataFrame({"input": inputs, "output": outputs})
    df = pd.concat([df, newDf], ignore_index=True)
print(df)

print(output_texts)
# print(input_texts)