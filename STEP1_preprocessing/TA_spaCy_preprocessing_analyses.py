import spacy
nlp = spacy.load("nl_core_news_lg")


text = (
   """Het fietspad voor fietsers en bakfietsen moet een minimale breedte van 1 meter hebben, behalve indien in de 2 rijrichtingen het fietspad gekruist wordt, dan dient deze doorgang 2,2 meter breed te zijn.""")
doc = nlp(text)


def analysis1(doc):
    analyse = "\n"
    analyse += "Analysis 1: keywords of the text fragment (.noun_chunks):"
    for chunk in doc.noun_chunks:
        analyse += "\n"
        analyse += f"\t{chunk}"
    return analyse

def analysis21(doc):
    analyse1 = "\n\n"
    analyse1 += "Analysis 2: analysis of the text fragment using part-of-speech tags (.pos_):"
    analyse1 += "\n\tZelfstandige naamwoorden (noun) [NOUN]:" + str([token.text for token in doc if "NOUN" in token.pos_])
    analyse1 += "\n\tWerkwoorden [VERB]:" + str([token.lemma_ for token in doc if "VERB" in token.pos_])
    analyse1 += "\n\tHulp-/Koppelwerkwoorden (auxiliary verb) [AUX]:" + str([token.lemma_ for token in doc if "AUX" in token.pos_])
    analyse1 += "\n\tPersoonlijk voornaamwoord (pronoun) [PRON]:" + str([token.text for token in doc if "PRON" in token.pos_])
    analyse1 += "\n\tEigennamen (proper noun) [PROPN]:" + str([token.text for token in doc if "PROPN" in token.pos_])
    analyse1 += "\n\tVoorzetsels (adposition) [ADP]:" + str([token.text for token in doc if "ADP" in token.pos_])
    analyse1 += "\n\tOnderschikkend voegwoord (subordinating conjunction) [SCONJ]:" + str([token.text for token in doc if "SCONJ" in token.pos_])
    analyse1 += "\n\tNederschikkend voegwoord (coordinating conjunction) [CCONJ]:" + str([token.text for token in doc if "CCONJ" in token.pos_])
    analyse1 += "\n\tLidwoord (determiner)[DET]:" + str([token.text for token in doc if "DET" in token.pos_])
    analyse1 += "\n\tBijwoorden (adverb) [ADV]:" + str([token.lemma_ for token in doc if "ADV" in token.pos_])
    analyse1 += "\n\tBijvoeglijk voornaamwoord (adjective) [ADJ]:" + str([token.text for token in doc if "ADJ" in token.pos_])
    analyse1 += "\n\tLeestekens [PUNCT]:" + str([token.text for token in doc if "PUNCT" in token.pos_])
    analyse1 += "\n\tCijfergetallen (numeral) [NUM]:" + str([token.text for token in doc if "NUM" in token.pos_])
    return analyse1

def analysis22(toegang_doc):
    analyse2 = "\n"
    zin = ''
    for token in toegang_doc:
        zin += token.text + '[' + str(token.pos_) + '] '
    analyse2 += "\n\t"  
    analyse2 += zin
    return analyse2

def analysis3(toegang_doc):
    analyse3 = "\n\n"
    analyse3 += "Analysis 3: analysis of the text fragment with labels using named-entity-recognition (.ents):"
    for entity in toegang_doc.ents:
        analyse3 += "\n"
        analyse3 += f"\t{entity.text} = {entity.label_}"
    return analyse3

def analysis4(toegang_doc):
    zin1 = ''
    analyse4 = "\n\n"
    analyse4 += "Analysis 4: analysis of the text fragment using dependency parsing (.dep_):"
    analyse4 += "\n\t1: Gebonden aan (headword) \n\t2: Soort gebondenheid/afhankelijkheid (dependency relationships)\n\n"
    for token in toegang_doc:
        zin1 += token.text + f"[1: {token.head.text}, 2: {token.dep_}] "
    analyse4 += f"\t{zin1}"
    return analyse4

analysis_spaCy = analysis1(doc) + analysis21(doc) + analysis22(doc) + analysis3(doc) + analysis4(doc)
print(analysis_spaCy)