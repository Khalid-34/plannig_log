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




print(minute(221,222))

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

