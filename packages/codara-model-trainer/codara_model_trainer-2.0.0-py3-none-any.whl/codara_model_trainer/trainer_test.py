import os
import json
import pytest
from codara_model_trainer import create_data_set


class TestCreateDataSet:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        # Setup code: create a test directory
        self.test_dir = 'test-model-training'
        self.test_file = f'{self.test_dir}/fine-tune-data-set.jsonl'
        os.makedirs(self.test_dir, exist_ok=True)
        yield  # this is where the testing happens
        # Teardown code: remove test directory and its contents
        if os.path.exists(self.test_dir):
            for file in os.listdir(self.test_dir):
                os.remove(os.path.join(self.test_dir, file))
            os.rmdir(self.test_dir)

    def test_data_written_correctly(self):
        create_data_set("Test instructions", "Test prompt", "Test response", filepath=self.test_file)

        with open(self.test_file, 'r') as file:
            data = json.loads(file.readline())
            assert data == {
                "messages": [
                    {"role": "system", "content": "Test instructions"},
                    {"role": "user", "content": "Test prompt"},
                    {"role": "assistant", "content": "Test response"}
                ]
            }

    def test_directory_creation(self):
        assert os.path.exists(self.test_dir)

    def test_multiple_appends(self):
        create_data_set("Instructions 1", "Prompt 1", "Response 1", filepath=self.test_file)
        create_data_set("Instructions 2", "Prompt 2", "Response 2", filepath=self.test_file)

        with open(self.test_file, 'r') as file:
            lines = file.readlines()
            assert len(lines) == 2
            data1 = json.loads(lines[0])
            data2 = json.loads(lines[1])
            assert data1["messages"][0]["content"] == "Instructions 1"
            assert data2["messages"][0]["content"] == "Instructions 2"

