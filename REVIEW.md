Feedback von Vanessa:



•  Korrektheit: 

Die Grundfunktionalität läuft sauber: Menü für Temperatur- oder Währungsrechner funktioniert und die Ergebnisse werden korrekt berechnet und formatiert.


•  Lesbarkeit: Der Code ist gut lesbar mit klaren Funktionsnamen, sinnvollen Aufteilungen in kleine Funktionen und mit vielen gut verständlichen Kommentaren.

Verbesserung: Einige """ ... """-Blöcke stehen außerhalb von Funktionen und sind damit keine „echten“ Docstrings, daher besser mit # auskommentieren oder als richtige Docstrings direkt in die passende Funktion setzen.


•  Effizienz: Optional: Bei mehreren Währungsumrechnungen hintereinander könnte man Kurse zwischenspeichern, statt jedes Mal neu abzurufen.


•  Wartbarkeit: Gut wartbar durch die saubere Trennung (Menü, Temperaturfunktionen, API, Währungsumrechnung) und Erweiterungen (z.B. weitere Währungen) sind relativ leicht möglich.


•  Fehlerbehandlung:

Zahleneingaben werden bei Temperatur und Währung mit try/except abgefangen, API-Fehler werden gut behandelt (Timeout, verständliche Meldungen).

Verbesserung: Bei der z.B. Temperatur können auch ungültige Buchstaben eingegeben werden (z.B. „G“) und das Programm fragt trotzdem noch nach dem Wert, bevor es den Fehler meldet. Das Programm bei einem Fehler auch direkt nochmal nachfragen.


•  Sicherheit: Timeout beim API-Request wurde bedacht und eingebaut.


•  Einhaltung von Standards: Die verwendete Sprache (Python) wurde richtig angewendet.


•  Tests: Einige wichtige Fälle sind bereits im Code berücksichtigt, z.B. wenn Start- und Zielskala gleich sind (C == C), bleibt der Wert unverändert.



• Skalierbarkeit: Die Struktur ist gut: Menü, getrennte Funktionen, klare Logik. Optional: Wenn ihr später viele Umrechnungen macht, wäre Caching der Kurse sinnvoll.



