from openai import OpenAI
import json

client = OpenAI(api_key="FILL IN YOUR OWN API KEY")

### loading .json files ###
### change X depending on the number of training items used ###
with open('FILEPATH TO general_explanation_RASE.json', 'r') as file:
    general_explanation = json.load(file)

with open('FILEPATH TO zone_explanation_not_annotated.json', 'r') as file:
    zone_explanation_not_annotated = json.load(file)

with open('FILEPATH TO zone_explanation_RASE_annotated.json', 'r') as file:
    zone_explanation_RASE_annotated = json.load(file)

with open('FILEPATH TO not_annotated_example.json', 'r') as file:
    not_annotated_example = json.load(file)

with open('FILEPATH TO RASE_annotated_example.json', 'r') as file:
    RASE_annotated_example = json.load(file)

with open('FILEPATH TO not_annotated_normative_text_X_training_articles.json', 'r') as file:
    not_annotated_normative_text_X_training_articles = json.load(file)

with open('FILEPATH TO RASE_annotated_normative_text_X_training_articles.json', 'r') as file:
    RASE_annotated_normative_text_X_training_articles = json.load(file)

with open('FILEPATH TO not_annotated_normative_text_9_test_articles.json', 'r') as file:
    not_annotated_normative_text_9_test_articles = json.load(file)



messages = [
    {"role": "system", "content": f'General explanation:\n{general_explanation}'},
    {"role": "system", "content": f'Explanations of the data points for not-annotated texts:\n{zone_explanation_not_annotated}'},
    {"role": "system", "content": f'Explanations of the data points for RASE-annotated texts:\n{zone_explanation_RASE_annotated}'},
    {"role": "system", "content": f'An example of a JSON input:\n{not_annotated_example}'},
    {"role": "system", "content": f'An example of the desired JSON output:\n{RASE_annotated_example}'},
    ]
for not_annotated, RASE_annotated in zip(not_annotated_normative_text_X_training_articles['artikelen'], RASE_annotated_normative_text_X_training_articles['artikelen']):
    messages.append({
            "role": "user",
            "content": f".json-file van niet-geannoteerde tekst: {not_annotated}"
        })
    messages.append({
            "role": "system",
            "content": f".json-output van RASE-geannoteerde tekst: {RASE_annotated}"
        })
messages.append({
        "role": "user",
        "content": f".json-file van niet-geannoteerde tekst: {not_annotated_normative_text_9_test_articles['artikelen'][8]}"
    })
response = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=messages,
    response_format={"type": "json_object"},
    temperature=0,
    top_p=0,
)

print(response.choices[0].message.content)

