#!/usr/bin/python3


def minOperations(n):
    """Retourne le nombre minimum d'opérations pour obtenir n caractères."""
    diviseur = 2
    operations = 0

# Si c'est 0 ou 1 
    if n == 0 or n == 1 :
        return 0

# Si c'est un prime number
    if n % 1 == 0 and n % n == 0:
        return n
    
# Pour le reste pair & impair
    while n > 1:
        if n % 1 == 0 and n % n == 0:
            return operations + n
        if n % diviseur == 0:
            n /= diviseur
            operations += diviseur
        else:
            diviseur += 1
    return operations
