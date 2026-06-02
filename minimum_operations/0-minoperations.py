#!/usr/bin/python3
"""Calcule le nombre minimum d'opérations (Copy All + Paste) pour
obtenir exactement n caractères à partir d'un seul caractère.
"""


def minOperations(n):
    """Retourne le nombre minimum d'opérations pour obtenir n caractères.

    Le résultat est la somme des facteurs premiers de n.
    Retourne 0 si n est impossible à atteindre (n <= 1).
    """
    diviseur = 2
    operations = 0

    if n == 0 or n == 1:
        return 0

    while n > 1:
        if n % diviseur == 0:
            n //= diviseur
            operations += diviseur
        else:
            diviseur += 1

    return operations
