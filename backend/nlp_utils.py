import spacy

nlp = spacy.load("en_core_web_sm")

def humanize_name(name):
    words = name.replace("_", " ")
    doc = nlp(words)

    verb_map = {
        "get": "Gets",
        "set": "Sets",
        "calculate": "Calculates",
        "compute": "Computes",
        "check": "Checks",
        "update": "Updates"
    }

    first = doc[0].text.lower()
    rest = " ".join([t.text for t in doc[1:]])

    if first in verb_map:
        return f"{verb_map[first]} {rest}."
    else:
        return f"Handles {words}."
