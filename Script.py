import os
import time
import datetime
import tarfile
from subprocess import call

DB_HOST = 'localhost'
DB_USER = 'appli_web'
DB_USER_PASSWORD = 'appli_web'
NOM_BDD = '/sauvegardes/BDDs.txt' # Fichier TXT où sont répertoriés les noms de chaque BDD
#NOM_BDD = 'appli_web'
CHEMIN_SAUVEGARDE = '/sauvegardes/sauvegardes_bdd/'

# Getting current datetime to create seprate backup folder like "12012013-071334".
DATETIME = time.strftime('%d%m%Y-%H%M%S')

TODAYBACKUPPATH = CHEMIN_SAUVEGARDE + DATETIME

def Sauvegarde():
  # Création du dossier de sauvegarde si il n'existe pas déjà.
  print("Création du dossier de sauvegarde")
  if not os.path.exists(CHEMIN_SAUVEGARDE):
      os.makedirs(CHEMIN_SAUVEGARDE)

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

  # Sauvegarde en .tar.gz
  def make_tarfile(output_filename, source_dir):
      with tarfile.open(output_filename, "w:gz") as tar:
          tar.add(source_dir, arcname=os.path.basename(source_dir))

  if multi:
     in_file = open(NOM_BDD,"r")
     flength = len(in_file.readlines())
     in_file.close()
     p = 1
     dbfile = open(NOM_BDD,"r")

     while p <= flength:
         db = dbfile.readline()   # reading database name from file
         db = db[:-1]             # deletes extra line
         fichier_sql = CHEMIN_SAUVEGARDE + "/" + db + ".sql"
         dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + fichier_sql 
         os.system(dumpcmd)
         make_tarfile(TODAYBACKUPPATH + ".tar.gz", fichier_sql)
         p = p + 1
     dbfile.close()
  else:
     db = NOM_BDD
     fichier_sql = CHEMIN_SAUVEGARDE + "/" + db + ".sql"
     dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + fichier_sql
     os.system(dumpcmd)
     make_tarfile(TODAYBACKUPPATH + ".tar.gz", fichier_sql)

  os.system("rm -rf " + fichier_sql)
  print("Script de sauvegarde exécuté.")
  print("Votre sauvegarde a été créé dans le dossier " + CHEMIN_SAUVEGARDE)

def Restaurer():
  print("Quelle sauvegarde souhaitez-vous restaurer ? ")
  print(os.system("ls -r " + CHEMIN_SAUVEGARDE))

choix = int(input("Que voulez-vous faire ?\n [1] pour Sauvegarder le serveur MySQL dans une archive compressée\n [2] pour Restaurer le serveur MySQL avec une sauvegarde spécifique\n [3] pour Supprimer les sauvegardes de plus de 7 jours : "))
if choix == 1:
  Sauvegarde()
if choix == 2:
  Restaurer()
if choix == 3:
  print("Pas fait")
