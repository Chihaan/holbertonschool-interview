#!/usr/bin/python3
"""Lit des lignes de log sur stdin et affiche des métriques cumulées."""

import sys


def parse(line):
    """Retourne (status, size) pour une ligne, ou None si inexploitable.

    La taille (dernier champ) doit être un entier, sinon la ligne est
    ignorée. Le statut (avant-dernier champ) vaut None s'il n'est pas un
    entier : la taille est alors comptée mais aucun code ne l'est.
    """
    parts = line.split()
    try:
        size = int(parts[-1])
    except (ValueError, IndexError):
        return None
    try:
        status = int(parts[-2])
    except (ValueError, IndexError):
        status = None
    return status, size


def display_logs(counts, total_size):
    """Affiche la taille totale puis le nb de lignes par code (croissant)."""
    print(f"File size: {total_size}")
    for code in sorted(counts):
        if counts[code] == 0:
            continue
        print(f"{code}: {counts[code]}")


def main():
    """Lit stdin et affiche les métriques (tous les 10, EOF, CTRL+C)."""
    count = 0
    total_size = 0
    counts = {200: 0, 301: 0, 400: 0, 401: 0,
              403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in sys.stdin:
            count += 1
            res = parse(line.strip())
            if res is not None:
                status, size = res
                total_size += size
                if status in counts:
                    counts[status] += 1
            if count % 10 == 0:
                display_logs(counts, total_size)
    except KeyboardInterrupt:
        display_logs(counts, total_size)
        raise
    else:
        display_logs(counts, total_size)


if __name__ == "__main__":
    main()
