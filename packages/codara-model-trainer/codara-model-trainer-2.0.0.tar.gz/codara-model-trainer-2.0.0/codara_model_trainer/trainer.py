import os
import json


def create_data_set(system_content, prompt, response, filepath=None):
    data = {
        "messages": [
            {"role": "system", "content": system_content},
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": response}
        ]
    }

    if filepath is None:
        filepath = "model-training/fine-tune-data-set.jsonl"

    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, 'a') as file:
        file.write(json.dumps(data) + "\n")
