import os
# On demande au joueur de saisir un mot
word = input("Joueur 1 - Saisissez un mot : ")

# On efface la console pour cacher le mot saisi par le joueur 1
os.system('cls')

# On initialise le nombre de tentatives à 7
attempt = 7

# On déclare 2 listes:
# une contenant les lettres du mot saisi par le joueur 1
# une deuxième liste contenant les lettres trouvées par le joueur 2
list_letters = []
list_letters_founded = []

# on rempli les 2 listes
for letter in word:
    # le liste list_letters contient les lettres qui constitue le mot
    list_letters.append(letter)
    # la liste list_letters_founded contient au début du jeu que des "_" 
    list_letters_founded.append("_")

# Tant que le nombre de tentatives n'a pas été atteint 0
# et que toutes les lettres n'ont pas été trouvées, autre test possible list_letters != list_letters_founded
while attempt != 0 and "_" in list_letters_founded :
    # On affiche les lettres trouvées jusqu'alors, séparées par des espaces pour une meilleure visibilité
    for letter_founded in list_letters_founded:
        print(letter_founded, end=" ")

    # On demande au joueur 2 de saisir une lettre
    letter = input("\n\nJoueur 2 - Proposez une letter : ")

    # Si la lettre saisie par le joueur 2 est présente dans le liste contenant les lettres du mot
    # On ajoute la lettre dans la liste des lettres trouvés
    if letter in list_letters :
        # on remplace au(x) bon(s) index le "_" par la lettre trouvée 
        for i in range(len(list_letters)):
            if list_letters[i] == letter:
                list_letters_founded[i] = letter
    # Sinon on décrémente le nombre de tentatives
    # on affiche "Raté" avec le nombre de tentatives restantes
    else :
        attempt = attempt - 1
        print(f"Raté ! Plus que {attempt} tentative(s)")

# Si le nombre de tentatives n' pas atteint 0
# On affiche Gagné
if attempt != 0 :
    print("\n\nC'est gagné !!! :)")
# Sinon on affiche "Perdu"
else :
    print("\n\nC'est perdu :(")