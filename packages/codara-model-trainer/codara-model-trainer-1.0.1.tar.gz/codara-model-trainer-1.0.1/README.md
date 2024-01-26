# codara-model-trainer

## Overview

The `codara-model-trainer` is a Python package designed to assist in creating datasets for fine-tuning machine learning
models, particularly language models. It simplifies the process of gathering and formatting training data in a JSON
Lines (JSONL) format.

## Features

- Easy creation of training data sets in JSONL format.
- Methods to set system instructions, training prompts, and generative responses.
- Automatically handles file creation and appending data in the correct format.

## Installation

No specific installation is required apart from having Python installed. The script uses standard Python libraries `os`
and `json`.

## Usage

1. Import the package:
   ```python
   from codara_model_trainer import FineTuningDataCreator
   ```

2. Create an instance of `FineTuningDataCreator`:
   ```python
   data_creator = FineTuningDataCreator()
   ```

3. Create the data set with agent instructions, training prompts, and generative responses as needed:
   ```python
   gpt_response = openai_api_call("User prompt here")
   data_creator.create_data_set("System instructions here", "User prompt here", gpt_response)
   ```

The data will be saved in the `model-training/fine-tune-data-set.jsonl` file.

## Structure of Data

The data is structured in JSON Lines format, where each line is a valid JSON object. An example of the data structure:

```json
{
  "messages": [
    {
      "role": "system",
      "content": "System instructions here"
    },
    {
      "role": "user",
      "content": "User prompt here"
    },
    {
      "role": "assistant",
      "content": "Model response here"
    }
  ]
}
```
