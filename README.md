
# Interactive Storytelling with GPT-3

Welcome to the Interactive Storytelling with GPT-3 project! This project focuses on building an interactive storytelling application using the GPT-3 model.

## Introduction

Interactive storytelling involves creating stories based on user prompts. In this project, we leverage GPT-3 to generate stories using a framework of prompts and deploy the application with a web interface.

## Dataset

For this project, we will use a custom JSON file containing story prompts. You can create your own dataset and place it in the `data/story_framework.json` file.

## Project Overview

### Prerequisites

- Python 3.6 or higher
- OpenAI API
- Flask
- Torch

### Installation

To set up the project, follow these steps:

```bash
# Clone this repository and navigate to the project directory:
git clone https://github.com/asimsultan/interactive_storytelling_gpt3.git
cd interactive_storytelling_gpt3

# Install the required packages:
pip install -r requirements.txt

# Ensure your data includes story prompts. Place these files in the data/ directory.
# The data should be in a JSON file with an array of prompts.

# To deploy the interactive storytelling application, run the following command:
python scripts/train.py --api_key YOUR_OPENAI_API_KEY --data_path data/story_framework.json

# To evaluate the generated stories, run:
python scripts/evaluate.py --api_key YOUR_OPENAI_API_KEY --data_path data/story_framework.json
