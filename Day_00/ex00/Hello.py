# Given data structures
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Update the data structures as per the instructions
ft_list[1] = "World!"

ft_tuple = ("Hello", "France!")

ft_set.remove("tutu!")
ft_set.add("Mulhouse!")

ft_dict["titi!"] = "42 Mulhouse!"

# Print the updated data structures
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

# En Python, les listes, tuples, sets et dictionnaires sont des types de données intégrées qui permettent de stocker des collections de données. Voici une brève explication de chacun :

# Liste (list)
# Définition: Une liste est une collection ordonnée et modifiable. Elle permet des éléments dupliqués.
# Création: Utilisation de crochets [].
# Usage: Vous pouvez utiliser une liste quand vous avez une collection d'éléments que vous pourriez vouloir modifier, trier ou manipuler de quelque manière que ce soit.

# Tuple (tuple)
# Définition: Un tuple est une collection ordonnée et non modifiable (immuable). Il permet aussi des éléments dupliqués.
# Création: Utilisation de parenthèses ().
# Usage: Les tuples sont utilisés quand vous voulez que vos données soient constantes et qu'elles ne changent jamais.

# Set (set)
# Définition: Un set est une collection non ordonnée et non indexée. Il est modifiable, mais ne peut pas avoir de doublons - chaque élément est unique.
# Création: Utilisation d'accolades {} avec des éléments séparés par des virgules, ou la fonction set().
# Usage: Les sets sont utiles pour la suppression de doublons, les tests d'appartenance et les opérations mathématiques comme les unions, intersections et différences.

# Dictionnaire (dict)
# Définition: Un dictionnaire est une collection ordonnée* et modifiable de paires clé-valeur. Aucune clé dupliquée n'est autorisée, bien que les valeurs puissent être dupliquées.
# Création: Utilisation d'accolades {} avec des éléments sous la forme clé: valeur.
# Usage: Les dictionnaires sont optimaux lorsque vous voulez associer une paire de valeurs clé-valeur, permettant de récupérer rapidement une valeur sans parcourir toute la collection.



# Modification de structures de données

# Pour modifier des structures de données telles que les listes, tuples, sets et dictionnaires en Python, voici ce que vous devez savoir :

# Liste
# Les listes sont modifiables, ce qui signifie que vous pouvez changer leurs éléments après leur création.

# Ajouter des éléments : Utilisez append() pour ajouter un élément à la fin, insert() pour ajouter un élément à une position spécifique.
# Modifier des éléments : Accédez à l'élément via son index et assignez-lui une nouvelle valeur.
# Supprimer des éléments : Utilisez remove() pour enlever un élément par sa valeur, pop() pour enlever un élément par son index, et del pour supprimer des éléments par index ou pour supprimer la liste entière.
# Tuple
# Les tuples sont immuables, ce qui signifie que vous ne pouvez pas modifier leurs éléments après leur création. Cependant, vous pouvez concaténer des tuples pour en créer de nouveaux, ou convertir un tuple en liste, le modifier, puis le reconvertir en tuple.

# Set
# Les sets sont modifiables et n'ont pas d'index.

# Ajouter des éléments : Utilisez add() pour ajouter un élément et update() pour ajouter plusieurs éléments.
# Supprimer des éléments : Utilisez remove() ou discard() pour supprimer un élément spécifique, et pop() pour supprimer un élément arbitraire.
# Dictionnaire
# Les dictionnaires sont modifiables et chaque élément est une paire clé-valeur.

# Ajouter et modifier des éléments : Assignez une valeur à une clé avec d[key] = value. Si la clé n'existe pas, elle sera ajoutée; si elle existe, sa valeur sera mise à jour.
# Supprimer des éléments : Utilisez pop(key) pour supprimer une paire clé-valeur par sa clé, del d[key] pour une suppression similaire, ou clear() pour vider le dictionnaire de tous ses éléments.
# Pour chacune de ces structures, vous devez tenir compte de leurs caractéristiques uniques lors de la modification pour éviter les erreurs. Par exemple, puisque les tuples sont immuables, vous ne pouvez pas changer un élément d'un tuple sans créer un nouveau tuple.