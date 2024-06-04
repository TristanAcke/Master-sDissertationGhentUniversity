from openai import OpenAI
import json

client = OpenAI(api_key="FILL IN YOUR OWN API KEY")

with open('FILEPATH TO general_explanation_SHACL.json', 'r') as file:
    general_explanation_SHACL = json.load(file)

with open('FILEPATH TO general_explanation_RASE.json', 'r') as file:
    general_explanation_RASE = json.load(file)

with open('FILEPATH TO SHACL_RASE_explanation.json', 'r') as file:
    SHACL_RASE_general_explanation = json.load(file)

with open('FILEPATH TO shacl_articles.json', 'r') as file:
    shacl_articles = json.load(file)

with open('FILEPATH TO RASE_annotated_text.json', 'r') as file:
    RASE_annotated_text = json.load(file)

with open('FILEPATH TO RASE_annotated_normative_text_9_test_articles.json', 'r') as file:
    test_articles_RASE_annotated_text = json.load(file)

with open('FILEPATH TO buildingdata.json', 'r') as file:
    buildingdata = json.load(file)

with open('FILEPATH TO functions_SHACL.json', 'r') as file:
    functions = json.load(file)

geannoteerde_artikelen = []


messages = [
    {"role": "system", "content": f'General explanation of SHACL:\n{general_explanation_SHACL}'},
    {"role": "system", "content": f'General explanation of RASE:\n{general_explanation_RASE}'},
    {"role": "system", "content": f'Explanation of the use of and help of RASE in the conversion to SHACL:\n{SHACL_RASE_general_explanation}'},
    {"role": "system", "content": "Verdere info voor het beginnen van de omzetting: de correcte klasses van de toegepaste ontologie in de SHACL is hier terug te vinden: https://pi.pauwel.be/voc/buildingelement/index-en.html, dus verplicht dit te gebruiken voor de targetclasses etc."},
    ]

for rdf in buildingdata['Building Data in RDF']:
    messages.append({
            "role": "system",
            "content": f"Dit is bouwdata die gevalideerd moet worden. Dit is de data in RDF waarop de SHACL dus zal toegepast wordent:\n{rdf['RDF Extract']}"
        })
for functie in functions['Functions in SHACL']:
    messages.append({
            "role": "system",
            "content": f"Dit is hoe mathematische functies in SHACL worden gedefinieerd, alvorens ze te gebruiken in SHACL-vertalingen van de artikels. Functies in SHACL:\n{functie['Functions']}"
        })

for shape in shacl_articles['artikelen']:
    for RASE_annotated in RASE_annotated_text['artikelen']:
        if shape['artikel_id'] == 'None':
            if shape['artikel_id'] == RASE_annotated['artikel_id']:
                messages.append({
                        "role": "user",
                        "content": f"Artikel in RASE-geannoteerde tekst:\n{RASE_annotated['geannoteerde_tekst']}"
                    })
                messages.append({
                        "role": "system",
                        "content": f"Artikel in SHACL:\n{shape['SHACL_notatie']}"
                    })     
        else:
            if shape['artikel_id'] == RASE_annotated['artikel_id']:
                for RASE_annotated1 in RASE_annotated_text['artikelen']:
                    if shape['artikel_id'] == RASE_annotated1['artikel_id']:
                        messages.append({
                                "role": "user",
                                "content": f"Artikels in RASE-geannoteerde tekst:\n{RASE_annotated['artikel_id']}\n{RASE_annotated['geannoteerde_tekst']}\n{RASE_annotated1['artikel_id']}\n{RASE_annotated1['geannoteerde_tekst']}"
                            })
                        messages.append({
                                "role": "system",
                                "content": f"Artikels in SHACL:\n{shape['SHACL_notatie']}"
                            })        
messages.append({
        "role": "user",
        "content": f"Artikels in RASE-geannoteerde tekst:\n{test_articles_RASE_annotated_text['artikelen'][0]}"
    })

response = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=messages,
    temperature=0,
    top_p=0,
)

print(response.choices[0].message.content)

