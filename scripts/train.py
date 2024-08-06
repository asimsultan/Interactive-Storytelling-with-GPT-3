
import os
import json
import openai
import argparse
from flask import Flask, request, jsonify
from utils import generate_story

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data['prompt']
    story = generate_story(prompt, openai.api_key)
    return jsonify({'story': story})

def main(api_key, data_path):
    openai.api_key = api_key
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--api_key', type=str, required=True, help='OpenAI API key')
    parser.add_argument('--data_path', type=str, required=True, help='Path to the JSON file containing story framework')
    args = parser.parse_args()
    main(args.api_key, args.data_path)
