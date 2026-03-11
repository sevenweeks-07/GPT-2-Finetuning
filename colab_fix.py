import json

filename = r"C:\Users\Dell\Desktop\GPT-2-Finetuning\gpt2_finetuning.ipynb" 

with open(filename, 'r', encoding='utf-8') as f:
    data = json.load(f)

# The nuclear option: delete the widgets completely so GitHub stops complaining
if 'widgets' in data.get('metadata', {}):
    del data['metadata']['widgets']
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Successfully nuked widgets and fixed {filename}!")
else:
    print("No widget metadata found to fix.")