# Software
Software Project 

# Projekt-Software

## Projektübersicht

Dieses Repository enthält die Projekte unserer Gruppe für das Software Engineering Abschlussprojekt.  
Die Projekte werden in zwei Teilprojekte aufgeteilt:

- **Conversion-Tool** (Team 1) – Ein Umrechnungsrechner für Temperaturen und Währungen.
- **Pomodoro-Timer** (Team 2) – Ein Timer für verschiedene Lerntechniken.


Dieses Repository zeigt den Einsatz von **Git-Versionierung**, **Branches**, **Code-Reviews** und dokumentiert die Nutzung von **AI-Tools (z. B. ChatGPT)** während des Entwicklungsprozesses.

---

## Team 1: Conversion-Tool

### Projektbeschreibung
Das Conversion-Tool erlaubt es dem Nutzer, entweder:

1. Temperaturen zwischen Celsius und Fahrenheit umzurechnen,  
2. Beträge zwischen verschiedenen Währungen zu konvertieren.

Die Währungsumrechnung nutzt aktuelle Wechselkurse, die über eine API abgerufen werden.  

### Hauptfunktionen

- Menü-Auswahl für Art der Umrechnung (Temperatur/Währung)  
- Benutzer-Eingabe von Werten  
- Umrechnung und Ausgabe des Ergebnisses  
- API-Anbindung für aktuelle Wechselkurse

### Technologien & Tools

- Python   
- Git & GitHub für Versionierung und Zusammenarbeit  
- API für Währungsdaten (z. B. fixer Endpunkt `exchangeratesapi.io`)

## Team 2: Pomodoro-Timer

### Projektbeschreibung
Der Pomodoro-Timer erlaubt es dem User:

1. Die Pomodoro-Lerntechnik mit individuellen Kombinationsmöglichkeiten zu nutzen und
2. Eine kurze Statistik über die Lern-Sessions zu erhalten.

Das Programm bietet eine GUI inkl. Tonsignal an.

### Hauptfunktionen

- Timer inkl. Kombinationsmöglichkeiten
- Ausgabe einer Statistik zu den Themen
- GUI  
- Signalton für den Wechsel zwischen Lern- und Pausenphasen

### Technologien & Tools

- Python   
- Git & GitHub für Versionierung und Zusammenarbeit  

# Review der Projekte

## Verarbeitung Review - Team pomodoro

Wir haben im Zuge der Review die folgenden Punkte rausgelesen:

Viele Funktionen / kompakter coden?
- Entscheidung: Wollen wir nicht ändern
- Begründung: Bewusste Modularität, bessere Les- und Wartbarkeit, keine künstliche bzw. komplizierten Zusammenfassungen

Kommentare mittels Docstrings reduzieren
- Entscheidung: Wollen wir nicht ändern
- Begründung: Fachlich richtig, aber aktuell vom Aufwand her nicht priorisiert, da zu wenige Einsatzmöglichkeiten vorhanden sind. Es sind für alle Bestandteile Kommentare vorhanden.

Vorzeitige Sitzungsabbrüche in Statistik aufnehmen
- Entscheidung: Haben wir direkt geändert
- Begründung: Inhaltlich sinnvoll, damit der gesamte Lernaufwand dokumentiert werden kann und nichts auf Grund der Logik verloren geht.

