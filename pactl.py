#!/usr/bin/env python3

import os
import subprocess

# Fonction pour exécuter une commande système
def run_command(command):
    subprocess.run(command, shell=True)

# Fonction pour installer un paquet
def install_package(package_name):
    run_command("sudo pacman -S " + package_name)

# Fonction pour désinstaller un paquet
def uninstall_package(package_name):
    run_command("sudo pacman -Rs " + package_name)

# Fonction pour installer un paquet depuis AUR
def install_aur_package(package_name):
    run_command("git clone https://aur.archlinux.org/" + package_name + ".git")
    os.chdir(package_name)
    run_command("makepkg -si")
    os.chdir("..")
    run_command("rm -rf " + package_name)

# Fonction pour rechercher un paquet
def search_package(package_name):
    run_command("pacman -Ss " + package_name)

# Affichage du menu principal
print("Bienvenue dans Pactl, le gestionnaire de paquets en ligne de commande pour Arch Linux.")
print("Que voulez-vous faire ?")
print("1. Installer un paquet")
print("2. Désinstaller un paquet")
print("3. Installer un paquet depuis AUR")
print("4. Rechercher un paquet")
print("5. Quitter")

# Demande de choix à l'utilisateur
choice = input("Entrez votre choix : ")

# Traitement du choix de l'utilisateur
while choice != "5":
    if choice == "1":
        package_name = input("Entrez le nom du paquet à installer : ")
        install_package(package_name)
    elif choice == "2":
        package_name = input("Entrez le nom du paquet à désinstaller : ")
        uninstall_package(package_name)
    elif choice == "3":
        package_name = input("Entrez le nom du paquet à installer depuis AUR : ")
        install_aur_package(package_name)
    elif choice == "4":
        package_name = input("Entrez le nom du paquet à rechercher : ")
        search_package(package_name)
    else:
        print("Choix invalide.")

    # Affichage du menu principal
    print("Que voulez-vous faire ?")
    print("1. Installer un paquet")
    print("2. Désinstaller un paquet")
    print("3. Installer un paquet depuis AUR")
    print("4. Rechercher un paquet")
    print("5. Quitter")

    # Demande de choix à l'utilisateur
    choice = input("Entrez votre choix : ")

print("Merci d'avoir utilisé Pactl.")
