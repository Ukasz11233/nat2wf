import pandas as pd
import re
import glob

file_pattern = f"conve*.txt"
matching_files = glob.glob(file_pattern)

for fileName in matching_files:
    print(fileName)
    

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
                outputs_value = "flowchart " + output_match.group(1)
                inputs.append(input_match.group(1))
                outputs.append(outputs_value)

            i += 1  
    
    newDf = pd.DataFrame({"input": inputs, "output": outputs})
    
    df = pd.concat([df, newDf], ignore_index=True) 
print(df)
