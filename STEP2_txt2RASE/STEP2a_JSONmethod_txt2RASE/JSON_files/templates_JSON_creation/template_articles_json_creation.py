import re
import json


file_path = 'FILEPATH TO ...articles.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()


articles = re.findall(r'Art\.\s\d+\/?\d*.*?(?=\nArt\.|\Z)', text, flags=re.S)

article_list = []

for article in articles:
    article_lines = [line.strip() for line in article.split('\n') if line.strip()]
    article_list.append(article_lines)

artikelen = []
for text in article_list:
    if len(text) > 1:
        artikel = {
            "artikel_id": text[0],
            "tekst": " ".join(text[1:])
        }
    else:
        artikel = {
            "artikel_id": text[0],
            "tekst": ""
        }
    artikelen.append(artikel)

output = {"artikelen": artikelen}
output_path = 'FILEPATH TO ....json'


with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"De gegevens zijn opgeslagen in {output_path}.")
