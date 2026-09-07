"""Job QDat : calcule des metriques et ecrit un rapport JSON."""

import json
import os
import platform
from datetime import datetime, timezone

from qdat_metrics import etendue, mediane, moyenne, normaliser

MESURES = [12.5, 7.0, 19.25, 3.5, 11.0]


def construire_rapport() -> dict:
    cle = os.environ.get("SECRET_API_KEY", "")
    return {
        "genere_le": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "machine": platform.node(),
        "python": platform.python_version(),
        "nb_mesures": len(MESURES),
        "moyenne": round(moyenne(MESURES), 3),
        "mediane": mediane(MESURES),
        "etendue": etendue(MESURES),
        "normalisees": [round(v, 3) for v in normaliser(MESURES)],
        "cle_api_presente": bool(cle),
        "cle_api_longueur": len(cle),
    }


def main() -> None:
    rapport = construire_rapport()
    texte = json.dumps(rapport, indent=2, ensure_ascii=False)
    print(texte)
    with open("rapport.json", "w", encoding="utf-8") as fichier:
        fichier.write(texte + "\n")


if __name__ == "__main__":
    main()
