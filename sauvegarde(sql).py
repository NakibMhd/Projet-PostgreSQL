import os
import time
import datetime

DB_HOST = 'localhost'
DB_USER = 'appli_web'
DB_USER_PASSWORD = 'appli_web'
NOM_BDD = '/sauvegardes/BDDs.txt' # Fichier TXT où sont répertoriés les noms de chaque BDD
#NOM_BDD = 'appli_web'
CHEMIN_SAUVEGARDE = '/sauvegardes/sauvegardes_bdd/'

# Getting current datetime to create seprate backup folder like "12012013-071334".
DATETIME = time.strftime('%d%m%Y-%H%M%S')

TODAYBACKUPPATH = CHEMIN_SAUVEGARDE + DATETIME

# Création du dossier de sauvegarde si il n'existe pas déjà.
print("Création du dossier de sauvegarde")
if not os.path.exists(TODAYBACKUPPATH):
    os.makedirs(TODAYBACKUPPATH)

# Code for checking if you want to take single database backup or assigned multiple backups in NOM_BDD.
print("Vérification du fichier TXT.")
if os.path.exists(NOM_BDD):
    file1 = open(NOM_BDD)
    multi = 1
    print("Fichier TXT trouvé...")
    print("Sauvegarde de toutes les BDD listées dans le fichier " + NOM_BDD)
else:
    print("Fichier TXT non trouvé...")
    print("Sauvegarde de la BDD " + NOM_BDD)
    multi = 0

# Starting actual database backup process.
if multi:
   in_file = open(NOM_BDD,"r")
   flength = len(in_file.readlines())
   in_file.close()
   p = 1
   dbfile = open(NOM_BDD,"r")

   while p <= flength:
       db = dbfile.readline()   # reading database name from file
       db = db[:-1]         # deletes extra line
       dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + TODAYBACKUPPATH + "/" + db + ".sql"
       os.system(dumpcmd)
       p = p + 1
   dbfile.close()
else:
   db = NOM_BDD
   dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + TODAYBACKUPPATH + "/" + db + ".sql"
   os.system(dumpcmd)

print("Script de sauvegard exécuté.")
print("Votre sauvegarde a été créé dans le dossier '" + TODAYBACKUPPATH)