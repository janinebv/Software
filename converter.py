import requests  # Notwendige Bibliothek für API-Aufrufe (HTTP-Requests)

# Unterstützte Währungen: Hier werden nur die wichtigsten Codes festgelegt.
SUPPORTED_CURRENCIES = ["EUR", "USD", "JPY", "GBP", "CAD", "CHF"]

# Haupt-Menü-Funktion

def display_menu():
    """Zeigt das Hauptmenü an und nimmt die Auswahl des Benutzers entgegen.""" # HIER ist der Docstring korrekt eingerückt
    print("\nWelche Umrechnung möchten Sie durchführen?  1 = Temperatur | 2 = Währung | 0 = Beenden")
    auswahl = input("Bitte wählen Sie eine Option: ")
    return auswahl

# Temperatur-Konvertierung
    """ Führt die Temperaturumrechnung zwischen Celsius, Fahrenheit und Kelvin durch.
    Die Umrechnungsformeln sind direkt im Code hinterlegt. """

# Hilfsfunktionen für Temperatur-Umrechnung 

def c_to_f(celsius):
    """Konvertiert Celsius nach Fahrenheit."""
    return celsius * 9/5 + 32

def f_to_c(fahrenheit):
    """Konvertiert Fahrenheit nach Celsius."""
    return (fahrenheit - 32) * 5/9

def c_to_k(celsius):
    """Konvertiert Celsius nach Kelvin."""
    return celsius + 273.15

def k_to_c(kelvin):
    """Konvertiert Kelvin nach Celsius."""
    return kelvin - 273.15

def f_to_k(fahrenheit):
    """Konvertiert Fahrenheit nach Kelvin (über Celsius)."""
    # Umrechnung über den Zwischenschritt Celsius, nutzt die definierten Funktionen
    celsius = f_to_c(fahrenheit)
    return c_to_k(celsius)

def k_to_f(kelvin):
    """Konvertiert Kelvin nach Fahrenheit (über Celsius)."""
    # Umrechnung über den Zwischenschritt Celsius, nutzt die definierten Funktionen
    celsius = k_to_c(kelvin)
    return c_to_f(celsius)


# Temperatur-Konvertierung (Hauptfunktion)

def convert_temperature():
    """Führt die Temperaturumrechnung zwischen Celsius, Fahrenheit und Kelvin durch."""
    
    print("\nTemperaturkonvertierung:")
    print("Bitte Skala wählen: C = Celsius, F = Fahrenheit, K = Kelvin")
    
    valid_scales = ["C", "F", "K"]

    # 1. Eingabe der Skalen
    von = input("Von welcher Skala möchten Sie umrechnen? (C/F/K): ").upper()
    if von not in valid_scales:
        print(f"Ungültige Skala: '{von}'! Bitte starten Sie neu.")
        return

    zu = input("Zu welcher Skala möchten Sie umrechnen? (C/F/K): ").upper()
    if zu not in valid_scales:
        print(f"Ungültige Skala: '{zu}'! Bitte starten Sie neu.")
        return
    
    # 2. Eingabe des Wertes erfolgt erst nach erfolgreicher Prüfung
    try:
        wert = float(input("Geben Sie den Wert der Ausgangstemperatur ein: "))
    except ValueError:
        print("Ungültige Eingabe! Bitte eine Zahl eingeben.")
        return
    
    ergebnis = None

    # 3. Logik: Aufruf der dedizierten Umrechnungsfunktionen
    
    if von == zu:
        ergebnis = wert
    
    # C Konvertierungen
    elif von == "C" and zu == "F":
        ergebnis = c_to_f(wert)
    elif von == "F" and zu == "C":
        ergebnis = f_to_c(wert)
    elif von == "C" and zu == "K":
        ergebnis = c_to_k(wert)
    elif von == "K" and zu == "C":
        ergebnis = k_to_c(wert)

    # F <-> K Konvertierungen (nutzen die dedizierten Hilfsfunktionen)
    elif von == "F" and zu == "K":
        ergebnis = f_to_k(wert)
    elif von == "K" and zu == "F":
        ergebnis = k_to_f(wert)
    
    else:
        print("Ungültige Auswahl der Skalen!")
        return
    
    # Ausgabe des Ergebnisses, gerundet auf zwei Dezimalstellen
    print(f"{wert} {von} = {ergebnis:.2f} {zu}")


# Währungs-Konvertierung

# Währungs-API Funktion
def get_exchange_rates(base="EUR"):
    """ Ruft die aktuellen Wechselkurse von der Frankfurter API ab.
    Die Kurse basieren auf der angegebenen Basiswährung ('base'). """
    
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
    """ Führt die Währungsumrechnung durch. Fragt nach Startwährung, Zielwährung und Betrag, 
    und nutzt dann die abgerufenen Wechselkurse. """

def convert_currency():
    print("\nWährungskonvertierung:")
    
    # 1. Benutzerführung und Validierung der Währungscodes
    currency_list_str = ", ".join(SUPPORTED_CURRENCIES)
    print(f"Unterstützte Währungen: {currency_list_str}")
    
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
    """ Die Hauptschleife des Programms. Steuert das Menü und den Programmfluss. """

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

# Ende des Programms
