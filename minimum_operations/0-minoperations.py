#!/usr/bin/python3


def minOperations(n):
    """Retourne le nombre minimum d'opérations pour obtenir n caractères."""
    diviseur = 2
    operations = 0

    if n == 0 or n == 1 :
        return 0

    while n > 1:
        if n % diviseur == 0:
            n //= diviseur
            operations += diviseur
        else:
            diviseur += 1
    return operations
