from difflib import SequenceMatcher
import numpy as np
import json

with open('FILEPATH TO not_annotated_normative_text_9_test_articles.json', 'r') as file:
    not_annotated_normative_text_9_test_articles = json.load(file)
prompts =  not_annotated_normative_text_9_test_articles
with open('FILEPATH TO resultaten.json', 'r') as file:
    resultaten = json.load(file)
results = resultaten
with open('FILEPATH TO RASE_annotated_normative_text_9_test_articles.json', 'r') as file:
    RASE_annotated_normative_text_9_test_articles = json.load(file)
expected =  RASE_annotated_normative_text_9_test_articles

percentages = []

stap = 0
for prompt, result, expectation in zip(prompts['artikelen'], results['artikelen'], expected['artikelen']):
    stap += 1
    matcher = SequenceMatcher(None, result['geannoteerde_tekst'], expectation['geannoteerde_tekst'])
    similarity_percentage = matcher.ratio() * 100  
    percentages.append(similarity_percentage)
    print(f"Test {stap} with article {prompt['artikel_id'][5:7]}:")
    print(f"similarity percentage = {round(similarity_percentage,3)}")


print(f"\nMean percentage of all tests: {round(np.mean(percentages),3)}\n") 
