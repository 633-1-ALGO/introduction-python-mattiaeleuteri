# Problème : Réaliser une table de multiplication de taile 10x10 en utilisant la liste fournie.
# Résultat attendu : un affichage comme ceci :   1  2  3  4  5  6  7  8  9  10
#                                             1  1  2  3  4  5  6  7  8  9  10
#                                             2  2  4  6  8  10 12 14 16 18 20
#                                             . .  .  .  .  .  .  .  .  .  .
# Indication :   L'alignement rectiligne n'est pas une contrainte, tant que la table est visible ligne par ligne c'est ok.
#               Si vous êtes perfectionnistes faites vous plaisir.
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tableau = []


print(" \t1\t2\t3\t4\t5\t6\t7\t8\t9\t10")
for i in liste:
    print(i, end="\t")
    for j in liste:
        print(i*j, end="\t")
    print("")
