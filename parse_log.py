import datetime
import logging


def lecture(fichier):
    # fonction qui permet de ouvrire et de lire un fichier texte
    f = open(fichier, "r", encoding="utf-8")
    logging.info("ouverture du fichier")
    texte = f.read()
    logging.info("lecture du fichier")
    # texte = texte.strip("\n")
    return texte
    logging.info("retourne le fichier")
    
    

# def minute(min, min2):
    
#     # fonction qui permet de soustraire des minute 
#     a = datetime.timedelta(minutes=min)
#     b = datetime.timedelta(minutes=min2)

    # return b - a
    # logging.info("calcule la soustraction en minute")

def converter(heure):
    # fonction qui permet de soustraire des minute 
    heure1 = int(heure[0:2])*60 + int(heure[3:5])
    logging.info("releve la premier valeur en heure est la convertie en minute")
    heure2 = int(heure[6:8])*60 + int(heure[9:11])
    logging.info("releve la deuxième valeur en heure est la convertie en minute")
    return heure2 - heure1
    logging.info(f"fais de la soustraction des minute de {heure2} et {heure1}")

def relever_valeur():
    # l = lecture('planning.log')
    f = open('planning.log', "r", encoding="utf-8")
    logging.info("ouverture du fichier")
    # l = l[0:10]
    # for i in f.readlines():
    f =  f.readlines()
    valeur_min = []
    for i in f:
        if i != '\n':
            valeur_min.append(i[12:-1])
            valeur_min.append(converter((i[0:11])))
            logging.info("releve et convertir en minute")
    # valeur_min ="".join(valeur_min)        
    return valeur_min
    
            # print(converter(i[0:11]))

# print(relever_valeur())

def theme():
    f = open('planning.log',"r", encoding="utf-8")
    texte = f.readlines()
    nom_valeur = []
    for i in texte:
        if i != '\n':
            nom_valeur.append(i[12:-1])
            logging.info("releve les theme")
            # print(i[12:-1])
    return nom_valeur
    
def regroupement(dict1, dict2):
    dict_from_list = {}
    for t in dict1:
        for r in dict2:
            if t in dict_from_list:
                dict_from_list[t] += r
            else:
                dict_from_list[t] = r
    logging.info("retourne le regroupement sous forme de dict les donne de chaque tache ")
    return dict_from_list
    

    # dict_from_list = dict(zip(dict1, dict2))
    # return dict_from_list 

def test_dict(dicts):
    res = {}
    for i in dicts:
        key = i.split()[0]
        value = i.split()[1]
        print(key)
        print(value)
        if key in res:
            res[key]+= int(value)
        else:
            res[key]=int(value)
    return res


# print(theme())

print(relever_valeur())
# print(regroupement(theme(),relever_valeur()))
# test_dictdf=["Introduction 40", "Break 30", "Introduction 20"]
# res = {}
# for i in test_dict:
#     value = i.split()[0]
#     minu = i.split()[1]
#     print(minu)
#     print(value)

# print(test_dict(relever_valeur()))
# print(converter('09:20-11:00')) 
    













