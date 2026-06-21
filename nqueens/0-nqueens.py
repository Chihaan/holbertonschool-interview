#!/usr/bin/env python3
"""Solves the N queens problem and prints every solution."""

import sys


def est_sur(plateau, ligne, colonne):
    """Return True if a queen at (ligne, colonne) attacks no placed queen."""
    for r in range(len(plateau)):
        col_r = plateau[r]
        if col_r == colonne or abs(col_r - colonne) == abs(r - ligne):
            return False
    return True


def resoudre(N):
    """Print every N queens solution for a board of size N."""
    def explore(plateau):
        ligne = len(plateau)
        if ligne == N:
            print([[i, plateau[i]] for i in range(N)])
            return
        else:
            for colonne in range(N):
                if est_sur(plateau, ligne, colonne):
                    plateau.append(colonne)
                    explore(plateau)
                    plateau.pop()
    explore([])


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

resoudre(N)
