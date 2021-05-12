import tkinter as tk

def decalage(lettre_message):
    a=ord(lettre_message)
    if (a > 90 and 97 > a) or 65 > a  :
        return chr(ord(lettre_message) + 0)
    elif a > 122  or (97 > a and a > 90)  :
        return chr(ord(lettre_message) + 0)
    if a == 90  :
        return chr(ord('A'))
    if a == 122  :
        return chr(ord('a'))
    else :
        return chr(ord(lettre_message) + 1)


def dec_texte(texte):
    texte_code = ""
    t= 0
    taille = longueur_cle(texte)
    print(taille)
    while len(texte_code) < len(texte):
      texte_code += decalage(texte[t])
      t = t + 1
    return texte_code


def chiffre():
    resultat.delete(0, tk.END)
    resultat.insert(0, dec_texte(entree_texte.get()))

def ic(texte):
    chaine = que_des_majuscules(texte,0)
    frequences = [0]*26
    n = len(chaine)
    for c in chaine:
        frequences[ord(c)-65] += 1
    indice = 0.0
    for ni in frequences:
        indice += ni*(ni-1)
    return indice/(n*(n-1))

def longueur_cle(texte):
    # devine la longueur de la cle avec l'indice de coincidence
    seuil = 0.06
    ok = False
    k = 0
    while not ok and k<20:
        partiel = ""
        k += 1
        j = 0
        while j < len(texte):
            partiel += texte[j]
            j += k
        ok = ic(partiel)>seuil
    return k
    print (k)

racine=tk.Tk()
racine.title("Cryptographie")

entree_texte = tk.Entry(racine, width = 50, font = ("helvetica", "20"))
entree_texte.grid(row = 0, column = 0)

label_texte = tk.Label(racine,font = ("helvetica", "20"), text = "Entrer le message ici.")
label_texte.grid(row = 0, column = 1)

bouton_coder=tk.Button(racine, text="Chiffrer texte",fg="black", width=15, command=chiffre)
bouton_coder.grid(row=2, column=0)

jj=tk.Button(racine, text="Chiffrer texte",fg="black", width=15, command=longueur_cle)
jj.grid(row=3, column=5)


resultat=tk.Entry(racine,width = 50, font = ("helvetica", "20"))
resultat.grid(row=3,column=0)

label_res=tk.Label(racine,font = ("helvetica", "20"), text="Déchiffement ici.")
label_res.grid(row = 3, column=1)

racine.mainloop()

