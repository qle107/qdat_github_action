# quelques calculs de stats basiques pour le job QDat

from __future__ import annotations


def moyenne(valeurs: list[float]) -> float:
    if not valeurs:
        raise ValueError("liste vide")
    return sum(valeurs) / len(valeurs)


def mediane(valeurs: list[float]) -> float:
    if not valeurs:
        raise ValueError("liste vide")
    ordonnees = sorted(valeurs)
    milieu = len(ordonnees) // 2
    if len(ordonnees) % 2 == 1:
        return float(ordonnees[milieu])
    # nombre pair -> on fait la moyenne des deux du milieu
    return (ordonnees[milieu - 1] + ordonnees[milieu]) / 2


def etendue(valeurs: list[float]) -> float:
    if not valeurs:
        raise ValueError("liste vide")
    return max(valeurs) - min(valeurs)


def normaliser(valeurs: list[float]) -> list[float]:
    """Min-max entre 0 et 1. Si toutes les valeurs sont egales on renvoie des 0
    (sinon on divise par zero)."""
    if not valeurs:
        raise ValueError("liste vide")
    bas, haut = min(valeurs), max(valeurs)
    if bas == haut:
        return [0.0 for _ in valeurs]
    return [(v - bas) / (haut - bas) for v in valeurs]
