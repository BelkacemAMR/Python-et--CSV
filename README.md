# Python et CSV :
 
## 1) La fionction "generate_csv": 

Le programme generate_csv prend un ensemble de données sous forme de liste de dictionnaires et génère un fichier CSV avec ces données triées dans des colonnes. 
Il utilise le module CSV pour écrire le fichier CSV, extrait les noms de colonnes du premier dictionnaire fourni en entrée, et pour chaque dictionnaire, il crée une nouvelle ligne dans le fichier CSV. 

Le programme transforme la valeur de chaque colonne en fonction de son type et de la clé, pour formater la date dans le format 'mm/dd/yyyy' et concaténer les listes et les tuples. Le fichier CSV résultant est créé dans le répertoire actuel et est nommé 'results.csv'.

## 2) La fonction "parse_csv":

La fonction "parse_csv" un fichier CSV contenant des informations sur les étudiants, crée une liste de dictionnaires où chaque dictionnaire représente un étudiant et ses informations, et retourne cette liste. Le programme utilise les modules csv et datetime pour analyser le contenu du fichier CSV, convertir la date de naissance des étudiants en un objet de date Python, et stocker les notes des étudiants sous forme de liste d'entiers.
