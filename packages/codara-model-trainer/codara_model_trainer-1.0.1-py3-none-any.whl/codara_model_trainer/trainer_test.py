import os
import json
from codara_model_trainer.trainer import FineTuningDataCreator

class TestFineTuningDataCreator:
    def setup_method(self):
        """Setup for test methods."""
        self.creator = FineTuningDataCreator()
        self.test_dir = 'test-model-training'
        self.test_file = f'{self.test_dir}/fine-tune-data-set.jsonl'
        self.creator.filepath = self.test_file

    def teardown_method(self):
        """Teardown for test methods."""
        if os.path.exists(self.test_dir):
            for file in os.listdir(self.test_dir):
                os.remove(os.path.join(self.test_dir, file))
            os.rmdir(self.test_dir)

    def test_create_data_set(self):
        test_instructions = "Test instructions."
        test_prompt = "Test prompt."
        test_response = "Test response."

        self.creator.create_data_set(test_instructions, test_prompt, test_response)

        assert os.path.exists(self.test_file)
        with open(self.test_file, 'r') as file:
            data = json.loads(file.readline())
            assert data == {
                "messages": [
                    {"role": "system", "content": test_instructions},
                    {"role": "user", "content": test_prompt},
                    {"role": "assistant", "content": test_response}
                ]
            }

    def test_create_data_set_directory_exists(self):
        os.makedirs(self.test_dir, exist_ok=True)
        assert os.path.exists(self.test_dir)  # Ensure directory exists
        self.creator.create_data_set("Test instructions", "Test prompt", "Test response")
        assert os.path.exists(self.test_file)  # Check if file is created

    def test_create_data_set_file_exists(self):
        os.makedirs(self.test_dir, exist_ok=True)
        # Create an empty file
        with open(self.test_file, 'w') as file:
            file.write("")

        assert os.path.exists(self.test_file)  # Ensure file exists

        self.creator.create_data_set("Test instructions", "Test prompt", "Test response")

        # Read the file for the data
        with open(self.test_file, 'r') as file:
            lines = file.readlines()

            # If file was initially empty, the data should be on the first line
            line_to_check = lines[0] if len(lines) == 1 else lines[-1]
            data = json.loads(line_to_check)
            assert data["messages"][0]["content"] == "Test instructions"
