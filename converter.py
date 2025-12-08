import requests  #Notwendige Bibliothek für API-Aufrufe (HTTP-Requests)

# Unterstützte Währungen: Hier werden nur die wichtigsten Codes festgelegt.
SUPPORTED_CURRENCIES = ["EUR", "USD", "JPY", "GBP", "CAD", "CHF"]

# Haupt-Menü-Funktion
def display_menu():
    """Zeigt das Hauptmenü an und nimmt die Auswahl des Benutzers entgegen."""
    print("\nWas möchtest du umrechnen?")
    print("1 = Temperatur")
    print("2 = Währung")
    print("0 = Beenden")
    auswahl = input("Bitte wähle eine Option: ")
    return auswahl

# Temperatur-Konvertierung
    """
    Führt die Temperaturumrechnung zwischen Celsius, Fahrenheit und Kelvin durch.
    Die Umrechnungsformeln sind direkt im Code hinterlegt.
    """
def convert_temperature():
    print("\nTemperaturkonvertierung:")
    print("Du kannst aus folgenden Skalen wählen: C = Celsius, F = Fahrenheit, K = Kelvin")
    
    # 1. Eingabe der Skalen und Umwandlung in Großbuchstaben zur Standardisierung
    von = input("Von welcher Skala möchtest du umrechnen? (C/F/K): ").upper()
    zu = input("Zu welcher Skala möchtest du umrechnen? (C/F/K): ").upper()
    
    # 2. Eingabe des Wertes und Fehlerbehandlung
    try:
        wert = float(input("Gib den Wert der Ausgangstemperatur ein: "))
    except ValueError:
        # Fängt Fehler ab, wenn der Benutzer keine Zahl eingibt
        print("Ungültige Eingabe! Bitte eine Zahl eingeben.")
        return
    
    ergebnis = None

    # 3. Logik für die Umrechnungsformeln
    
    # C ↔ F: Celsius und Fahrenheit
    if von == "C" and zu == "F":
        ergebnis = wert * 9/5 + 32 # Formel: C * 9/5 + 32 = F
    elif von == "F" and zu == "C":
        ergebnis = (wert - 32) * 5/9 # Formel: (F - 32) * 5/9 = C

    # C ↔ K: Celsius und Kelvin
    elif von == "C" and zu == "K":
        ergebnis = wert + 273.15 # Formel: C + 273.15 = K (Absoluter Nullpunkt)
    elif von == "K" and zu == "C":
        ergebnis = wert - 273.15

    # F ↔ K: Fahrenheit und Kelvin
    elif von == "F" and zu == "K":
        # Hier wird zuerst in Celsius umgerechnet, dann in Kelvin
        ergebnis = (wert - 32) * 5/9 + 273.15
    elif von == "K" and zu == "F":
        # Hier wird zuerst in Celsius umgerechnet, dann in Fahrenheit
        ergebnis = (wert - 273.15) * 9/5 + 32

    # Sonderfall: Gleiche Einheit
    elif von == zu:
        ergebnis = wert
    else:
        print("Ungültige Auswahl der Skalen!")
        return
    
    # Ausgabe des Ergebnisses, gerundet auf zwei Dezimalstellen
    print(f"{wert} {von} = {ergebnis:.2f} {zu}")


# Währungs-Konvertierung

# Währungs-API Funktion
def get_exchange_rates(base="EUR"):
    """
    Ruft die aktuellen Wechselkurse von der Frankfurter API ab.
    Die Kurse basieren auf der angegebenen Basiswährung ('base').
    """
    # Externe API-Adresse (Frankfurter API ist kostenlos und zuverlässig)
    url = f"https://api.frankfurter.app/latest?from={base}"
    
    try:
        # API-Abruf mit Timeout zur Vermeidung endloser Wartezeiten
        response = requests.get(url, timeout=10) 
        
        # Prüfung des HTTP-Statuscodes (200 = OK, alles andere ist ein Fehler)
        if response.status_code != 200:
            print(f"Fehler beim API-Aufruf. HTTP-Status: {response.status_code}")
            return {}

        data = response.json()
        # Liest die Kurse unter dem Schlüssel "rates"
        rates = data.get("rates", {})
        
        # Die Frankfurter API liefert die Basiswährung nicht in den "rates" zurück
        # aber sie muss 1.0 sein. Wir fügen sie hinzu, damit der Code funktioniert:
        rates[base] = 1.0 
        
        return rates
        
    except requests.exceptions.RequestException as e:
        # Fängt Netzwerkfehler (DNS, Timeout, Verbindung) ab
        print(f"Netzwerkfehler beim Abrufen der Wechselkurse: {e}")
        return {}
    except Exception as e:
        # Fängt andere Fehler ab (z.B. falsches JSON-Format)
        print(f"Ein unerwarteter Fehler beim Parsen ist aufgetreten: {e}")
        return {}

# Währungs-Konvertierer
    """
    Führt die Währungsumrechnung durch. Fragt nach Startwährung, Zielwährung und Betrag, 
    und nutzt dann die abgerufenen Wechselkurse.
    """
def convert_currency():
    print("\nWährungskonvertierung:")
    
    # 1. Benutzerführung und Validierung der Währungscodes
    currency_list_str = ", ".join(SUPPORTED_CURRENCIES)
    print(f"Du kannst nur folgende Währungen verwenden: {currency_list_str}")
    
    # Schleife zur erzwungenen Eingabe eines gültigen Basis-Codes
    while True:
        base = input("Ausgangswährung (3-stelliger Code, z.B. EUR): ").upper()
        if base in SUPPORTED_CURRENCIES:
            break
        print(f"Ungültige Ausgangswährung '{base}'. Bitte wähle aus: {currency_list_str}")

    # Schleife zur erzwungenen Eingabe eines gültigen Ziel-Codes
    while True:
        ziel = input("Zielwährung (3-stelliger Code, z.B. USD): ").upper()
        if ziel in SUPPORTED_CURRENCIES:
            break
        print(f"Ungültige Zielwährung '{ziel}'. Bitte wähle aus: {currency_list_str}")

    # 2. Eingabe des Betrags mit Fehlerbehandlung
    try:
        betrag = float(input("Betrag eingeben: "))
    except ValueError:
        print("Ungültige Eingabe! Bitte eine Zahl eingeben.")
        return
    
    # 3. Abruf der Wechselkurse
    rates = get_exchange_rates(base)
    if not rates:
        print("Wechselkurse konnten für diese Basiswährung nicht geladen werden.")
        return
    
    # 4. Berechnung und Ausgabe
    
    # Sicherstellen, dass der Zielkurs in den geladenen Daten vorhanden ist
    if ziel not in rates:
        # Dies sollte nur passieren, wenn die API plötzlich einen unterstützten Kurs nicht liefert
        print(f"Fehler: Zielwährung {ziel} nicht in den geladenen Kursen enthalten.")
        return
    
    ergebnis = betrag * rates[ziel]
    print(f"\n{betrag} {base} = {ergebnis:.2f} {ziel}")

# Hauptprogramm

    """
    Die Hauptschleife des Programms. Steuert das Menü und den Programmfluss.
    """
def main():
    while True:
        auswahl = display_menu()
        
        # Kontrollstruktur zur Steuerung des Programms (Welcher Konverter wird gewählt)
        if auswahl == "1":
            convert_temperature()
        elif auswahl == "2":
            convert_currency()
        elif auswahl == "0":
            print("Programm beendet.")
            break
        else:
            # Fängt ungültige Eingaben im Hauptmenü ab
            print("Ungültige Auswahl!")

if __name__ == "__main__":
    main()

