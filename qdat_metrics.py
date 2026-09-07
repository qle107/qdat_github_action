"""Petites metriques statistiques utilisees par le job QDat."""

from __future__ import annotations


def moyenne(valeurs: list[float]) -> float:
    """Moyenne arithmetique d'une liste non vide."""
    if not valeurs:
        raise ValueError("liste vide")
    return sum(valeurs) / len(valeurs)


def mediane(valeurs: list[float]) -> float:
    """Mediane d'une liste non vide."""
    if not valeurs:
        raise ValueError("liste vide")
    ordonnees = sorted(valeurs)
    milieu = len(ordonnees) // 2
    if len(ordonnees) % 2 == 1:
        return float(ordonnees[milieu])
    return (ordonnees[milieu - 1] + ordonnees[milieu]) / 2


def etendue(valeurs: list[float]) -> float:
    """Difference entre le max et le min."""
    if not valeurs:
        raise ValueError("liste vide")
    return max(valeurs) - min(valeurs)


def normaliser(valeurs: list[float]) -> list[float]:
    """Ramene les valeurs dans [0, 1] (min-max). Liste constante -> zeros."""
    if not valeurs:
        raise ValueError("liste vide")
    bas, haut = min(valeurs), max(valeurs)
    if bas == haut:
        return [0.0 for _ in valeurs]
    return [(v - bas) / (haut - bas) for v in valeurs]
