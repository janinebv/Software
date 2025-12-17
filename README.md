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



Comments / Feedback: pomodoro-Code:

Der vorliegende Code ist lauffähig und produziert – soweit erkennbar – keine Probleme. Es wurden allerdings enorm viele Funktionen definiert. Das macht das Gesamtprojekt zwar sehr modular, zu hinterfragen wäre allerdings, ob man hier etwas kompakter “bauen” (coden) könnte? 

Die Lesbarkeit für Menschen scheint gut gegeben – es wurden alle Funktionsmodule gut auskommentiert. Insofern das Programm eine Umsetzung eines fertigen Konzepts (“pomodoro-Lenrmethode”) darstellt, ist eine Erweiterung / Ergänzung wsl nicht angedacht. 

Durch die modulare Bauweise ließen sich aber relativ einfach Komponenten hinzufügen. Es müssten dazu aber dann auch im Eingabe-Interface Änderungen vorgenommen werden. Insgesamt ist die Umsetzung komplex – aber gut!