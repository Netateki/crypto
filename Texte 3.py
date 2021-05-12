import tkinter as tk


def decalage(lettre_message, lettre_cle):
    a = ord(lettre_message)
    c = ord(lettre_cle)
    b = 0
    d = 0
    r = 0
    p = 0
    if (a > 96 and 123 > a):
        al = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
        for i in al :
            if i==a :
                b=al.index(i)
                print(b)
        for i in al :
            if i==c :
                d = al.index(i)
                print(d)
        r = b + d
        if r > 25 :
            r = r % 26

        print ("r = ",r)
        print(al[r])
        p = al[r]
        print (p)
        print(chr(p))
        return chr(p)
    else:
        return chr(ord(lettre_message) + 0)


def dec_texte(texte, cle):
    texte_code = ""
    t, c = 0, 0
    while len(texte_code) < len(texte):
        texte_code += decalage(texte[t], cle[c])
        t, c = t + 1, c + 1
        if c == len(cle):
            c = 0
    return texte_code


def chiffre():
    resultat.delete(0, tk.END)
    if entree_texte.get() == "" or entree_cle.get() == "":
        resultat.insert(0, "Il manque quelque chose en entrée :/")
    resultat.insert(0, dec_texte(entree_texte.get(), entree_cle.get()))


def dechiffrement(texte_a_decoder, cle):
    texte_decode = ""
    t, c = 0, 0
    while len(texte_decode) < len(texte_a_decoder):
        texte_decode += decalage(texte_a_decoder[t], chr(256 - ord(cle[c])))
        t, c = t + 1, c + 1
        if c == len(cle):
            c = 0
    return texte_decode


def dechiffre():
    if entree_texte.get() == "" or entree_cle.get() == "":
        resultat.insert(0, "Il manque quelque chose en entrée :/")
    else:
        label_res.config(text=dechiffrement(resultat.get(), entree_cle.get()))


def chiffre_xor(lettre_message, lettre_cle):
    return chr(ord(lettre_message) ^ ord(lettre_cle))


racine = tk.Tk()
racine.title("Cryptographie")

entree_texte = tk.Entry(racine, width=50, font=("helvetica", "20"))
entree_texte.grid(row=0, column=0)

entree_cle = tk.Entry(racine, width=50, font=("helvetica", "20"))
entree_cle.grid(row=1, column=0)

label_texte = tk.Label(racine, font=("helvetica", "20"), text="Entrer le message ici.")
label_texte.grid(row=0, column=1)

label_cle = tk.Label(racine, font=("helvetica", "20"), text="Entrer la clé ici.")
label_cle.grid(row=1, column=1)

bouton_coder = tk.Button(racine, text="Chiffrer texte", fg="black", width=15, command=chiffre)
bouton_coder.grid(row=2, column=0)

bouton_decoder = tk.Button(racine, text="Déchiffrer texte", fg="black", width=15, command=dechiffre)
bouton_decoder.grid(row=2, column=1)

resultat = tk.Entry(racine, width=50, font=("helvetica", "20"))
resultat.grid(row=3, column=0)

label_res = tk.Label(racine, font=("helvetica", "20"), text="Déchiffement ici.")
label_res.grid(row=3, column=1)

racine.mainloop()