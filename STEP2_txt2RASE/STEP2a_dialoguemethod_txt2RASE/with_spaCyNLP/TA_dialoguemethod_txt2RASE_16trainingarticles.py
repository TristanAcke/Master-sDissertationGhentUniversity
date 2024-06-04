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

text5 = (
   """Art. 18.
Niveauverschillen tot en met 18 cm moeten, zowel binnen als buiten, minstens met een helling overbrugd worden, met uitzondering van niveauverschillen tot twee cm in buitenruimtes of niveauverschillen tot twee cm bij een overgang tussen binnen- en buitenruimtes. Niveauverschillen van meer dan 18 cm moeten overbrugd worden, ofwel met een trap in combinatie met een helling, ofwel met een trap in combinatie met een lift, ofwel met een helling in combinatie met een lift. Ter uitvoering van artikel 33 en artikel 34, §1, kan in de aanvraag een afwijking van de verplichting tot het plaatsen van een lift worden opgenomen onder andere als in het aanvraagdossier gemotiveerd aangetoond wordt dat de aanvraag over een gebouw, bestemd voor industrie en ambacht, gaat, dat een of meer ruimtes op de gelijkvloerse verdieping eenzelfde functie hebben als de ruimtes op een andere verdieping die door het ontbreken van de lift ontoegankelijk zijn, en dat de totale oppervlakte die door de afwijking ontoegankelijk blijft, beperkt is tot ten hoogste vijfentwintig procent van de totale publiek toegankelijke oppervlakte. 
Ter uitvoering van artikel 33 en artikel 34, §1, kan in de aanvraag ook een afwijking op de verplichting tot het plaatsen van een lift worden opgenomen als in het aanvraagdossier aangetoond wordt dat de aanvraag over een gebouw bestemd voor toeristische verblijfsaccommodatie gaat en dat het gebouw na de handelingen twee of minder dan twee bouwlagen omvat en na de handelingen maximaal tien accommodaties beschikbaar zijn. 
""")
doc5 = nlp(text5)
antwoord5 = """RASE annotated text: 
Art. 18.
<R> <a> Niveauverschillen </a> <r> tot en met 18 cm </r> moeten, zowel binnen als buiten, minstens met een <r> helling </r> overbrugd worden, <e> met uitzondering van niveauverschillen <r> tot twee cm </r> in <s> buitenruimtes </s> of niveauverschillen <r> tot twee cm </r> bij een <s> overgang tussen binnen- en buitenruimtes </s> </e>. </R> <R> <a> Niveauverschillen </a> van <r> meer dan 18 cm </r> moeten overbrugd worden, ofwel met een <r> trap in combinatie met een helling </r>, ofwel met <r> een trap in combinatie met een lift </r>, ofwel met <r> een helling in combinatie met een lift </r>. </R> <E> Ter uitvoering van artikel 33 en artikel 34, §1, kan in de aanvraag een afwijking van de verplichting tot het plaatsen van een <a> lift </a> worden opgenomen onder andere als in het <r> aanvraagdossier gemotiveerd aangetoond wordt dat de aanvraag over een gebouw, bestemd voor industrie en ambacht, gaat, dat een of meer ruimtes op de gelijkvloerse verdieping eenzelfde functie hebben als de ruimtes op een andere verdieping die door het ontbreken van de lift ontoegankelijk zijn, en dat de totale oppervlakte die door de afwijking ontoegankelijk blijft, beperkt is tot ten hoogste vijfentwintig procent van de totale publiek toegankelijke oppervlakte </r>. </E>
<E> Ter uitvoering van artikel 33 en artikel 34, §1, kan in de aanvraag ook een afwijking op de verplichting tot het plaatsen van een <a> lift </a> worden opgenomen als in het <r> aanvraagdossier aangetoond wordt dat de aanvraag over een gebouw bestemd voor toeristische verblijfsaccommodatie gaat en dat het gebouw na de handelingen twee of minder dan twee bouwlagen omvat en na de handelingen maximaal tien accommodaties beschikbaar zijn </r>. </E>
"""

text6 = (
    """Art. 19.
§1. Het hellingspercentage bedraagt hoogstens:
1. tien procent bij niveauverschillen tot 10 cm, of in geval van buitenruimtes bij niveauverschillen van 2 tot en met 10 cm;
2. 8,3 procent bij niveauverschillen van 10 cm tot 25 cm;
3. 6,25 procent bij niveauverschillen van 25 cm tot 50 cm;
4. vijf procent bij niveauverschillen van 50 cm of groter. 
§2. Een combinatie van hellingen is toegestaan op voorwaarde dat gezorgd wordt voor een tussenbordes van 120 cm op 150 cm ter hoogte van de overgang. Als een combinatie van hellingen gepaard gaat met een verandering van richting, is een tussenbordes van 150 cm op 150 cm, ter hoogte van de richtingsverandering, vereist. 
§3. Bij hellingen met een hellingspercentage van meer dan vier procent moet zowel bovenaan als onderaan voor een vrije en vlakke draairuimte worden gezorgd. Die draairuimte mag maximaal twee procent in één richting hellen met het oog op de afwatering. 
§4. Bij een overbrugging van een niveauverschil van meer dan 50 cm of een helling van meer dan 10 m met een hellingspercentage van meer dan vier procent, moet voor een tussenbordes van 120 cm op 150 cm gezorgd worden. Als de helling verandert van richting, is een tussenbordes van 150 cm op 150 cm, ter hoogte van derichtingsverandering, vereist. 
§5. De breedte van een helling met een hellingspercentage van meer dan vier procent bedraagt minstens 145 cm, zodat na de afwerking van de eventuele wanden en met inbegrip van de ruimte voor eventuele plinten en leuningen een vrije en vlakke doorgangsbreedte van minstens 120 cm gegarandeerd wordt. 
§6. In de aanvraag kunnen afwijkingen worden opgenomen als in het aanvraagdossier gemotiveerd aangetoond wordt dat na de afwerking van de eventuele wanden een vrije en vlakke doorgangsbreedte, gemeten tussen de afgewerkte wanden en met inbegrip van eventuele leuningen en plinten, van minstens 120 cm gegarandeerd wordt. 
§7. Als een helling een niveauverschil van meer dan 10 cm overbrugt, moet aan de open zijkanten van de helling en aan de eventuele tussenbordessen over de volledige lengte van de helling voor een afrijdbeveiliging van minstens 5 cm hoogte gezorgd worden.
§8. (…)
§9. Aan de zijkanten van een helling die een niveauverschil van meer dan 25 cm overbrugt, moet aan beide zijden een leuning aangebracht worden, die doorloopt over eventuele
tussenbordessen. Voor het begin en aan het einde van de helling moet de leuning minstens 40 cm horizontaal verderlopen. Als de leuning in het ijle stopt, moet ze worden afgerond naar de grond of naar de wand. 
""")
doc6 = nlp(text6)
antwoord6 = """RASE annotated text: 
Art. 19.
§1. <R> Het <a> hellingspercentage </a> bedraagt <r> hoogstens </r>:
1. <r> tien procent </r> bij <a> niveauverschillen tot 10 cm </a>, <e> of in geval van <s> buitenruimtes </s> bij <a> niveauverschillen van 2 tot en met 10 cm </a> </e>;
2. <r> 8,3 procent </r> bij <a> niveauverschillen van 10 cm tot 25 cm </a>;
3. <r> 6,25 procent </r> bij <a> niveauverschillen van 25 cm tot 50 cm </a>;
4. <r> vijf procent </r> bij <a> niveauverschillen van 50 cm of groter </a>. </R>
§2. <R> Een <a> combinatie van hellingen </a> is toegestaan op voorwaarde dat gezorgd wordt voor een <r> tussenbordes van 120 cm op 150 cm <r> ter hoogte van de overgang. <E> Als een combinatie van hellingen gepaard gaat met een <s> verandering van richting </s>, is een <r> tussenbordes van 150 cm op 150 cm </r>, ter hoogte van de richtingsverandering, vereist. </E> </R>
§3. <R> Bij hellingen met een hellingspercentage van meer dan vier procent moet zowel bovenaan als onderaan voor een vrije en vlakke draairuimte worden gezorgd. Die draairuimte mag maximaal twee procent in één richting hellen met het oog op de afwatering. </R>
§4. <R> Bij een overbrugging van een <a> niveauverschil van meer dan 50 cm </a> of <a> een helling van meer dan 10 m met een hellingspercentage van meer dan vier procent </a>, moet voor een <r> tussenbordes van 120 cm op 150 cm </r> gezorgd worden. <E> Als de helling <s> verandert van richting </s>, is een <r> tussenbordes van 150 cm op 150 cm </r>, ter hoogte van de richtingsverandering, vereist. </E> </R>
§5. <R> De <a> breedte van een helling met een hellingspercentage van meer dan vier procent </a> bedraagt <r> minstens 145 cm </r>, zodat na de afwerking van de eventuele wanden en met inbegrip van de ruimte voor eventuele plinten en leuningen een <r> vrije en vlakke doorgangsbreedte van minstens 120 cm </r> gegarandeerd wordt. </R>
§6. <E> In de aanvraag kunnen afwijkingen worden opgenomen als in het aanvraagdossier gemotiveerd aangetoond wordt dat na de afwerking van de eventuele wanden een <r> vrije en vlakke doorgangsbreedte, gemeten tussen de afgewerkte wanden en met inbegrip van eventuele leuningen en plinten, van minstens 120 cm </r> gegarandeerd wordt. </E>
§7. <R> Als een <a> helling een niveauverschil van meer dan 10 cm overbrugt </a>, moet aan de <a>open zijkanten </a> van de helling en aan de eventuele <a> tussenbordessen </a> over de volledige lengte van de helling voor een <r> afrijdbeveiliging van minstens 5 cm </r> hoogte gezorgd worden. </R>
§8. (…)
§9. <R> Aan de zijkanten van een <a> helling die een niveauverschil van meer dan 25 cm overbrugt </a>, moet <r> aan beide zijden een leuning </r> aangebracht worden, die doorloopt over eventuele tussenbordessen. <a> Voor het begin en aan het einde van de helling </a> moet de leuning <r> minstens 40 cm horizontaal verderlopen </r>. Als de leuning in het ijle stopt, moet ze worden <r> afgerond naar de grond of naar de wand </r>. </R>
"""

text7 = (
    """Art. 20.
§1. Over de volledige lengte van de trappen en ter hoogte van eventuele tussenbordessen moet voor een breedte van minstens 125 cm gezorgd worden, telkens gemeten tussen de onafgewerkte binnenmuren, indien aanwezig, zodat na afwerking van de eventuele wanden en tussen de leuningen, een breedte van minstens 100 cm, vrij van obstakels, gegarandeerd wordt, wat gebruikers toelaat zich zonder hinder langs de trap te verplaatsen. 
§2. Na ten hoogste 17 treden moet voor een tussenbordes van minstens 100 cm diep gezorgd worden. 
§3. Alle treden moeten over een zo gelijkvormig mogelijke op- en aantrede beschikken. [De aantrede is de horizontale afstand tussen twee opeenvolgende trapneuzen, gelegen op de looplijn van twee opeenvolgende traptreden. De optrede is de verticale afstand tussen de bovenzijde van twee opeenvolgende treden.] De optrede mag hoogstens 18 cm meten en de aantrede moet minimaal 23 cm meten. De som van tweemaal de optrede en eenmaal de aantrede van elke trede moet tussen 57 cm en 63 cm bedragen of een veelvoud daarva. 
§4. Aan beide zijden van de trap moet een trapleuning aangebracht worden, die doorloopt ter hoogte van eventuele tussenbordessen. Voor het begin en aan het einde van de trap moet de trapleuning minstens 40 cm horizontaal verderlopen. Als de leuning in het ijle stopt, moet ze worden afgerond naar de grond of naar de wand. 
§5. Bij gebouwen als vermeld in artikel 5, eerste en tweede lid, moet niet voldaan worden aan de bepalingen van dit artikel, als het gebouw over een lift beschikt, die voldoet aan de bepalingen van artikel 21. 
""")
doc7 = nlp(text7)
antwoord7 = """RASE annotated text: 
Art. 20.
§1. <R> Over de volledige lengte van de <a> trappen </a> en ter hoogte van eventuele <a> tussenbordessen </a> moet voor een <r> breedte van minstens 125 cm </r> gezorgd worden, telkens gemeten tussen de onafgewerkte binnenmuren, indien aanwezig, , zodat na afwerking van de eventuele wanden en tussen de leuningen, een <r> breedte van minstens 100 cm </r>, vrij van obstakels, gegarandeerd wordt, wat gebruikers toelaat zich zonder hinder langs de trap te verplaatsen. </R>
§2. <R> Na <r> ten hoogste 17 treden </r> moet voor een <r> tussenbordes van minstens 100 cm </r> diep gezorgd worden. </R>
§3. <R> Alle <a> treden </a> moeten over een zo <r> gelijkvormig mogelijke op- en aantrede </r> beschikken. </R>[De aantrede is de horizontale afstand tussen twee opeenvolgende trapneuzen, gelegen op de looplijn van twee opeenvolgende traptreden. De optrede is de verticale afstand tussen de bovenzijde van twee opeenvolgende treden.] <R> De <a> optrede </a> mag <r> hoogstens 18 cm </r> meten en de <a> aantrede </a> moet <r> minimaal 23 cm </r> meten. </R> <R> De <a> som van tweemaal de optrede en eenmaal de aantrede </a> van elke trede moet <r> tussen 57 cm en 63 cm bedragen of een veelvoud daarvan </r>. </R>
§4. <R> Aan beide zijden van de <a> trap </a> moet een <r> trapleuning </r> aangebracht worden, die doorloopt ter hoogte van eventuele tussenbordessen. <a> Voor het begin en aan het einde van de trap </a> moet de trapleuning <r> minstens 40 cm horizontaal verderlopen </r>. Als de leuning in het ijle stopt, moet ze worden <r> afgerond naar de grond of naar de wand </r>. </R>
§5. <E> Bij gebouwen als vermeld in artikel 5, eerste en tweede lid, moet niet voldaan worden aan de bepalingen van dit artikel, als het gebouw over een lift beschikt, die voldoet aan de bepalingen van artikel 21. </E>
"""

text8 = (
    """Art. 21.
§1. Als een lift geïnstalleerd wordt, moet die in een afgesloten koker zitten of moet het om een verticale plateaulift gaan. Liften in een afgesloten koker moeten minstens liften zijn van het type 2 zoals omschreven in de EN 81-70. 
§2. Voor een lifttoegang moet een vrije en vlakke draairuimte zijn. 
§3. Liften die in een afgesloten koker geplaatst zijn, moeten automatische deuren hebben. De vrije en vlakke doorgangsbreedte van de liftdeur moet minstens 90 cm bedragen. 
§4. Bij verticale plateauliften moet het hefplateau minstens 100 cm breed en 140 cm diep zijn. 
§5. Over de volledige lengte van de plateaulift, alsook ter hoogte van de doorgangen van de deuren, moet een vrije en vlakke doorgangsbreedte van minstens 90 cm gegarandeerd worden. 
""")
doc8 = nlp(text8)
antwoord8 = """RASE annotated text: 
Art. 21.
§1. <R> Als een <a> lift </a> geïnstalleerd wordt, moet die in een <r> afgesloten koker </r> zitten of moet het om een <e> verticale plateaulift </e> gaan. <a> Liften in een afgesloten koker </a> moeten <r> minstens liften zijn van het type 2 </r> zoals omschreven in de EN 81-70. </R>
§2. <R> Voor een <a> lifttoegang </a> moet een <r> vrije en vlakke draairuimte </r> zijn. </R>
§3. <R> <a> Liften die in een afgesloten koker </a> geplaatst zijn, moeten <r> automatische deuren </r> hebben. De <a> vrije en vlakke doorgangsbreedte </a> van de liftdeur moet <r> minstens 90 cm </r> bedragen. </R>
§4. <R> Bij <a> verticale plateauliften </a> moet het <r> hefplateau minstens 100 cm breed en 140 cm diep </r> zijn. </R>
§5. <R> Over de volledige lengte van de <a> plateaulift </a>, alsook ter hoogte van de doorgangen van de deuren, moet een <r> vrije en vlakke doorgangsbreedte van minstens 90 cm </r> gegarandeerd worden. </R>
"""

text9 = (
    """Art. 22.
§1. Voor toegangen of deuropeningen moet, na afwerking, een vrije doorgangshoogte van minstens 2,09 meter gegarandeerd worden. 
§2. De ruwbouwmaten van toegangen of deuropeningen moeten minstens 105 cm breed zijn, zodat na afwerking een vrije en vlakke doorgangsbreedte van minstens 90 cm gegarandeerd wordt. Voor wat de ruwbouwmaten betreft van toegangsdeuren als vermeld in artikel 5 alinea 1, 2 en 3 kan een minimale breedte van 100 cm volstaan, mits na afwerking een vrije en vlakke doorgangsbreedte van minstens 85 cm gegarandeerd wordt. 
""")
doc9 = nlp(text9)
antwoord9 = """RASE annotated text: 
Art. 22.
§1. <R> Voor <a> toegangen of deuropeningen </a> moet, na afwerking, een <r> vrije doorgangshoogte van minstens 2,09 meter </r> gegarandeerd worden. </R>
§2. <R> De <a> ruwbouwmaten van toegangen of deuropeningen </a> moeten <r> minstens 105 cm</r> breed zijn, zodat na afwerking een <r> vrije en vlakke doorgangsbreedte van minstens 90 cm </r> gegarandeerd wordt. <E> Voor wat de <a> ruwbouwmaten betreft van toegangsdeuren als vermeld in artikel 5 alinea 1, 2 en 3 </a> kan een <r> minimale breedte van 100 cm </r> volstaan, mits na afwerking een <r> vrije en vlakke doorgangsbreedte van minstens 85 cm </r> gegarandeerd wordt. </E> </R>
"""

text10 = (
    """Art. 31.
In de aanvraag kunnen afwijkingen van de ruwbouwmaten, vermeld in artikel 30, worden opgenomen als in het aanvraagdossier gemotiveerd aangetoond wordt dat na de afwerking van de sanitaire ruimte aan de volgende voorwaarden is voldaan:
1. ter hoogte van de wastafel, de toiletpot en de douchezone is een vrije en vlakke draairuimte. De ruimte onder de aangepaste wastafel mag meegerekend worden voor de bepaling van de vrije en vlakke draairuimte; 
2. in een aangepast toilet:
a. moet voor de toiletpot en na de afwerking en inrichting van de ruimte een vrije afstand van minstens 120 cm gegarandeerd zijn;
b. moet minstens aan één zijde van de toiletpot een vrije transferzone van minstens 90 cm zijn;
c. moet de vrije doorgang tussen de toiletpot en de wastafel minstens 90 cm breed zijn;
d. moet de afstand van de voorzijde van de toiletpot tot tegen de achterliggende wand minstens 70 cm bedragen;
e. moet een wastafel aangebracht zijn waaronder een ruimte is van minstens 70 cm hoog, minstens 90 cm breed en minstens 60 cm diep. Als de wastafel in een inwendige hoek is geplaatst, moet de afstand tussen de as van de wastafel en de inwendige hoek minsten 50 cm bedragen; 
3. in een aangepaste doucheruimte:
a. moet de vloer van de douchezone drempelloos aansluiten op de vloer van de doucheruimte;
b. mag de vloer van de douchezone hoogstens twee procent hellen;
c. moet het vloeroppervlak van de douchezone na de afwerking van de wanden minstens 120 cm op 120 cm bedragen;
d. moet een douchezitje van minstens 45 cm diep en 40 cm breed aanwezig zijn. Als het douchezitje in een inwendige hoek is geplaatst, moet de afstand tussen de as van het douchezitje en de inwendige hoek minstens 45 cm bedragen; moet aan minstens één zijde van het douchezitje een vrije transferzone van minstens 90 cm zijn;
e. moet aan de voorzijde van het douchezitje een vrije ruimte van minstens 120 cm zijn;
f. moet de douchekraan aangebracht worden op een afstand tussen 45 en 55 cm van de wand waartegen het douchezitje geplaatst is. 
""")
doc10 = nlp(text10)
antwoord10 = """RASE annotated text: 
Art. 31.
<E> In de aanvraag kunnen <a> afwijkingen van de ruwbouwmaten </a>, vermeld in artikel 30, worden opgenomen als in het aanvraagdossier gemotiveerd aangetoond wordt dat na de afwerking van de sanitaire ruimte aan de volgende voorwaarden is voldaan:
1. <R> <a>ter hoogte van de wastafel, de toiletpot en de douchezone </a> is een <r> vrije en vlakke draairuimte </r>. De ruimte onder de aangepaste wastafel mag meegerekend worden voor de bepaling van de vrije en vlakke draairuimte; </R>
2. <R> in een <a> aangepast toilet </a>:
a. moet <a> voor de toiletpot </a> en na de afwerking en inrichting van de ruimte een <r> vrije afstand van minstens 120 cm </r> gegarandeerd zijn;
b. moet <a> minstens aan één zijde van de toiletpot </a> een <r> vrije transferzone van minstens 90 cm </r> zijn;
c. moet de <a> vrije doorgang tussen de toiletpot en de wastafel </a> <r> minstens 90 cm </r> breed zijn;
d. moet <a> de afstand van de voorzijde van de toiletpot tot tegen de achterliggende wand </a> <r> minstens 70 cm </r> bedragen;
e. moet <a> een wastafel </a> aangebracht zijn <r> waaronder een ruimte is van minstens 70 cm hoog, minstens 90 cm breed en minstens 60 cm diep </r>. <e> Als de wastafel in een inwendige hoek is geplaatst, moet <a> de afstand tussen de as van de wastafel en de inwendige hoek </a> <r> minsten 50 cm </r> bedragen </e>; </R>
3. <R> in een <a> aangepaste doucheruimte </a>:
a. moet <a> de vloer van de douchezone </a> <r> drempelloos aansluiten op de vloer van de doucheruimte </r>;
b. mag <a> de vloer van de douchezone </a> <r> hoogstens twee procent hellen </r>;
c. moet <a> het vloeroppervlak van de douchezone </a> na de afwerking van de wanden <r> minstens 120 cm op 120 cm </r> bedragen;
d. moet <a> een douchezitje </a> van <r> minstens 45 cm diep en 40 cm breed </r> aanwezig zijn. <e> Als het douchezitje in een inwendige hoek is geplaatst, moet de <a> afstand tussen de as van het douchezitje en de inwendige hoek </a> <r> minstens 45 cm </r> bedragen </e>; moet aan <a> minstens één zijde van het douchezitje </a> een <r> vrije transferzone van minstens 90 cm </r> zijn;
e. moet aan <a> de voorzijde van het douchezitje </a> een <r> vrije ruimte van minstens 120 cm </r> zijn;
f. moet de <a> douchekraan </a> aangebracht worden op een <r> afstand tussen 45 en 55 cm van de wand waartegen het douchezitje geplaatst is </r>. </R> </E>"""


text11 = (
    """Art. 11.
Indien een aanvraag valt onder het toepassingsgebied van deze stedenbouwkundige verordening, dan wordt in de stedenbouwkundige vergunning opgelegd dat de normbepalingen van hoofdstuk III dienen te worden nageleefd.
""")
doc11 = nlp(text11)
antwoord11 = """RASE annotated text: 
Art. 11.
<R> <a> Indien een aanvraag valt onder het toepassingsgebied van deze stedenbouwkundige verordening </a>, dan wordt in de stedenbouwkundige vergunning opgelegd dat de <r> normbepalingen van hoofdstuk III dienen te worden nageleefd </r>. </R>
"""

text12 = (
    """Art. 12.
§1. In alle delen van een constructie waarop dit besluit van toepassing is, moet voor een vrije en vlakke draairuimte worden gezorgd.
§2. Met behoud van de toepassing van artikel 22, alinea 1, moet in alle delen van een constructie waarop dit besluit van toepassing is, een vrije doorgangshoogte, na afwerking, van minstens 2,30 meter gegarandeerd worden. Deze verplichting geldt niet als de realisatie ervan tot een constructieprobleem leidt op bovenliggende verdiepingen waar geen werken aan gepland waren.
""")
doc12 = nlp(text12)
antwoord12 = """RASE annotated text: 
Art. 12.
§1. <R> In <a> alle delen van een constructie </a> waarop dit besluit van toepassing is, moet voor een <r> vrije en vlakke draairuimte </r> worden gezorgd. </R> 
§2. <R> Met behoud van de toepassing van artikel 22, alinea 1, moet in <a> alle delen van een constructie </a> waarop dit besluit van toepassing is, <r> een vrije doorgangshoogte, na afwerking, van minstens 2,30 meter </r> gegarandeerd worden. <E> Deze verplichting geldt niet als de realisatie ervan tot een constructieprobleem leidt op bovenliggende verdiepingen waar geen werken aan gepland waren. </E> </R>
"""

text13 = (
    """Art. 13.
Het traject naar de delen van een constructie die de publiek toegankelijke functie vervullen, moet met gids- of geleidelijnen aangeduid worden. [Met een geleidelijn wordt een speciaal voor de geleiding van blinden of slechtzienden aangebracht kunstmatig element bedoeld, dat voor blinden en slechtzienden bruikbaar is als oriëntatiepunt of als ononderbroken geleiding bij het lopen. Met een gidslijn wordt een natuurlijk in de ruimte aanwezig element bedoeld dat, hoewel het niet speciaal voor de geleiding van blinden of slechtzienden werd aangebracht, voor blinden en slechtzienden bruikbaar is als oriëntatiepunt of als ononderbroken geleiding bij het open.]
""")
doc13 = nlp(text13)
antwoord13 = """RASE annotated text: 
Art. 13.
<R> Het <a> traject naar de delen van een constructie die de publiek toegankelijke functie vervullen </a>, moet met <r> gids- of geleidelijnen </r> aangeduid worden. </R> [Met een geleidelijn wordt een speciaal voor de geleiding van blinden of slechtzienden aangebracht kunstmatig element bedoeld, dat voor blinden en slechtzienden bruikbaar is als oriëntatiepunt of als ononderbroken geleiding bij het lopen. Met een gidslijn wordt een natuurlijk in de ruimte aanwezig element bedoeld dat, hoewel het niet speciaal voor de geleiding van blinden of slechtzienden werd aangebracht, voor blinden en slechtzienden bruikbaar is als oriëntatiepunt of als ononderbroken geleiding bij het open.]
"""

text14 = (
    """Art. 14.
De breedte van een looppad dat zich niet tussen binnenmuren bevindt en dat niet valt onder de bepalingen van het besluit van de Vlaamse Regering van 29 april 1997 houdende vaststelling van een algemene bouwverordening inzake wegen voor voetgangersverkeer, bedraagt minstens 150 cm. In afwijking van het eerste lid is een versmalling van een dergelijk looppad toegestaan in de volgende gevallen:
1. bij een versmalling die zich over hoogstens 120 cm uitstrekt: als ter hoogte van die versmalling een doorgang van minstens 90 cm gegarandeerd wordt;
2. bij een versmalling die zich over meer dan 120 cm uitstrekt: als ter hoogte van die versmalling een doorgang van minstens 120 cm gegarandeerd wordt en minstens elke tien meter, alsook aan het begin en het einde van de versmalling, voor een vrije en vlakke draairuimte wordt gezorgd.
""")
doc14 = nlp(text14)
antwoord14 ="""RASE annotated text: 
Art. 14.
<R> De <a> breedte van een looppad </a> dat zich niet <e> tussen binnenmuren </e> bevindt en dat niet valt onder de <e> bepalingen van het besluit van de Vlaamse Regering van 29 april 1997 houdende vaststelling van een algemene bouwverordening inzake wegen voor voetgangersverkeer </e>, bedraagt <r> minstens 150 cm </r>. </R> <E>In afwijking van het eerste lid is een <a> versmalling </a> van een dergelijk looppad toegestaan in de volgende gevallen:
1. bij een versmalling die zich over <r> hoogstens 120 cm </r> uitstrekt: als ter hoogte van die versmalling een <r> doorgang van minstens 90 cm </r> gegarandeerd wordt; 
2. bij een versmalling die zich over <r> meer dan 120 cm uitstrekt </r>: als ter hoogte van die versmalling een <r> doorgang van minstens 120 cm </r> gegarandeerd wordt en <a> minstens elke tien meter </a>, alsook aan het <a> begin en het einde van de versmalling </a> voor een <r> vrije en vlakke draairuimte </r> wordt gezorgd. </E> 
"""

text15 = (
    """Art. 29/1.
Bij handelingen aan publiek toegankelijke kleedruimtes of pashokjes moet minstens vier procent van het totale aantal kleedruimtes of pashokjes na de handelingen aan de bepalingen van artikel 12 en van artikel 22 tot en met 26 voldoen. Ongeacht het totale aantal kleedruimtes of pashokjes na de handelingen moet minstens één kleedruimte of pashokje aan de bepalingen van artikel 12 en van artikel 22 tot en met 26 voldoen. Bij aparte kleedruimtes of pashokjes, die alleen voor vrouwen of alleen voor mannen bestemd zijn, moet telkens minstens één kleedruimte of pashokje in elke ruimte voldoen aan de bepalingen van artikel 12 en artikel 22 tot en met 26, tenzij de aangepaste kleedruimte of het aangepaste pashokje, bestemd voor zowel vrouwen als mannen, zich in een zone bevindt die niet gereserveerd is voor mannen dan wel vrouwen. Als het totale aantal nieuw te bouwen, te herbouwen, te verbouwen of uit te breiden kleedruimtes of pashokjes minder bedraagt dan vier procent van het totale aantal kleedruimtes of pashokjes, beperkt de verplichting van paragraaf 1 zich tot de nieuw te bouwen, te herbouwen, te verbouwen of uit te breiden kleedruimtes of pashokjes.
""")
doc15 = nlp(text15)
antwoord15 = """RASE annotated text: 
Art. 29/1.
<R> Bij <a> handelingen aan publiek toegankelijke kleedruimtes of pashokjes </a> moet <r> minstens vier procent van het totale aantal kleedruimtes of pashokjes na de handelingen aan de bepalingen van artikel 12 en van artikel 22 tot en met 26 voldoen </r>. Ongeacht het totale aantal kleedruimtes of pashokjes na de handelingen moet <r> minstens één kleedruimte of pashokje aan de bepalingen van artikel 12 en van artikel 22 tot en met 26 voldoen </r>. </R> <R> Bij <a> aparte kleedruimtes of pashokjes </a>, die alleen voor vrouwen of alleen voor mannen bestemd zijn, moet telkens <r> minstens één kleedruimte of pashokje in elke ruimte voldoen aan de bepalingen van artikel 12 en artikel 22 tot en met 26 </r>, <e> tenzij de aangepaste kleedruimte of het aangepaste pashokje, bestemd voor zowel vrouwen als mannen, zich in een zone bevindt die niet gereserveerd is voor mannen dan wel vrouwen </e>. </R> <E> Als het totale aantal nieuw te bouwen, te herbouwen, te verbouwen of uit te breiden kleedruimtes of pashokjes minder bedraagt dan vier procent van het totale aantal kleedruimtes of pashokjes, beperkt de verplichting van paragraaf 1 zich tot de nieuw te bouwen, te herbouwen, te verbouwen of uit te breiden kleedruimtes of pashokjes. </E>
"""

text16 = (
    """Art. 29/2.
Bij handelingen aan publiek toegankelijke toiletten moet in elk sanitair blok minstens één toilet voldoen aan de bepalingen van artikel 12, 30, eerste lid en artikel 31, inzonderheid 1° en 2°. Bij handelingen aan publiek toegankelijke doucheruimtes, moet in elk sanitair blok minstens één douche voldoen aan de bepalingen van artikel 12, 30, tweede en derde alinea, artikel 31, inzonderheid 1° en 3° en artikel 31/1. Bij aparte toiletten of doucheruimtes, die alleen voor vrouwen of alleen voor mannen bestemd zijn, moet telkens minstens één toilet of doucheruimte in elke zone voldoen aan de bepalingen van artikel 12 en artikel 30 tot en met 31/1, tenzij het aangepast toilet of de aangepaste doucheruimte, bestemd voor zowel vrouwen als mannen, zich in een zone bevindt die niet gereserveerd is voor mannen dan wel vrouwen.
""")
doc16 = nlp(text16)
antwoord16 = """RASE annotated text: 
Art. 29/2.
<R> Bij <a> handelingen aan publiek toegankelijke toiletten </a> moet <r> in elk sanitair blok minstens één toilet voldoen aan de bepalingen van artikel 12, 30, eerste lid en artikel 31, inzonderheid 1° en 2° </r>. </R> <R> Bij <a> handelingen aan publiek toegankelijke doucheruimtes </a>, moet <r> in elk sanitair blok minstens één douche voldoen aan de bepalingen van artikel 12, 30, tweede en derde alinea, artikel 31, inzonderheid 1° en 3° en artikel 31/1 </r>. </R> <R> Bij <a> aparte toiletten of doucheruimtes </a>, die alleen voor vrouwen of alleen voor mannen bestemd zijn, moet telkens <r> minstens één toilet of doucheruimte in elke zone voldoen aan de bepalingen van artikel 12 en artikel 30 tot en met 31/1 </r>, <e> tenzij het aangepast toilet of de aangepaste doucheruimte, bestemd voor zowel vrouwen als mannen, zich in een zone bevindt die niet gereserveerd is voor mannen dan wel vrouwen </e>. </R>
"""

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
""" )
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
    "content": "Not annotated text: Art. 11.\n Indien een aanvraag valt onder het toepassingsgebied van deze stedenbouwkundige verordening , dan wordt in de stedenbouwkundige vergunning opgelegd dat de  normbepalingen van hoofdstuk III dienen te worden nageleefd. \n\nRASE annotated text: Art. 11.\n<R> <a> Indien een aanvraag valt onder het toepassingsgebied van deze stedenbouwkundige verordening </a>, dan wordt in de stedenbouwkundige vergunning opgelegd dat de <r> normbepalingen van hoofdstuk III dienen te worden nageleefd </r>. </R>\n"
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
    "content": "Not annotated text: Afdeling II. Bepalingen met betrekking tot looppaden naar constructies en naar de daarin gelegen vertrekken:\nArt. 14.\n De  breedte van een looppad  dat zich niet  tussen binnenmuren  bevindt en dat niet valt onder de  bepalingen van het besluit van de Vlaamse Regering van 29 april 1997 houdende vaststelling van een algemene bouwverordening inzake wegen voor voetgangersverkeer , bedraagt  minstens 150 cm.  In afwijking van het eerste lid is een  versmalling  van een dergelijk looppad toegestaan in de volgende gevallen: 1. bij een versmalling die zich over  hoogstens 120 cm  uitstrekt: als ter hoogte van die versmalling een  doorgang van minstens 90 cm  gegarandeerd wordt; 2. bij een versmalling die zich over  meer dan 120 cm uitstrekt : als ter hoogte van die versmalling een  doorgang van minstens 120 cm  gegarandeerd wordt en  minstens elke tien meter , alsook aan het  begin en het einde van de versmalling  voor een  vrije en vlakke draairuimte  wordt gezorgd. \n\nRASE annotated text: Afdeling II. Bepalingen met betrekking tot looppaden naar constructies en naar de daarin gelegen vertrekken:\nArt. 14.\n<R> De <a> breedte van een looppad </a> dat zich niet <e> tussen binnenmuren </e> bevindt en dat niet valt onder de <e> bepalingen van het besluit van de Vlaamse Regering van 29 april 1997 houdende vaststelling van een algemene bouwverordening inzake wegen voor voetgangersverkeer </e>, bedraagt <r> minstens 150 cm </r>. </R> <E>In afwijking van het eerste lid is een <a> versmalling </a> van een dergelijk looppad toegestaan in de volgende gevallen: 1. bij een versmalling die zich over <r> hoogstens 120 cm </r> uitstrekt: als ter hoogte van die versmalling een <r> doorgang van minstens 90 cm </r> gegarandeerd wordt; 2. bij een versmalling die zich over <r> meer dan 120 cm uitstrekt </r>: als ter hoogte van die versmalling een <r> doorgang van minstens 120 cm </r> gegarandeerd wordt en <a> minstens elke tien meter </a>, alsook aan het <a> begin en het einde van de versmalling </a> voor een <r> vrije en vlakke draairuimte </r> wordt gezorgd. </E> \n    "
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
    "content": f"Prompt for GPT-4:\nNot annotated text: {text5} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse(doc5)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text5} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse1(doc5)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text5} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse2(doc5)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text5} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse3(doc5)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text5} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse4(doc5)}"
    },
    {
    "role": "assistant",
    "content": f"{antwoord5}"
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text6} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse(doc6)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text6} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse1(doc6)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text6} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse2(doc6)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text6} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse3(doc6)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text6} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse4(doc6)}"
    },
    {
    "role": "assistant",
    "content": f"{antwoord6}"
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text7} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse(doc7)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text7} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse1(doc7)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text7} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse2(doc7)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text7} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse3(doc7)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text7} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse4(doc7)}"
    },
    {
    "role": "assistant",
    "content": f"{antwoord7}"
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text8} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse(doc8)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text8} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse1(doc8)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text8} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse2(doc8)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text8} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse3(doc8)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text8} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse4(doc8)}"
    },
    {
    "role": "assistant",
    "content": f"{antwoord8}"
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text9} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse(doc9)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text9} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse1(doc9)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text9} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse2(doc9)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text9} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse3(doc9)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text9} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse4(doc9)}"
    },
    {
    "role": "assistant",
    "content": f"{antwoord9}"
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text10} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse(doc10)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text10} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse1(doc10)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text10} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse2(doc10)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text10} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse3(doc10)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text10} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse4(doc10)}"
    },
    {
    "role": "assistant",
    "content": f"{antwoord10}"
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text11} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse(doc11)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text11} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse1(doc11)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text11} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse2(doc11)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text11} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse3(doc11)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text11} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse4(doc11)}"
    },
    {
    "role": "assistant",
    "content": f"{antwoord11}"
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text12} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse(doc12)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text12} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse1(doc12)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text12} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse2(doc12)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text12} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse3(doc12)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text12} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse4(doc12)}"
    },
    {
    "role": "assistant",
    "content": f"{antwoord12}"
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text13} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse(doc13)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text13} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse1(doc13)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text13} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse2(doc13)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text13} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse3(doc13)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text13} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse4(doc13)}"
    },
    {
    "role": "assistant",
    "content": f"{antwoord13}"
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text14} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse(doc14)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text14} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse1(doc14)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text14} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse2(doc14)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text14} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse3(doc14)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text14} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse4(doc14)}"
    },
    {
    "role": "assistant",
    "content": f"{antwoord14}"
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text15} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse(doc15)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text15} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse1(doc15)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text15} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse2(doc15)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text15} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse3(doc15)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text15} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse4(doc15)}"
    },
    {
    "role": "assistant",
    "content": f"{antwoord15}"
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text16} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse(doc16)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text16} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse1(doc16)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text16} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse2(doc16)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text16} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse3(doc16)}"
    },
    {
    "role": "assistant",
    "content":"Everything carefully noted for developing a RASE annotated text."
    },
    {
    "role": "user",
    "content": f"Prompt for GPT-4:\nNot annotated text: {text16} \n\nContext of the text above (made with spaCy) to understand the structure of the text:{analyse4(doc16)}"
    },
    {
    "role": "assistant",
    "content": f"{antwoord16}"
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


