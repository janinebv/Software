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

## Verarbeitung Review - Team converter 

Wir haben das Feedback des Review-Teams (Vanessa & Samara) analysiert und folgende Entscheidungen für die finale Version und die zukünftige Entwicklung getroffen:

1. Sofort adaptierte Punkte (vor dem Merge)
- Docstring-Positionierung: Wir haben die fehlerhaft platzierten Docstrings korrigiert. Diese wurden nun direkt unter die Funktionsdefinitionen verschoben, um dem Python-Standard (PEP 257) zu entsprechen und die Lesbarkeit zu optimieren.
  
- Fehlerbehandlung bei Menüeingaben: Die Logik wurde so angepasst, dass bei einer ungültigen Menüauswahl (z. B. "G" statt "1") sofort eine Fehlermeldung erscheint und die Abfrage wiederholt wird, bevor nach weiteren Werten gefragt wird. Diese Adaptierung war notwendig, da zuvor der Fehler erst im Folgeschritt (bei der Werteeingabe oder Berechnung) auftauchte. Durch die Änderung sind wir nun näher am Punkt des Problems, verhindern unnötige Benutzereingaben und erhöhen die Effizienz des Programms
  
2. Punkte für die zukünftige Einarbeitung (Backlog)
   
Diese Punkte sind sinnvoll, werden aber aufgrund des aktuellen Projektumfangs erst in einer späteren Version umgesetzt:
- Caching von Wechselkursen: Vanessa schlug vor, API-Kurse zwischenzuspeichern. Wir planen, ein lokales Dictionary als Cache zu implementieren, um die Effizienz bei mehrfachen Umrechnungen zu steigern und API-Limits zu schonen.
  
- Automatisierte Tests: Da aktuell nur manuelle Tests durchgeführt wurden, planen wir für die Zukunft die Einbindung von unittest oder pytest, um die Korrektheit der Umrechnungsformeln automatisch sicherzustellen.
  
- Zusätzliche Module (Schuhgrößen): Der Vorschlag von Samara, fixe Parameter wie Schuhgrößen zu ergänzen, wird als Erweiterung der Skalierbarkeit aufgenommen.
  
3. Nicht umgesetzte Punkte (mit Begründung)
- Zusammenführung von Docstrings und regulären Kommentaren: Samara merkte an, dass Docstrings nicht unter regulären Kommentaren stehen sollten. Wir haben uns entschieden, erklärende Kommentare für komplexe Algorithmen innerhalb der Funktionen beizubehalten, da Docstrings nur die Schnittstelle (Was macht die Funktion?), aber nicht den Ablauf (Wie macht sie es?) beschreiben sollen.

<img width="453" height="686" alt="image" src="https://github.com/user-attachments/assets/33dc93bf-c451-495f-a178-50910973d021" />


