f = open("planning.log", "r", encoding="utf-8")

texte = f.read()

def minute():

    ligne = texte.readlines
    newline = ligne.split()

    return newline

    print(newline)