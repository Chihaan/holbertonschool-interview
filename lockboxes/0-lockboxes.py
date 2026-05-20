#!/usr/bin/python3
"""Function to unlock boxes"""


def canUnlockAll(boxes):
    """Start of the function"""

    n = len(boxes)
    # Une liste de boites a explorer en partant de 0 ouverte
    a_explorer = [0]
    # Une liste des boites où je suis allé
    boites_ouvertes = {0}

    # Tant que a_explorer n'est pas vide
    while a_explorer:
        # Je pop la boite
        boite = a_explorer.pop()
        # Je vais a la boite de ma clef
        for clef in boxes[boite]:
            # Si cette boite n'est pas dans mes boites ouvertes
            if clef not in boites_ouvertes and clef < n:
                # Je l'ajoute a ma liste de boite a ouvrir
                a_explorer.append(clef)
                # J'ajoute la clef a mes boites ouvertes
                boites_ouvertes.add(clef)
    # Si la taille de la liste boites est égale a celle de mes boites ouvertes
    return n == len(boites_ouvertes)
    # True si j'ai ouvert toutes les boites
    # False, il manquait une clef
