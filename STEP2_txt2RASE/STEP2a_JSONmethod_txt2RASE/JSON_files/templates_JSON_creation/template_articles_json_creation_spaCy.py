import spacy
import json
import re


nlp = spacy.load("nl_core_news_lg")

file_path = 'FILEPATH TO ...articles.txt'


with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()


articles = re.findall(r'Art\.\s\d+\/?\d*.*?(?=\nArt\.|\Z)', text, flags=re.S)


article_list = []
for article in articles:
    article_lines = [line.strip() for line in article.split('\n') if line.strip()]
    article_list.append(article_lines)



def analyse_text(text):
    doc = nlp(text)
    keywords = [chunk.text for chunk in doc.noun_chunks]
    pos_tags = {
        "zelfstandige_naamwoorden_(noun)_[NOUN]": [token.text for token in doc if "NOUN" in token.pos_],
        "werkwoorden_(verb)_[VERB]": [token.lemma_ for token in doc if "VERB" in token.pos_],
        "hulp_koppelwerkwoorden_(auxiliary_verb)_[AUX]": [token.lemma_ for token in doc if "AUX" in token.pos_],
        "persoonlijk_voornaamwoord_(pronoun)_[PRON]": [token.text for token in doc if "PRON" in token.pos_],
        "eigennamen_(proper_noun)_[PROPN]": [token.text for token in doc if "PROPN" in token.pos_],
        "voorzetsels_(adposition)_[ADP]": [token.text for token in doc if "ADP" in token.pos_],
        "onderschikkend voegwoord_(subordinating_conjunction)_[SCONJ]": [token.text for token in doc if "SCONJ" in token.pos_],
        "nederschikkend voegwoord_(coordinating_conjunction)_[CCONJ]": [token.text for token in doc if "CCONJ" in token.pos_],
        "lidwoord_(determiner)_[DET]": [token.text for token in doc if "DET" in token.pos_],
        "bijwoorden_(adverb)_[ADV]": [token.lemma_ for token in doc if "ADV" in token.pos_],
        "bijvoeglijk_voornaamwoord_(adjective) [ADJ]": [token.text for token in doc if "ADJ" in token.pos_],
        "leestekens_(punctuation_mark)_[PUNCT]": [token.text for token in doc if "PUNCT" in token.pos_],
        "cijfergetallen_(numeral)_[NUM]": [token.text for token in doc if "NUM" in token.pos_]
    }
    named_entities = {ent.label_: ent.text for ent in doc.ents}
    dependency_parsing = " ".join([f"{token.text}[1: {token.head.text}, 2: {token.dep_}]" for token in doc])

    return {
        "keywords": keywords,
        "pos_tags": pos_tags,
        "named_entities": named_entities,
        "dependency_parsing": dependency_parsing
    }



artikelen = []
for text in article_list:
    if len(text) > 1:
        analysis = analyse_text(" ".join(text[1:]))
        artikelen.append({
            "artikel_id": text[0],
            "tekst": " ".join(text[1:]),
            "analyses": analysis
        })


output = {"artikelen": artikelen}
output_path = 'FILEPATH TO ....json'

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"De gegevens zijn opgeslagen in {output_path}.")