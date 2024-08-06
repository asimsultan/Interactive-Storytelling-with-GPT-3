
import openai
import argparse
import json
from utils import generate_story

def main(api_key, data_path):
    openai.api_key = api_key

    with open(data_path, 'r') as f:
        story_framework = json.load(f)

    for prompt in story_framework['prompts']:
        story = generate_story(prompt, openai.api_key)
        print(f'Prompt: {prompt}')
        print(f'Story: {story}
')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--api_key', type=str, required=True, help='OpenAI API key')
    parser.add_argument('--data_path', type=str, required=True, help='Path to the JSON file containing story framework')
    args = parser.parse_args()
    main(args.api_key, args.data_path)
