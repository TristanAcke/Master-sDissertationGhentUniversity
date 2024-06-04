from openai import OpenAI
import spacy

nlp = spacy.load("nl_core_news_lg")
client = OpenAI(api_key="FILL IN YOUR OWN API KEY")

### training data ###
text1 = (
   """Het fietspad voor fietsers en bakfietsen moet een minimale breedte van 1 meter hebben, behalve indien in de 2 rijrichtingen het fietspad gekruist wordt, dan dient deze doorgang 2,2 meter breed te zijn.""")
doc1 = nlp(text1)
antwoord1 = """RASE annotated text: <R> Het <a>fietspad</a> voor <s>fietsers</s> en <s>bakfietsen</s> moet <r>een minimale breedte van 1 meter</r> hebben, <E>behalve indien in de 2 rijrichtingen het fietspad gekruist wordt, dan dient <a>deze doorgang</a> <r>2,2 meter breed</r> te zijn</E>. </R>"""

text2 = (
    """Art. 15.\n De breedte van een looppad, gemeten tussen onafgewerkte binnenmuren, bedraagt minstens 175 cm, zodat na de afwerking van de wanden en met inbegrip van de ruimte voor plinten en leuningen een vrije en vlakke doorgangsbreedte van minstens 150 cm gegarandeerd wordt. In de aanvraag kunnen afwijkingen op de ruwbouwmaten worden opgenomen als in het aanvraagdossier gemotiveerd aangetoond wordt dat na de afwerking van de wanden een vrije en vlakke doorgangsbreedte, gemeten tussen de afgewerkte wanden met inbegrip van eventuele leuningen en plinten, van minstens 150 cm gegarandeerd wordt. \n In afwijking van lid 1 en 2 is een versmalling van een dergelijk looppad toegestaan in de\nvolgende gevallen:\n1. bij een versmalling die zich over hoogstens 120 cm uitstrekt: als de breedte van het\nlooppad, gemeten tussen de onafgewerkte binnenmuren, minstens 115 cm bedraagt,\nzodat na afwerking van de wanden en met inbegrip van de ruimte voor plinten steeds een vrije en vlakke doorgangsbreedte van minstens 90 cm gegarandeerd wordt;\n2. bij een versmalling die zich over meer dan 120 cm uitstrekt: als de breedte van het\nlooppad, gemeten tussen de onafgewerkte binnenmuren, minstens 145 cm bedraagt,\nzodat na afwerking van de wanden en met inbegrip van de ruimte voor plinten een vrije en vlakke doorgangsbreedte van minstens 120 cm gegarandeerd wordt. In dit laatste geval moet minstens elke tien meter alsook aan het begin en het einde van de versmalling, voor een vrije en vlakke draairuimte worden gezorgd.\n""")
doc2 = nlp(text2)
antwoord2 = """RASE annotated text: \n\nArt. 15.\n<R> De <a> breedte van een looppad, gemeten tussen onafgewerkte binnenmuren </a>, bedraagt <r> minstens 175 cm </r>, zodat na de afwerking van de wanden en met inbegrip van de ruimte voor plinten en leuningen een <r> vrije en vlakke doorgangsbreedte van minstens 150 cm </r> gegarandeerd wordt. </R> <E> In de aanvraag kunnen afwijkingen op de ruwbouwmaten worden opgenomen als in het aanvraagdossier gemotiveerd aangetoond wordt dat na de afwerking van de wanden een <a> vrije en vlakke doorgangsbreedte, gemeten tussen de afgewerkte wanden met inbegrip van eventuele leuningen en plinten </a>, van <r> minstens 150 cm </r> gegarandeerd wordt. </E> \n<E> In afwijking van lid 1 en 2 is een <a> versmalling van een dergelijk looppad </a> toegestaan in de\nvolgende gevallen:\n1. bij een versmalling die zich over <r> hoogstens 120 cm </r> uitstrekt: als de <a> breedte van het\nlooppad, gemeten tussen de onafgewerkte binnenmuren </a>, <r> minstens 115 cm </r> bedraagt,\nzodat na afwerking van de wanden en met inbegrip van de ruimte voor plinten steeds een <r> vrije en vlakke doorgangsbreedte van minstens 90 cm </r> gegarandeerd wordt;\n2. bij een versmalling die zich over <r> meer dan 120 cm </r> uitstrekt: als de <a> breedte van het\nlooppad, gemeten tussen de onafgewerkte binnenmuren </a>, <r> minstens 145 cm </r> bedraagt,\nzodat na afwerking van de wanden en met inbegrip van de ruimte voor plinten een <r> vrije en vlakke doorgangsbreedte van minstens 120 cm </r> gegarandeerd wordt. In dit laatste geval moet <a> minstens elke tien meter </a>, alsook aan het <a> begin en het einde van de versmalling </a>, voor een <r> vrije en vlakke draairuimte </r> worden gezorgd. </E>\n"""

text3 = (
    """Art. 16.\nEen looppad mag alleen hellen in de richting dwars op de normale looprichting om\neen normale afwatering te verzekeren.""")
doc3 = nlp(text3)
antwoord3 = """RASE annotated text: \n\nArt. 16.\n<R> Een <a> looppad </a> mag alleen <r> hellen in de richting dwars op de normale looprichting om\neen normale afwatering te verzekeren </r>. </R>"""

text4 = (
    """Art. 17.\nBij handelingen waarbij brandhaspels, brandblusapparaten of andere uit de wand stekende constructies geïnstalleerd worden, mogen die constructies het ongestoord gebruik van het looppad niet in het gedrang brengen. [Hiertoe kunnen die apparaten in een nis ingewerkt worden zodat ze niet buiten het afgewerkte muurvlak uitsteken.]""")
doc4 = nlp(text4)
antwoord4 = """RASE annotated text: \n\nArt. 17.\n<R> Bij <a> handelingen waarbij brandhaspels, brandblusapparaten of andere uit de wand stekende\nconstructies </a> geïnstalleerd worden, mogen die constructies het <r> ongestoord gebruik van het\nlooppad niet in het gedrang brengen </r>. </R> [Hiertoe kunnen die apparaten in een nis ingewerkt worden zodat ze niet buiten het afgewerkte muurvlak uitsteken.]"""

### spaCy analyses ###
def analyse(toegang_doc):
    analyse = "\n"
    analyse += "Analysis 1: keywords of the text fragment:"
    for chunk in toegang_doc.noun_chunks:
        analyse += "\n"
        analyse += f"\t{chunk}"
    return analyse

def analyse1(toegang_doc):
    analyse1 = "\n\n"
    analyse1 += "Analysis 2: analysis of the text fragment using part-of-speech tags (.pos_):"
    analyse1 += "\n\tZelfstandige naamwoorden (noun) [NOUN]:" + str([token.text for token in toegang_doc if "NOUN" in token.pos_])
    analyse1 += "\n\tWerkwoorden [VERB]:" + str([token.lemma_ for token in toegang_doc if "VERB" in token.pos_])
    analyse1 += "\n\tHulp-/Koppelwerkwoorden (auxiliary verb) [AUX]:" + str([token.lemma_ for token in toegang_doc if "AUX" in token.pos_])
    analyse1 += "\n\tPersoonlijk voornaamwoord (pronoun) [PRON]:" + str([token.text for token in toegang_doc if "PRON" in token.pos_])
    analyse1 += "\n\tEigennamen (proper noun) [PROPN]:" + str([token.text for token in toegang_doc if "PROPN" in token.pos_])
    analyse1 += "\n\tVoorzetsels (adposition) [ADP]:" + str([token.text for token in toegang_doc if "ADP" in token.pos_])
    analyse1 += "\n\tOnderschikkend voegwoord (subordinating conjunction) [SCONJ]:" + str([token.text for token in toegang_doc if "SCONJ" in token.pos_])
    analyse1 += "\n\tNederschikkend voegwoord (coordinating conjunction) [CCONJ]:" + str([token.text for token in toegang_doc if "CCONJ" in token.pos_])
    analyse1 += "\n\tLidwoord (determiner)[DET]:" + str([token.text for token in toegang_doc if "DET" in token.pos_])
    analyse1 += "\n\tBijwoorden (adverb) [ADV]:" + str([token.lemma_ for token in toegang_doc if "ADV" in token.pos_])
    analyse1 += "\n\tBijvoeglijk voornaamwoord (adjective) [ADJ]:" + str([token.text for token in toegang_doc if "ADJ" in token.pos_])
    analyse1 += "\n\tLeestekens [PUNCT]:" + str([token.text for token in toegang_doc if "PUNCT" in token.pos_])
    analyse1 += "\n\tCijfergetallen (numeral) [NUM]:" + str([token.text for token in toegang_doc if "NUM" in token.pos_])
    return analyse1

def analyse2(toegang_doc):
    analyse2 = "\n"
    zin = ''
    for token in toegang_doc:
        zin += token.text + '[' + str(token.pos_) + '] '
    analyse2 += "\n\t"  
    analyse2 += zin
    return analyse2

def analyse3(toegang_doc):
    analyse3 = "\n\n"
    analyse3 += "Analysis 3: analysis of the text fragment with labels using named-entity-recognition:"
    for entity in toegang_doc.ents:
        analyse3 += "\n"
        analyse3 += f"\t{entity.text} = {entity.label_}"
    return analyse3

def analyse4(toegang_doc):
    zin1 = ''
    analyse4 = "\n\n"
    analyse4 += "Analysis 4: analysis of the text fragment using dependency parsing (.dep_):"
    analyse4 += "\n\t1: Gebonden aan (headword) \n\t2: Soort gebondenheid/afhankelijkheid (dependency relationships)\n\n"
    for token in toegang_doc:
        zin1 += token.text + f"[1: {token.head.text}, 2: {token.dep_}] "
    analyse4 += f"\t{zin1}"
    return analyse4

### validation data ###
text = (
   """Art. Extra 02.
De verhouding van de hoogte tot de breedte van elke deuropening moet minimaal 2:1 zijn om te zorgen voor voldoende verticale ruimte.
""" 
)
doc = nlp(text)

analysis = analyse(doc)
analysis1 = analyse1(doc)
analysis2 = analyse2(doc)
analysis3 = analyse3(doc)
analysis4 = analyse4(doc)

### GPT interaction (ChatCompletions) ###
response = client.chat.completions.create(
model="gpt-4-1106-preview",
 messages=[
    {
    "role": "system",
    "content": "You'll learn RASE markup from extracts from a document and training sets of paired dutch texts (one unannotated, one RASE-annotated) that I will give you. After reviewing, respond with: \"Everything carefully noted for developing a RASE annotated text.\" Only when receiving a \"Prompt for GPT-4:\" with an unannotated dutch text and context about the text provided by SpaCy Natural Language Processing (this context will give you more insight into the given unannotated text) and only when receiving 'Analysis 4:' then apply your training to produce a dutch RASE-annotated version. Use only the provided materials to ensure accurate RASE annotations."
    },
    {
    "role": "user",
    "content": "You'll learn RASE markup from extracts from a document and training sets of paired texts (one unannotated, one RASE-annotated) that I will give you. After reviewing, respond with: \"Everything carefully noted for developing a RASE annotated text.\" Only when receiving a \"Prompt for GPT-4:\" with an unannotated text and context about the text provided by SpaCy Natural Language Processing (this context will give you more insight into the given unannotated text) and only when receiving 'Analysis 4:' then apply your training to produce a RASE-annotated version. Use only the provided materials to ensure accurate RASE annotations."
    },
    {
    "role": "assistant",
    "content": "Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": "The RASE markup methodology is a sophisticated approach designed to make normative texts, such as legal standards, building codes, or guidelines, accessible and interpretable both by machines for automated processing and by humans for understanding and review. This methodology hinges on four elemental operators: Requirements, Applicabilities, Selections, and Exceptions. Let's delve deeper into each component and provide a detailed practical example to illustrate how RASE markup can be applied to a specific text segment."
    },
    {
    "role": "assistant",
    "content": "Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": "Detailed Explanation of RASE Components:\nRequirements (R): These are explicit mandates within the text that specify actions that must be taken or conditions that must be met. They are often signaled by modal verbs like \"must\" or \"shall.\" In the context of building codes, a requirement might specify a minimum room size or the type of materials that must be used in certain constructions."
    },
    {
    "role": "assistant",
    "content": "Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": "Applicabilities (A): This aspect determines when, where, or to what the requirements apply. Applicabilities set the context or scope under which certain rules or standards are relevant. For example, certain building codes might only apply to residential buildings exceeding three stories."
    },
    {
    "role": "assistant",
    "content": "Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": "Selections (S): Selections offer options or alternatives within the regulations, allowing for flexibility in compliance. This might include a list of acceptable materials for a particular application, from which a builder can choose."
    },
    {
    "role": "assistant",
    "content": "Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": "Exceptions (E): Exceptions provide specific circumstances under which a requirement does not apply. This is crucial for accommodating unique situations or for clarifying the limits of a regulation's applicability."
    },
    {
    "role": "assistant",
    "content": "Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": "Practical Example of RASE Markup:\nConsider a segment of text from a hypothetical building code:\n\nThe access route for spedestrians wheelchair users shall not be steeper than 1:20. For distances of less than 3 metres, it may be steeper, but not more than 1:12.\n\n\nApplying RASE markup to this text would involve identifying and categorizing each part of the sentence according to the RASE framework:\n\nRequirement (R): \"not be steeper than 1:20\"\nApplicability (A): \"the access route\"\nSelection (S): Implicit in this case, as the selection is between the use for pedestrians and wheelchair users.\nException (E): The exception has is its own applicability and requirement in this case: The exception is for \"distance of less than 3 metres\" = \"For distances of less than 3 metres, it may be steeper, but not more than 1:12.\""
    },
    {
    "role": "assistant",
    "content": "Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": "How the Markup Happens:\nThe markup process involves closely reading the text to determine the intent and structure of the requirements. Each segment of the text is then annotated or tagged with the appropriate RASE element. This can be done manually by subject matter experts or semi-automatically using natural language processing tools designed to recognize and classify parts of the text based on the RASE framework.\n\nIn practice, this might look like adding specific tags around each portion of the text, such as <R>The <a>access route</a> for <s>pedestrians</s><s>wheelchair users</s> shall <r>not be steeper than 1:20</r>. <E>For <a>distances of less than 3 metres</a>, it may be steeper,but <r>not more than 1:12</r>.</E> </R>\n\nThese tags make the structure of the document clear for both human readers and software tools, facilitating easier interpretation, compliance checks, and automated processing."
    },
    {
    "role": "assistant",
    "content": "Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": "Conclusion:\nThe RASE markup method not only aids in the clear interpretation of normative texts by delineating requirements, applicabilities, selections, and exceptions but also ensures that these documents are ready for automated processing. This methodology enhances compliance checks, aids in the development of knowledge-based systems, and supports the digital transformation efforts within industries governed by complex regulations and standards."
    },
    {
    "role": "assistant",
    "content": "Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": "Now I will give you each time an example of the practice of tagging sentences with the use of RASE. In the prompt first there will be an unannotated text and secondly a RASE annotated text." 
    },
    {
    "role": "assistant",
    "content": "Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": "Not annotated text: Art. 11.\n Indien een aanvraag valt onder het toepassingsgebied van deze stedenbouwkundige verordening , dan wordt in de stedenbouwkundige vergunning opgelegd dat de  normbepalingen van hoofdstuk III dienen te worden nageleefd . \n\nRASE annotated text: Art. 11.\n<R> <a> Indien een aanvraag valt onder het toepassingsgebied van deze stedenbouwkundige verordening </a>, dan wordt in de stedenbouwkundige vergunning opgelegd dat de <r> normbepalingen van hoofdstuk III dienen te worden nageleefd </r>. </R>\n"
    },
    {
    "role": "assistant",
    "content": "Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": "Not annotated text: Art. 12.\n§1.  In  alle delen van een constructie  waarop dit besluit van toepassing is, moet voor een  vrije en vlakke draairuimte  worden gezorgd.  §2.  Met behoud van de toepassing van artikel 22, alinea 1, moet in  alle delen van een constructie  waarop dit besluit van toepassing is,  een vrije doorgangshoogte, na afwerking, van minstens 2,30 meter  gegarandeerd worden.  Deze verplichting geldt niet als de realisatie ervan tot een constructieprobleem leidt op bovenliggende verdiepingen waar geen werken aan gepland waren.  \n\nRASE annotated text: Art. 12.\n§1. <R> In <a> alle delen van een constructie </a> waarop dit besluit van toepassing is, moet voor een <r> vrije en vlakke draairuimte </r> worden gezorgd. </R> §2. <R> Met behoud van de toepassing van artikel 22, alinea 1, moet in <a> alle delen van een constructie </a> waarop dit besluit van toepassing is, <r> een vrije doorgangshoogte, na afwerking, van minstens 2,30 meter </r> gegarandeerd worden. <E> Deze verplichting geldt niet als de realisatie ervan tot een constructieprobleem leidt op bovenliggende verdiepingen waar geen werken aan gepland waren. </E> </R>\n\n"
    },
    {
    "role": "assistant",
    "content": "Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": "Not annotated text: Art. 13.\nHet  traject naar de delen van een constructie die de publiek toegankelijke functie vervullen , moet met  gids- of geleidelijnen  aangeduid worden.  [Met een geleidelijn wordt een speciaal voor de geleiding van blinden of slechtzienden aangebracht kunstmatig element bedoeld, dat voor blinden en slechtzienden bruikbaar is als oriëntatiepunt of als ononderbroken geleiding bij het lopen. Met een gidslijn wordt een natuurlijk in de ruimte aanwezig element bedoeld dat, hoewel het niet speciaal voor de geleiding van blinden of slechtzienden werd aangebracht, voor blinden en slechtzienden bruikbaar is als oriëntatiepunt of als \nononderbroken geleiding bij het open.]\n\nRASE annotated text: Art. 13.\n<R> Het <a> traject naar de delen van een constructie die de publiek toegankelijke functie vervullen </a>, moet met <r> gids- of geleidelijnen </r> aangeduid worden. </R> [Met een geleidelijn wordt een speciaal voor de geleiding van blinden of slechtzienden aangebracht kunstmatig element bedoeld, dat voor blinden en slechtzienden bruikbaar is als oriëntatiepunt of als ononderbroken geleiding bij het lopen. Met een gidslijn wordt een natuurlijk in de ruimte aanwezig element bedoeld dat, hoewel het niet speciaal voor de geleiding van blinden of slechtzienden werd aangebracht, voor blinden en slechtzienden bruikbaar is als oriëntatiepunt of als ononderbroken geleiding bij het open.]"
    },
    {
    "role": "assistant",
    "content": "Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": "Not annotated text: Afdeling II. Bepalingen met betrekking tot looppaden naar constructies en naar de daarin gelegen vertrekken:\nArt. 14.\n De  breedte van een looppad  dat zich niet  tussen binnenmuren  bevindt en dat niet valt onder de  bepalingen van het besluit van de Vlaamse Regering van 29 april 1997 houdende vaststelling van een algemene bouwverordening inzake wegen voor voetgangersverkeer , bedraagt  minstens 150 cm .  In afwijking van het eerste lid is een  versmalling  van een dergelijk looppad toegestaan in de volgende gevallen: 1. bij een versmalling die zich over  hoogstens 120 cm  uitstrekt: als ter hoogte van die versmalling een  doorgang van minstens 90 cm  gegarandeerd wordt; 2. bij een versmalling die zich over  meer dan 120 cm uitstrekt : als ter hoogte van die versmalling een  doorgang van minstens 120 cm  gegarandeerd wordt en  minstens elke tien meter , alsook aan het  begin en het einde van de versmalling  voor een  vrije en vlakke draairuimte  wordt gezorgd. \n\nRASE annotated text: Afdeling II. Bepalingen met betrekking tot looppaden naar constructies en naar de daarin gelegen vertrekken:\nArt. 14.\n<R> De <a> breedte van een looppad </a> dat zich niet <e> tussen binnenmuren </e> bevindt en dat niet valt onder de <e> bepalingen van het besluit van de Vlaamse Regering van 29 april 1997 houdende vaststelling van een algemene bouwverordening inzake wegen voor voetgangersverkeer </e>, bedraagt <r> minstens 150 cm </r>. </R> <E>In afwijking van het eerste lid is een <a> versmalling </a> van een dergelijk looppad toegestaan in de volgende gevallen: 1. bij een versmalling die zich over <r> hoogstens 120 cm </r> uitstrekt: als ter hoogte van die versmalling een <r> doorgang van minstens 90 cm </r> gegarandeerd wordt; 2. bij een versmalling die zich over <r> meer dan 120 cm uitstrekt </r>: als ter hoogte van die versmalling een <r> doorgang van minstens 120 cm </r> gegarandeerd wordt en <a> minstens elke tien meter </a>, alsook aan het <a> begin en het einde van de versmalling </a> voor een <r> vrije en vlakke draairuimte </r> wordt gezorgd. </E> \n    "
    },
    {
    "role": "assistant",
    "content": "Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": "Now we will start developing RASE annotated texts. So only when receiving context (made with spaCy) with 'Analysis 4:' then apply your training to produce a dutch RASE-annotated version."
    },
    {
    "role": "assistant",
    "content": "Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text1} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse(doc1)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text1} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse1(doc1)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text1} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse2(doc1)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text1} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse3(doc1)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text1} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse4(doc1)}"
    },
    {
    "role": "assistant",
    "content": f"{antwoord1}"
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text2} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse(doc2)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text2} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse1(doc2)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text2} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse2(doc2)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text2} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse3(doc2)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text2} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse4(doc2)}"
    },
    {
    "role": "assistant",
    "content": f"{antwoord2}"
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text3} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse(doc3)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text3} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse1(doc3)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text3} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse2(doc3)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text3} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse3(doc3)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text3} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse4(doc3)}"
    },
    {
    "role": "assistant",
    "content": f"{antwoord3}"
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text4} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse(doc4)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text4} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse1(doc4)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text4} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse2(doc4)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text4} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse3(doc4)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text4} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse4(doc4)}"
    },
    {
    "role": "assistant",
    "content": f"{antwoord4}"
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analysis}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analysis1}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analysis2}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analysis3}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analysis4}"
    }
],
temperature=0,
max_tokens=1000,
top_p=0.35,
frequency_penalty=0,
presence_penalty=0
)

print(response.choices[0].message.content)

