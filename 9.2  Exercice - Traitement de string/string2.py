# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

texte_nouveau = texte

texte_nouveau.replace('est', 'représente')

compteur = 0

texte_nouveau_split = texte_nouveau.split(' ')

for m in texte_nouveau_split:
    if m == 'exemple' or m == "d'exemple" or m == "d'exemple.":
        compteur += 1

texte_nouveau_reversed = ''

for m in reversed(texte_nouveau_split):
    texte_nouveau_reversed += m + ' '

print("Phrase originale :", texte)

print("Nouvelle phrase :", texte_nouveau)
print("Nouvelle phrase renversée :", texte_nouveau_reversed)
print("Il y a", compteur, "occurences du mot 'exemple' dans la phrase ")
