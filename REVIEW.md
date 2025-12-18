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


Feedback von Janine: 

1. Korrektheit: 
Der Code erfüllt die Anforderungen eines Pomodoro-Systems mit Arbeitsphase und kurzen/langen Pausen. 
Es funktioniert alles und die Grundlogik ist korrekt abgebildet. 
Der Timer stopp auch zur richitgen Zeit (also bei self.verbleibende_sekunden == 0). 
Dieser Code bietet keine benutzerdefinierte Eingabe, was aber für die Pomodoro-Methode ja nicht zwingend notwendig ist.

2. Lesbarkeit:
Die Trennung der Logik und der GUI ist sehr gut umgesetzt.
Die Namen der Variablen und Funktionen sind sehr klar gewählt und selbsterklärend. 
Der Code verwendet nur Kommentare mit # und keine """ Docstrings. 
Allerdings ist die Verwendung der Kommentare sehr hilfreich und klar.

3. Effizienz: 
Die Zeitsteuerung über root.after(1000,...) ist für eine GUI Anwendung effizient und ressourcensparend, da sie den Loop der GUI nicht blockiert.

4. Wartbarkeit: 
Der Code is gut durch Kommentare erklärt. Um die Wartbarkeit nach professionellen Standards zu verbessern, sollten einzeilige Kommentare über den Methoden in Python Docstrings (""") umgewandelt werden, so kann automatisch eine Dokumentation generiert werden. 

5. Fehlerbehandlung:
Die Anwendung nutzt messageboy.showerror, um ungültige Konfigurationen (zu viele Pomodoros vor einer Pause) abzufangen. Das sorgt für gute Benutzerführung und verhindert falsche Eingaben. 
Es fehlt allerdings eine Behandlung für vorzeitige Sitzungsabbrücke. Daten werden nur bei vollständigem Ablauf gespeichert, was zu Informationsverlust in der Statistik führen kann. 
Man könntee hier also eine Logik implementieren, die beim Klick auf "Reset" oder "Beenden" die tatsächlich verstrichene Zeit speichert, anstatt nur die geplante Zeit nach Erfolg zu speichern. 

6. Einhaltung von Standards: 
Python wird als Sprache sehr gut und richtig verwendet. 

7. Tests: 
Der Code kann durch die Demo-Modi gut getestet werden und die Funktionalität kann schnell und einfach geprüft werden. 

8. Skalierbarkeit: 
Der Code ist durch die Trennung von Logik und Benutzeroberfläche sehr gut skalierbar. 
Die Logik kann ohne Änderungen in größeren Oberflächen wie einer App eingesetzt werden. Außerdem isz es einfach, den Code um neue Funktionen zu erweitern. Hier wären zum Beispiel das Speichern der Statistiken in einer externen Datenbank denkbar. 

