
import openai

def generate_story(prompt, api_key):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100
    )
    story = response.choices[0].text.strip()
    return story
