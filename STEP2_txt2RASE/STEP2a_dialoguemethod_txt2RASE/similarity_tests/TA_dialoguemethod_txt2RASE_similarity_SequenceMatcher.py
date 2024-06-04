from difflib import SequenceMatcher
import numpy as np

percentages = []

### TESTS for TA_dialoguemethod_txt2RASE_16trainingarticles_nospaCy.py ###

##################
prompt1 = """Art. 23. Bij elke draaideur, moet er gezorgd worden voor een alternatieve toegang of deur, die niet draait. Deze verplichting geldt niet bij draaideuren die uitgerust zijn met mechanismen die het gebruik door personen met een handicap garanderen."""
result1 = """RASE annotated text: Art. 23 <R> Bij elke <a> draaideur </a>, moet er gezorgd worden voor een <r> alternatieve toegang of deur, die niet draait </r>. <E> Deze verplichting geldt niet bij <a> draaideuren die uitgerust zijn met mechanismen die het gebruik door personen met een handicap garanderen </a>. </E> </R>"""
expected1 = """RASE annotated text: Art. 23. <R> Bij elke <a> draaideur </a>, moet er gezorgd worden voor een <r> alternatieve toegang of deur, die niet draait </r>. <E> Deze verplichting geldt niet bij <a> draaideuren die uitgerust zijn met mechanismen die het gebruik door personen met een handicap garanderen </a>. </E> </R>"""


matcher = SequenceMatcher(None, result1, expected1)
similarity_percentage = matcher.ratio() * 100 
percentages.append(similarity_percentage)

print(f"Test 1 with article {prompt1[5:7]}:")
print(f"similarity percentage = {round(similarity_percentage, 3)}")

##################
prompt2 = """Art. 24.
Vóór en achter elke toegang of deur waarop dit besluit van toepassing is, met uitsluiting van toegangen tot of deuren naar gesloten trappenhallen, moet voor een vrije en vlakke draairuimte worden gezorgd, die maximaal twee procent in één richting mag hellen met het oog op de afwatering. [De vrije en vlakke draairuimtes van meerdere deuren mogen elkaar overlappen. Het draaivlak van een deur moet vlak zijn.] Bij manueel te bedienen deuren moet de buitenste rand van de vrije en vlakke draairuimte aan de trekzijde van de deur, het draaivlak van de deur raken en moet de buitenste rand van de vrije en vlakke draairuimte aan de duwzijde van de deur, het gesloten deurvlak raken."""
result2 = """RASE annotated text: Art. 24. <R> Vóór en achter elke <a> toegang of deur waarop dit besluit van toepassing is </a>, met uitsluiting van <e> toegangen tot of deuren naar gesloten trappenhallen </e>, moet voor een <r> vrije en vlakke draairuimte </r> worden gezorgd, die maximaal <r> twee procent in één richting mag hellen </r> met het oog op de afwatering. </R> [De vrije en vlakke draairuimtes van meerdere deuren mogen elkaar overlappen. Het draaivlak van een deur moet vlak zijn.] <R> Bij <a> manueel te bedienen deuren </a> moet de <r> buitenste rand van de vrije en vlakke draairuimte aan de trekzijde van de deur, het draaivlak van de deur raken </r> en moet de <r> buitenste rand van de vrije en vlakke draairuimte aan de duwzijde van de deur, het gesloten deurvlak raken </r>. </R>"""
expected2 = """RASE annotated text: Art. 24. <R> <a> Vóór en achter elke toegang of deur </a> waarop dit besluit van toepassing is, met uitsluiting van <e> toegangen tot of deuren naar gesloten trappenhallen </e>, moet voor een <r> vrije en vlakke draairuimte </r> worden gezorgd, die <r> maximaal twee procent in één richting mag hellen </r> met het oog op de afwatering. </R> [De vrije en vlakke draairuimtes van meerdere deuren mogen elkaar overlappen. Het draaivlak van een deur moet vlak zijn.] <R> Bij <a> manueel te bedienen deuren </a> moet de <r> buitenste rand van de vrije en vlakke draairuimte aan de trekzijde van de deur, het draaivlak van de deur raken </r> en moet de <r> buitenste rand van de vrije en vlakke draairuimte aan de duwzijde van de deur, het gesloten deurvlak raken </r>.</R>"""


matcher2 = SequenceMatcher(None, result2, expected2)
similarity_percentage2 = matcher2.ratio() * 100 
percentages.append(similarity_percentage2)

print(f"Test 2 with article {prompt2[5:7]}:")
print(f"similarity percentage = {round(similarity_percentage2, 3)}")

##################
prompt3 = """Art. 25.
 Bij een manueel te bedienen deur, met uitsluiting van toegangen tot of deuren naar gesloten trappenhallen, moet naast de krukzijde voor een vrije en vlakke wand- en vloerbreedte worden gezorgd, met een ruwbouwmaat van minstens 45 cm, zodat na de afwerking een vrije en vlakke wand-en vloerbreedte van minstens 50 cm gegarandeerd wordt."""
result3 = """RASE annotated text: Art. 25. <R> Bij een <a> manueel te bedienen deur </a>, met uitsluiting van <e> toegangen tot of deuren naar gesloten trappenhallen </e>, moet <r> naast de krukzijde voor een vrije en vlakke wand- en vloerbreedte </r> worden gezorgd, met een <r> ruwbouwmaat van minstens 45 cm </r>, zodat na de afwerking een <r> vrije en vlakke wand-en vloerbreedte van minstens 50 cm </r> gegarandeerd wordt. </R>"""
expected3 = """RASE annotated text: Art. 25. <R> Bij een <a> manueel te bedienen deur </a>, met uitsluiting van <e> toegangen tot of deuren naar gesloten trappenhallen </e>, moet <r> naast de krukzijde voor een vrije en vlakke wand- en vloerbreedte </r> worden gezorgd, met een <r> ruwbouwmaat van minstens 45 cm </r>, zodat na de afwerking een <r> vrije en vlakke wand- en vloerbreedte van minstens 50 cm </r> gegarandeerd wordt. </R>"""


matcher3 = SequenceMatcher(None, result3, expected3)
similarity_percentage3 = matcher3.ratio() * 100 
percentages.append(similarity_percentage3)

print(f"Test 3 with article {prompt3[5:7]}:")
print(f"similarity percentage = {round(similarity_percentage3, 3)}")

##################
prompt4 = """Art. 26.
 Deuren die toegang verlenen tot aangepaste sanitaire voorzieningen, kleedruimtes of pashokjes, moeten naar buiten opendraaien."""
result4 = """RASE annotated text: Art. 26. <R> <a> Deuren die toegang verlenen tot aangepaste sanitaire voorzieningen, kleedruimtes of pashokjes </a>, moeten <r> naar buiten opendraaien </r>. </R>"""
expected4 = """RASE annotated text: Art. 26. <R> <a> Deuren die toegang verlenen tot aangepaste sanitaire voorzieningen, kleedruimtes of pashokjes </a>, moeten <r> naar buiten opendraaien </r>. </R>"""


matcher4 = SequenceMatcher(None, result4, expected4)
similarity_percentage4 = matcher4.ratio() * 100 
percentages.append(similarity_percentage4)

print(f"Test 4 with article {prompt4[5:7]}:")
print(f"similarity percentage = {round(similarity_percentage4, 3)}")

##################
prompt5 = """Art. 27.
 Als een constructie beschikt over één tot en met honderd eigen parkeerplaatsen, moet
 minstens zes procent van het totale aantal parkeerplaatsen, en minstens één parkeerplaats, een aangepaste parkeerplaats zijn. Vanaf vijf tot en met honderd eigen parkeerplaatsen, moeten de aangepaste parkeerplaatsen ook voorbehouden parkeerplaatsen zijn. Als een constructie beschikt over meer dan honderd eigen parkeerplaatsen, moet bovendien per extra schijf van vijftig parkeerplaatsen, telkens één parkeerplaats een aangepaste en voorbehouden parkeerplaats zijn. Als het totale aantal nieuw aan te leggen parkeerplaatsen minder bedraagt dan zes procent van het
totale aantal parkeerplaatsen, beperkt de verplichting van het eerste en het tweede lid zich tot de nieuw aan te leggen parkeerplaatsen. Een aangepaste parkeerplaats voldoet aan de volgende normen:
1. ze bevindt zich zo dicht mogelijk bij de toegankelijke ingang van de constructie of bij de
voetgangersuitgang van de parkeervoorziening;
2. bij dwarsparkeren en schuinparkeren bedraagt de breedte van de aangepaste
parkeerplaats minstens 350 cm en bij langsparkeren bedraagt de lengte van de
aangepaste parkeerplaats minstens 600 cm;
3. het oppervlak van de aangepaste parkeerplaats helt niet meer dan twee procent. 
[Om als voorbehouden parkeerplaats in aanmerking te komen, moet een parkeerplaats aan de bepalingen van de derde alinea voldoen en voorbehouden worden voor personen met een handicap conform het koninklijk besluit houdende algemeen reglement op de politie van het wegverkeer en van het gebruik van de openbare weg van 1 december 1975, en aangegeven volgens de bepalingen van het voormelde koninklijk besluit en het ministerieel besluit van 11 oktober 1976 waarbij de minimumafmetingen en de bijzondere plaatsingsvoorwaarden van de verkeerstekens worden bepaald.]
"""
result5 = """RASE annotated text: Art. 27. <R> Als een <a> constructie beschikt over één tot en met honderd eigen parkeerplaatsen </a>, moet <r> minstens zes procent van het totale aantal parkeerplaatsen </r>, en <r> minstens één parkeerplaats, een aangepaste parkeerplaats </r> zijn. <E> Vanaf <a> vijf tot en met honderd eigen parkeerplaatsen </a>, moeten de aangepaste parkeerplaatsen ook <r> voorbehouden parkeerplaatsen </r> zijn. </E> <E> Als een <a> constructie beschikt over meer dan honderd eigen parkeerplaatsen </a>, moet bovendien <a> per extra schijf van vijftig parkeerplaatsen </a>, telkens <r> één parkeerplaats een aangepaste en voorbehouden parkeerplaats </r> zijn. </E> <E> Als het totale aantal nieuw aan te leggen parkeerplaatsen minder bedraagt dan zes procent van het totale aantal parkeerplaatsen, beperkt de verplichting van het eerste en het tweede lid zich tot de nieuw aan te leggen parkeerplaatsen. </E> <R> Een <a> aangepaste parkeerplaats </a> voldoet aan de volgende normen: 1. <r> ze bevindt zich zo dicht mogelijk bij de toegankelijke ingang van de constructie of bij de voetgangersuitgang van de parkeervoorziening </r>; 2. bij <a> dwarsparkeren en schuinparkeren </a> bedraagt de <r> breedte van de aangepaste parkeerplaats minstens 350 cm </r> en bij <a> langsparkeren </a> bedraagt de <r> lengte van de aangepaste parkeerplaats minstens 600 cm </r>; 3. <r> het oppervlak van de aangepaste parkeerplaats helt niet meer dan twee procent </r>. </R> [E> Om als voorbehouden parkeerplaats in aanmerking te komen, moet een parkeerplaats aan de bepalingen van de derde alinea voldoen en voorbehouden worden voor personen met een handicap conform het koninklijk besluit houdende algemeen reglement op de politie van het wegverkeer en van het gebruik van de openbare weg van 1 december 1975, en aangegeven volgens de bepalingen van het voormelde koninklijk besluit en het ministerieel besluit van 11 oktober 1976 waarbij de minimumafmetingen en de bijzondere plaatsingsvoorwaarden van de verkeerstekens worden bepaald. </E>]"""
expected5 = """RASE annotated text: Art. 27. <R> Als een <a> constructie beschikt over één tot en met honderd eigen parkeerplaatsen </a>, moet <r> minstens zes procent van het totale aantal parkeerplaatsen </r>, en <r> minstens één parkeerplaats, een aangepaste parkeerplaats </r> zijn. Vanaf <a> vijf tot en met honderd eigen parkeerplaatsen </a>, moeten de aangepaste parkeerplaatsen ook <r> voorbehouden parkeerplaatsen </r> zijn. </R> <R> Als een <a> constructie beschikt over meer dan honderd eigen parkeerplaatsen </a>, moet bovendien <s> per extra schijf van vijftig parkeerplaatsen </s>, telkens <r> één parkeerplaats een aangepaste en voorbehouden parkeerplaats </r> zijn. </R> <E> Als het totale aantal nieuw aan te leggen parkeerplaatsen minder bedraagt dan zes procent van het totale aantal parkeerplaatsen, beperkt de verplichting van het eerste en het tweede lid zich tot de nieuw aan te leggen parkeerplaatsen. </E> <R> Een <a> aangepaste parkeerplaats </a> voldoet aan de volgende normen: 1. ze bevindt zich <r> zo dicht mogelijk bij de toegankelijke ingang van de constructie of bij de voetgangersuitgang van de parkeervoorziening </r>; 2. bij <s> dwarsparkeren en schuinparkeren </s> bedraagt de <r> breedte van de aangepaste parkeerplaats minstens 350 cm </r> en bij <a> langsparkeren </a> bedraagt de <r> lengte van de aangepaste parkeerplaats minstens 600 cm </r>; 3. <r> het oppervlak van de aangepaste parkeerplaats helt niet meer dan twee procent </r>. </R> [Om als voorbehouden parkeerplaats in aanmerking te komen, moet een parkeerplaats aan de bepalingen van de derde alinea voldoen en voorbehouden worden voor personen met een handicap conform het koninklijk besluit houdende algemeen reglement op de politie van het wegverkeer en van het gebruik van de openbare weg van 1 december 1975, en aangegeven volgens de bepalingen van het voormelde koninklijk besluit en het ministerieel besluit van 11 oktober 1976 waarbij de minimumafmetingen en de bijzondere plaatsingsvoorwaarden van de verkeerstekens worden bepaald.]"""


matcher5 = SequenceMatcher(None, result5, expected5)
similarity_percentage5 = matcher5.ratio() * 100 
percentages.append(similarity_percentage5)

print(f"Test 5 with article {prompt5[5:7]}:")
print(f"similarity percentage = {round(similarity_percentage5, 3)}")

##################
prompt6 = """Art. 28.
 Als een vast inrichtingselement met het oog op het onthaal van het publiek of een daarmee gelijkgestelde constructie wordt aangebracht, moet vóór dat element voor een vrije en vlakke draairuimte worden gezorgd. Aan alle elementen als vermeld in het eerste lid moet een verlaagd gedeelte aangebracht worden. Dehoogte tot de bovenzijde van het verlaagde gedeelte bedraagt hoogstens 80 cm. Onder het verlaagde gedeelte moet een opening zijn van minstens 70 cm hoog, minstens 90 cm breed en minstens 60 cm diep. 
"""
result6 = """RASE annotated text: Art. 28. <R> Als een <a> vast inrichtingselement met het oog op het onthaal van het publiek </a> of een daarmee gelijkgestelde constructie wordt aangebracht, moet <r> vóór dat element voor een vrije en vlakke draairuimte </r> worden gezorgd. </R> <R> Aan <a> alle elementen als vermeld in het eerste lid </a> moet een <r> verlaagd gedeelte </r> aangebracht worden. De <a> hoogte tot de bovenzijde van het verlaagde gedeelte </a> bedraagt <r> hoogstens 80 cm </r>. </R> <R> Onder het verlaagde gedeelte moet een opening zijn van <r> minstens 70 cm hoog, minstens 90 cm breed en minstens 60 cm diep </r>. </R>"""
expected6 = """RASE annotated text: Art. 28. <R> Als een <a> vast inrichtingselement met het oog op het onthaal van het publiek </a> of een daarmee gelijkgestelde constructie wordt aangebracht, moet <r> vóór dat element voor een vrije en vlakke draairuimte </r> worden gezorgd. </R> <R> Aan <a> alle elementen als vermeld in het eerste lid </a> moet een <r> verlaagd gedeelte </r> aangebracht worden. De <r> hoogte tot de bovenzijde van het verlaagde gedeelte bedraagt hoogstens 80 cm </r>. <r> Onder het verlaagde gedeelte moet een opening zijn van minstens 70 cm hoog, minstens 90 cm breed en minstens 60 cm diep </r>. </R>"""


matcher6 = SequenceMatcher(None, result6, expected6)
similarity_percentage6 = matcher6.ratio() * 100
percentages.append(similarity_percentage6)

print(f"Test 6 with article {prompt6[5:7]}:")
print(f"similarity percentage = {round(similarity_percentage6, 3)}")

##################
prompt7 = """Art. 29.
 Bij handelingen aan binnen- of buitenruimtes met vaste inrichtingselementen die dienst doen als zitplaatsen voor toeschouwers of toehoorders, moeten minstens twee vrije ruimtes gereserveerd worden voor personen met een handicap in elke ruimte met minder dan vijftig zitplaatsen waar een voorstelling wordt aangeboden. Elk van die vrije ruimtes moet minstens 90 cm breed en instens 140 cm diep zijn en moet zich bevinden op een vloer zonder niveauverschillen of hellingen. Op het toegangspad naar die vrije ruimtes en eraan grenzend moet in een vrije en vlakke draairuimte voorzien worden. Vanaf vijftig zitplaatsen en voor elke extra groep van vijftig zitplaatsen moet bijkomend voor minstens één extra vrije ruimte als vermeld in het eerste lid gezorgd worden. Als het totale aantal nieuw te bouwen, te herbouwen, te verbouwen of uit te breiden zitplaatsen minder bedraagt dan de te reserveren vrije ruimtes voor personen met een handicap als vermeld in het
eerste en tweede lid, beperkt die verplichting zich tot de nieuw te bouwen, te herbouwen, te verbouwen of uit te breiden zitplaatsen. 
"""
result7 = """RASE annotated text: Art. 29. <R> Bij <a> handelingen aan binnen- of buitenruimtes met vaste inrichtingselementen die dienst doen als zitplaatsen voor toeschouwers of toehoorders </a>, moeten <r> minstens twee vrije ruimtes gereserveerd worden voor personen met een handicap </r> in <a> elke ruimte met minder dan vijftig zitplaatsen waar een voorstelling wordt aangeboden </a>. Elk van die vrije ruimtes moet <r> minstens 90 cm breed en instens 140 cm diep </r> zijn en moet zich bevinden op een <r> vloer zonder niveauverschillen of hellingen </r>. Op het toegangspad naar die vrije ruimtes en eraan grenzend moet in een <r> vrije en vlakke draairuimte </r> voorzien worden. </R> <R> Vanaf vijftig zitplaatsen en voor elke extra groep van vijftig zitplaatsen moet bijkomend voor <r> minstens één extra vrije ruimte </r> als vermeld in het eerste lid gezorgd worden. </R> <E> Als het totale aantal nieuw te bouwen, te herbouwen, te verbouwen of uit te breiden zitplaatsen minder bedraagt dan de te reserveren vrije ruimtes voor personen met een handicap als vermeld in het eerste en tweede lid, beperkt die verplichting zich tot de nieuw te bouwen, te herbouwen, te verbouwen of uit te breiden zitplaatsen. </E>"""
expected7 = """RASE annotated text: Art. 29. <R> Bij <a> handelingen aan binnen- of buitenruimtes met vaste inrichtingselementen die dienst doen als zitplaatsen voor toeschouwers of toehoorders </a>, moeten <r> minstens twee vrije ruimtes gereserveerd worden voor personen met een handicap <r> in <s> elke ruimte met minder dan vijftig zitplaatsen waar een voorstelling wordt aangeboden </s>. Elk van die vrije ruimtes moet <r> minstens 90 cm breed en instens 140 cm diep </r> zijn en moet zich bevinden op een <r> vloer zonder niveauverschillen of hellingen </r>. Op het toegangspad naar die vrije ruimtes en eraan grenzend moet in een <r> vrije en vlakke draairuimte </r> voorzien worden. </R> <R> <a>Vanaf vijftig zitplaatsen en voor elke extra groep van vijftig zitplaatsen </a> moet bijkomend voor <r> minstens één extra vrije ruimte </r> als vermeld in het eerste lid gezorgd worden. </R> <E> Als het totale aantal nieuw te bouwen, te herbouwen, te verbouwen of uit te breiden zitplaatsen minder bedraagt dan de te reserveren vrije ruimtes voor personen met een handicap als vermeld in het eerste en tweede lid, beperkt die verplichting zich tot de nieuw te bouwen, te herbouwen, te verbouwen of uit te breiden zitplaatsen. </E>"""


matcher7 = SequenceMatcher(None, result7, expected7)
similarity_percentage7 = matcher7.ratio() * 100
percentages.append(similarity_percentage7)

print(f"Test 7 with article {prompt7[5:7]}:")
print(f"similarity percentage = {round(similarity_percentage7, 3)}")

###### EXTRA ARTICLES #####

##################
prompt8 = """Art. Extra 01. Elke deur moet exact één eigenschap hebben die de breedte van een deur aangeeft."""
result8 = """RASE annotated text: Art. Extra 01. <R> Elke <a> deur </a> moet <r> exact één eigenschap hebben die de breedte van een deur aangeeft </r>. </R>"""
expected8 = """RASE annotated text: Art. Extra 01. <R> <a> Elke deur </a> moet <r> exact één eigenschap </r> hebben die <r> de breedte van een deur aangeeft </r>. </R>"""

matcher8 = SequenceMatcher(None, result8, expected8)
similarity_percentage8 = matcher8.ratio() * 100
percentages.append(similarity_percentage8)

print(f"Test 8 with article {prompt8[5:13]}:")
print(f"similarity percentage = {round(similarity_percentage8,3)}")


##################
prompt9 = """Art. Extra 02. De verhouding van de hoogte tot de breedte van elke deuropening moet minimaal 2:1 zijn om te zorgen voor voldoende verticale ruimte."""
result9 = """RASE annotated text: Art. Extra 02. <R> De <a> verhouding van de hoogte tot de breedte van elke deuropening </a> moet <r> minimaal 2:1 zijn om te zorgen voor voldoende verticale ruimte </r>. </R>"""
expected9 = """RASE annotated text: Art. Extra 02. <R> De <a> verhouding van de hoogte tot de breedte van elke deuropening </a> moet <r> minimaal 2:1 zijn <r> om te zorgen voor voldoende verticale ruimte. </R>"""


matcher9 = SequenceMatcher(None, result9, expected9)
similarity_percentage9 = matcher9.ratio() * 100
percentages.append(similarity_percentage9)

print(f"Test 9 with article {prompt9[5:13]}:")
print(f"similarity percentage = {round(similarity_percentage9,3)}")

print(f"\nMean percentage of all tests: {round(np.mean(percentages),3)}\n") 