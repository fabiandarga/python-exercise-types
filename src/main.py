from typing import List, Dict, Union, Optional


def berechne_durchschnitt(noten):
    """Berechnet den Durchschnitt einer Liste von Noten"""
    return sum(noten) / len(noten)


def finde_schueler(schueler_dict, name):
    """Findet einen Schüler in einem Dictionary und gibt seine Informationen zurück"""
    return schueler_dict.get(name, "Nicht gefunden")


def formatiere_note(note):
    """Formatiert eine Note als String mit einem '+' wenn sie besser als 2.0 ist"""
    if note < 2.0:
        return str(note) + "+"
    return str(note)


def erstelle_bericht(name, alter, noten):
    """Erstellt einen Bericht für einen Schüler"""
    return {
        "name": name,
        "alter": alter,
        "noten": noten,
        "durchschnitt": berechne_durchschnitt(noten)
    }


def aktualisiere_alter(schueler, neues_alter):
    """Aktualisiert das Alter eines Schülers"""
    schueler["alter"] = neues_alter
    return schueler


def main():
    # Beispiel-Daten
    schueler_daten = {
        "Max": {"alter": 16, "noten": [1, 2, 2, 3]},
        "Lisa": {"alter": "17", "noten": [1, 1, 2, 1]},  # Absichtlicher Fehler: Alter als String
        "Tom": {"alter": 16, "noten": [2, 3, "2", 4]}    # Absichtlicher Fehler: Note als String
    }

    try:
        # Berechnungen und Ausgaben
        print("Schülerberichte:")
        for name, daten in schueler_daten.items():
            bericht = erstelle_bericht(name, daten["alter"], daten["noten"])
            print(f"\nBericht für {name}:")
            print(f"Alter: {bericht['alter']}")
            print(f"Notendurchschnitt: {formatiere_note(bericht['durchschnitt'])}")

        # Demonstriere einige Typfehler
        lisa_info = finde_schueler(schueler_daten, "Lisa")
        lisa_info["noten"].append(2.5)  # Könnte fehlschlagen

        tom_durchschnitt = berechne_durchschnitt(schueler_daten["Tom"]["noten"])  # Wird fehlschlagen

        # Alter aktualisieren
        max_aktualisiert = aktualisiere_alter(schueler_daten["Max"], "17")  # Absichtlicher Fehler: Alter als String

    except (TypeError, AttributeError) as e:
        print(f"\nFehler aufgetreten: {e}")
        print("Dieser Fehler könnte durch Type-Hints verhindert werden!")


if __name__ == "__main__":
    main()
