import os
import sys
import tarfile
import datetime
from subprocess import call

class Backup:
    fichier = []
    tar = None
    fichiertar = None

    def __init__(self, nom):
        self.nom = nom

    def add(self, nom_fichier):
        """Ajouter des fichiers et dossiers"""
        if os.path.isfile(nom_fichier) or os.path.isdir(nom_fichier):
            self.fichier.append(nom_fichier)
        else:
            sys.exit("Fichier ou dossier non existant: %s" % nom_fichier)

    def create_tar(self):
        """Créer un dossier tar avec les fichiers ajouté grace à self.add()"""
        self.fichiertar = self.name.replace(' ', '') + "-" + datetime.date.today().strftime("%m-%d-%Y") + ".tar.gz"
        self.tar = fichiertar.open(self.tarfile, 'w:gz')

        for nom_fichier in self.fichier:
            self.tar.add(nom_fichier)

        self.tar.close()

    # Create files
    backup.create_tar()
  
