import tkinter as tk

def decalage(lettre_message):
    a=ord(lettre_message)
    if a==97  :
        return chr(ord('b') + 0)
    elif a==99 :
        return chr(ord('d') + 0)
    elif a == 100  :
        return chr(ord('n'))
    elif a == 102  :
        return chr(ord('m'))
    elif a == 103  :
        return chr(ord('l'))
    elif a == 105  :
        return chr(ord('s'))
    elif a == 107  :
        return chr(ord('i'))
    elif a == 108  :
        return chr(ord('h'))
    elif a == 110  :
        return chr(ord('a'))
    elif a == 111  :
        return chr(ord('r'))
    elif a == 113  :
        return chr(ord('p'))
    elif a == 115  :
        return chr(ord('o'))
    elif a == 117  :
        return chr(ord('t'))
    elif a == 118  :
        return chr(ord('c'))
    elif a == 119  :
        return chr(ord('f'))
    elif a == 120  :
        return chr(ord('e'))
    elif a == 121  :
        return chr(ord('u'))
    else :
        return chr(ord(lettre_message) + 0)


def dec_texte(texte):
    texte_code = ""
    t= 0
    while len(texte_code) < len(texte):
      texte_code += decalage(texte[t])
      t = t + 1
    return texte_code


def chiffre():
    resultat.delete(0, tk.END)
    resultat.insert(0, dec_texte(entree_texte.get()))


racine=tk.Tk()
racine.title("Cryptographie")

entree_texte = tk.Entry(racine, width = 50, font = ("helvetica", "20"))
entree_texte.grid(row = 0, column = 0)

label_texte = tk.Label(racine,font = ("helvetica", "20"), text = "Entrer le message ici.")
label_texte.grid(row = 0, column = 1)

bouton_coder=tk.Button(racine, text="Chiffrer texte",fg="black", width=15, command=chiffre)
bouton_coder.grid(row=2, column=0)


resultat=tk.Entry(racine,width = 50, font = ("helvetica", "20"))
resultat.grid(row=3,column=0)

label_res=tk.Label(racine,font = ("helvetica", "20"), text="Déchiffement ici.")
label_res.grid(row = 3, column=1)

racine.mainloop()

