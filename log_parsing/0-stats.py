#!/usr/bin/python3
"""Lit des lignes de log sur stdin et affiche des métriques cumulées.

Format attendu par ligne :
    <IP> - [<date>] "GET /projects/260 HTTP/1.1" <status> <size>
Les lignes hors format sont ignorées. Les statistiques (taille totale
et nombre de lignes par code HTTP) sont affichées tous les 10 lignes
et à l'interruption clavier (CTRL+C).
"""

import sys


def parse(line):
    """Extrait (status, size) d'une ligne, ou None si elle est invalide.

    On ne valide que les deux derniers champs (les seuls utilisés) :
    le code HTTP et la taille doivent être des entiers.
    """
    parts = line.split()
    try:
        status = int(parts[-2])
        size = int(parts[-1])
    except (ValueError, IndexError):
        return None
    return status, size


def display_logs(counts, total_size):
    """Affiche la taille totale puis le nb de lignes par code (croissant).

    Les codes jamais rencontrés (compteur à 0) sont ignorés.
    """
    print(f"File size: {total_size}")
    for code in sorted(counts):
        if counts[code] == 0:
            continue
        print(f"{code}: {counts[code]}")


def main():
    """Lit stdin, accumule les métriques, affiche tous les 10 + sur CTRL+C."""
    count = 0
    total_size = 0
    counts = {200: 0, 301: 0, 400: 0, 401: 0,
              403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in sys.stdin:
            count += 1
            res = parse(line.strip())
            if res is None:
                continue
            status, size = res
            if status in counts:
                counts[status] += 1        # dict pré-rempli -> pas de KeyError
            total_size += size
            if count % 10 == 0:        # bilan tous les 10 lignes
                display_logs(counts, total_size)
    except KeyboardInterrupt:          # CTRL+C -> dernier bilan
        display_logs(counts, total_size)


if __name__ == "__main__":
    main()
