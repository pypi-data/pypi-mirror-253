import os
import json

class FineTuningDataCreator:
    def __init__(self, filepath="model-training/fine-tune-data-set.jsonl"):
        self.filepath = filepath

    def create_data_set(self, system_content, prompt, response):
        # Ensure directory exists
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)

        # Create or append to the file
        data = {
            "messages": [
                {"role": "system", "content": system_content},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": response}
            ]
        }

        with open(self.filepath, 'a') as file:
            file.write(json.dumps(data) + "\n")
