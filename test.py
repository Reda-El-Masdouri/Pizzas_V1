def trie_personnalise(e):
    return len(e)  # elle serve dans le tri des liste par longueur, on peut mettre return e pour trier par ordre alphab.

# Afficher les pizzas

def afficher(collection, nombre = -1):
#    collection.sort(reverse=True, key=trie_personnalise)  # pour trier par ordre alphabétique notre liste, si on a comme paramètre reverse=True la liste sera trier à l'envers
    if not nombre == -1:
        collection = collection[:nombre]

    nb_pizzas = len(collection)
    if nb_pizzas == 0:
        print("ACUNE PIZZA.")
        return
    print(f"--------- LISTE DES PIZZAS ({nb_pizzas}) ---------")
    for pizza in collection:
        print(pizza)
    print("")
    print("Première pizza :", collection[0])
    print("Dernière pizza :", collection[-1])


# demander ajouter pizza à l'utilisateur
def ajouter_pizza_utilisateur(collection):
    p = input("Pizza à ajouter: ")
    if p.lower() in collection:
        print("Erreur, pizza existe déjà")
    else:
        collection.append(p)


# Pizza existe:
def pizza_existe(collection, pizza):
    if not pizza in collection: # lower() met la chaine en miniscule/ upper() en majusculue
        print("cette pizza n'existe pas.")
        return True
    else:
        print("Cette pizza existe déjà.")
        return False

pizzas_tuple = ("4 frommages", "végétarienne", "hawai", "calzone")
pizzas_liste = list(pizzas_tuple)

ajouter_pizza_utilisateur(pizzas_liste)
afficher(pizzas_liste, 2)

