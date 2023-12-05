from korp.korp import Korp # funny import
from random import randint, choice
import sys
import spacy

def get_korp_concordance(query, corpora, params):
    n = randint(0,999)
    (_, [concordance]) = korp.concordance(query, corpora, start=n, end=n, additional_parameters=params)
    return concordance

def get_custom_concordance(query, corpus):
    concordances = []
    for sentence in corpus:
        for (i,token) in enumerate(sentence):
            if query(token):
                concordances.append((sentence,i))
    return choice(concordances)

def quiz(sentence):
    tokens = sentence["tokens"]
    matching_token = tokens[sentence["match"]["start"]]
    head = tokens[int(matching_token["dephead"]) - 1]
    question = ["<" + token["word"] + ">" if token == head else token["word"] for token in tokens if token != matching_token]
    print(" ".join(question).lower())
    correct_ans = " ".join([token["word"] for token in tokens])
    ans = input(matching_token["word"].lower() + "? ").lower()
    if len(ans.split()) >= 3 and matching_token["word"].lower() in ans and ans in correct_ans.lower():
        print("Correct!")
    else:
        print("Correct answer: " + correct_ans)

def to_korp_dict(concordance, corpus="OWN"):
    sentence,i = concordance
    korp_dict = {
        "corpus": corpus, 
        "match": { # simplification: only works for 1-token queries
            "position": i - 1,
            "start": i - 1,
            "end": i},
        "tokens": []}
    for token in sentence:
        korp_dict["tokens"].append({
            "word": token.text,
            "pos": token.pos_,
            "ref": str(token.i),
            "dephead": str(token.head.i),
        })
    return korp_dict

if len(sys.argv) > 1:
    path = sys.argv[1]
    with open(path) as f:
        strings = f.readlines()
    nlp = spacy.load("sv_core_news_lg")
    sentences = [nlp(string) for string in strings]
    query = lambda token: token.pos_ == "ADV"
    while True:
        concordance = to_korp_dict(get_custom_concordance(query,sentences))
        quiz(concordance)
        
else:
    korp = Korp(service_name='språkbanken')
    corpora = ["attasidor", "lasbart"]
    query = '[pos = "AB"]' 
    params = {
    "default_context": "1 sentence", # to get full sentences as results
    "show": ["ref", "word", "pos", "dephead"] # listing the information we are interested in
    }

    while True:
        concordance = get_korp_concordance(query, corpora, params)
        quiz(concordance)