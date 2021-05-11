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
    
    

def minute(min, min2):
    
    # fonction qui permet de soustraire des minute 
    a = datetime.timedelta(minutes=min)
    b = datetime.timedelta(minutes=min2)

    return b - a
    logging.info("calcule la soustraction en minute")

def converter(heure):
    heure1 = int(heure[0:2])*60 + int(heure[3:5])
    heure2 = int(heure[6:8])*60 + int(heure[9:11])
    return heure2 - heure1

def relever_valeur():
    # l = lecture('planning.log')
    f = open('planning.log', "r", encoding="utf-8")
    # l = l[0:10]
    # for i in f.readlines():
    f =  f.readlines()
    valeur_min = []
    for i in f:
        if i != '\n':
            valeur_min.append(converter(i[0:11]))
    # valeur_min ="".join(valeur_min)        
    return valeur_min 
            # print(converter(i[0:11]))

def theme():
    f = open('planning.log',"r", encoding="utf-8")
    texte = f.readlines()
    nom_valeur = []
    for i in texte:
        if i != '\n':
            nom_valeur.append(i[12:-1])
            # print(i[12:-1])
    return nom_valeur
    
def regroupement(dict1, dict2):
    dict_from_list = {}
    for t in dict1:
        for r in dict2:
            dict_from_list[t] = r
            dict2.remove(r)
            break
    return dict_from_list

    # dict_from_list = dict(zip(dict1, dict2))
    # return dict_from_list 




print(theme())
print(relever_valeur())
print(regroupement(theme(),relever_valeur() ))

# print(converter('09:20-11:00')) 
    





# print(relever_valeur())


# print(minute(221,222))

# print(lecture('planning.log'))



# f = open("planning.log", "r", encoding="utf-8")

#     texte = f.read()
#     texte = texte.strip("\n")


# time = ['09:20', '11:00']

# print(type(time))


# print(time int([0]-[1]))

# a = datetime.timedelta(hours=9, minutes=20)
# b = datetime.timedelta(hours=11, minutes=0)

# print(b-a)


    # return newline

    # print(newline)

