import numpy as np
from Levenshtein import distance as levenshtein_distance

### TESTS for TA_dialoguemethod_txt2RASE_4trainingarticles.py ###

def similarity_score(str1, str2):
    """The Levenshtein distance: this measures how many operations (insertions, deletions, substitutions) 
    are needed to change one string to another. 
    A lower score means that the strings are more similar."""

    max_len = max(len(str1), len(str2)) 
    if max_len == 0:
        return 100  # both strings are empty, so 100% equal
    score = (1 - (levenshtein_distance(str1, str2) / max_len)) * 100
    return score
    


strings = [
    """RASE annotated text:

Art. 23.
<R> Bij <a> elke draaideur</a>, moet er gezorgd worden voor <r> een alternatieve toegang of deur, die niet draait</r>. <E> Deze verplichting geldt niet bij <a> draaideuren die uitgerust zijn met mechanismen</a> die <r> het gebruik door personen met een handicap garanderen</r>. </E> </R>""",
    """RASE annotated text:

Art. 23.
<R> Bij <a> elke draaideur</a>, moet er gezorgd worden voor <r> een alternatieve toegang of deur, die niet draait</r>. <E> Deze verplichting geldt niet bij <a> draaideuren die uitgerust zijn met mechanismen</a> die <r> het gebruik door personen met een handicap garanderen</r>. </E> </R>
""",
    """RASE annotated text:

Art. 23.
<R> Bij <a> elke draaideur </a>, moet er gezorgd worden voor <r> een alternatieve toegang of deur, die niet draait </r>. <E> Deze verplichting geldt niet bij <a> draaideuren die uitgerust zijn met mechanismen </a> die <r> het gebruik door personen met een handicap garanderen </r>. </E> </R>
""",
    """RASE annotated text:

Art. 23.
<R> Bij <a> elke draaideur</a>, moet er gezorgd worden voor <r> een alternatieve toegang of deur, die niet draait</r>. <E> Deze verplichting geldt niet bij <a> draaideuren die uitgerust zijn met mechanismen</a> die <r> het gebruik door personen met een handicap garanderen</r>. </E> </R>
""",
    """RASE annotated text:

Art. 23.
<R> Bij <a> elke draaideur </a>, moet er gezorgd worden voor <r> een alternatieve toegang of deur, die niet draait </r>. <E> Deze verplichting geldt niet bij <a> draaideuren die uitgerust zijn met mechanismen </a> die <r> het gebruik door personen met een handicap garanderen </r>. </E> </R>
""",
    """RASE annotated text:

Art. 23.
<R> Bij <a> elke draaideur</a>, moet er gezorgd worden voor <r> een alternatieve toegang of deur, die niet draait</r>. <E> Deze verplichting geldt niet bij <a> draaideuren die uitgerust zijn met mechanismen</a> die <r> het gebruik door personen met een handicap garanderen</r>. </E> </R>
""",
    """RASE annotated text:

Art. 23.
<R> Bij <a> elke draaideur </a>, moet er gezorgd worden voor <r> een alternatieve toegang of deur, die niet draait </r>. <E> Deze verplichting geldt niet bij <a> draaideuren die uitgerust zijn met mechanismen </a> die <r> het gebruik door personen met een handicap garanderen </r>. </E> </R>
""",
    """RASE annotated text:

Art. 23.
<R> Bij <a> elke draaideur</a>, moet er gezorgd worden voor <r> een alternatieve toegang of deur, die niet draait</r>. <E> Deze verplichting geldt niet bij <a> draaideuren die uitgerust zijn met mechanismen</a> die <r> het gebruik door personen met een handicap garanderen</r>. </E> </R>
""",
    """ RASE annotated text:

Art. 23.
<R> Bij <a> elke draaideur</a>, moet er gezorgd worden voor <r> een alternatieve toegang of deur, die niet draait</r>. <E> Deze verplichting geldt niet bij <a> draaideuren die uitgerust zijn met mechanismen</a> die <r> het gebruik door personen met een handicap garanderen</r>. </E> </R>
""",
    """RASE annotated text:

Art. 23.
<R> Bij <a> elke draaideur </a>, moet er gezorgd worden voor <r> een alternatieve toegang of deur, die niet draait </r>. <E> Deze verplichting geldt niet bij <a> draaideuren die uitgerust zijn met mechanismen </a> die <r> het gebruik door personen met een handicap garanderen </r>. </E> </R>
"""
]

# calculating the average similarity between all string combinations
scores = []
for i in range(len(strings)):
    for j in range(i + 1, len(strings)):
        scores.append(similarity_score(strings[i], strings[j]))
average_similarity = np.mean(scores)        
print(f"The average similarity between the tests is {average_similarity:.2f}%.")

# now with spaces removed -> more thoughtful
nieuwe_strings = []
zin = ''
for regel in strings:
    zin = ''
    for karakter in regel:
        if karakter != ' ':
            zin += karakter
    nieuwe_strings.append(zin)

scores_nieuw = []
for i in range(len(nieuwe_strings)):
    for j in range(i + 1, len(nieuwe_strings)):
        scores_nieuw.append(similarity_score(nieuwe_strings[i], nieuwe_strings[j]))
average_similarity1 = np.mean(scores_nieuw)

print(f"The average similarity between the tests (concatenated) is {average_similarity1:.2f}%.")
