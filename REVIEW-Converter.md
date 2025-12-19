Feedback von Vanessa:



•  Korrektheit: 

Die Grundfunktionalität läuft sauber: Menü für Temperatur- oder Währungsrechner funktioniert und die Ergebnisse werden korrekt berechnet und formatiert.


•  Lesbarkeit: Der Code ist gut lesbar mit klaren Funktionsnamen, sinnvollen Aufteilungen in kleine Funktionen und mit vielen gut verständlichen Kommentaren.

Verbesserung: Einige """ ... """-Blöcke stehen außerhalb von Funktionen und sind damit keine „echten“ Docstrings, daher besser mit # auskommentieren oder als richtige Docstrings direkt in die passende Funktion setzen.


•  Effizienz: Optional: Bei mehreren Währungsumrechnungen hintereinander könnte man Kurse zwischenspeichern, statt jedes Mal neu abzurufen.


•  Wartbarkeit: Gut wartbar durch die saubere Trennung (Menü, Temperaturfunktionen, API, Währungsumrechnung) und Erweiterungen (z.B. weitere Währungen) sind relativ leicht möglich.


•  Fehlerbehandlung:

Zahleneingaben werden bei Temperatur und Währung mit try/except abgefangen, API-Fehler werden gut behandelt (Timeout, verständliche Meldungen).

Verbesserung: Bei der z.B. Temperatur können auch ungültige Buchstaben eingegeben werden (z.B. „G“) und das Programm fragt trotzdem noch nach dem Wert, bevor es den Fehler meldet. Das Programm könnte bei einem Fehler auch direkt nochmal nachfragen.


•  Sicherheit: Timeout beim API-Request wurde bedacht und eingebaut.


•  Einhaltung von Standards: Die verwendete Sprache (Python) wurde richtig angewendet.


•  Tests: Einige wichtige Fälle sind bereits im Code berücksichtigt, z.B. wenn Start- und Zielskala gleich sind (C == C), bleibt der Wert unverändert.



• Skalierbarkeit: Die Struktur ist gut: Menü, getrennte Funktionen, klare Logik. Optional: Wenn ihr später viele Umrechnungen macht, wäre Caching der Kurse sinnvoll.


Feedback von Samara

⦁ Korrektheit: Ja, der Code funktioniert korrekt und erfüllt die Anforderungen gemäß readme.
⦁ Lesbarkeit: Der Code ist gut lesbar. Persönlich würde ich Docstrings nicht unterhalb von regulären Kommentaren verwenden, da man sonst vielleicht eine Klasse, etc. erwartet, zu der diese nicht gehören.
⦁ Effizienz: Nach bisherigen Kenntnissen sieht der Code effizient aus und erfüllt den Zweck.
⦁ Wartbarkeit: Es sind soweit ausreichend Kommentare vorhanden. Nach bisherigem Kenntnisstand wirkt es als könnte man z.B. Module für Schuhgrößen EU zu US einarbeiten, da es dabei um fixe Parameter geht.
⦁ Fehlerbehandlung: Es gibt bei der API-Anbindung Timeout-Vermeidung und HTTPS-Statuscodes.
⦁ Einhaltung von Standards: Der Code entspricht den Standards zur Anwendung von python
⦁ Tests: Es sind keine Testfälle vorhanden. Der Code kann nur durch Ausführung getestet werden.
⦁ Skalierbarkeit: Der Code wäre skalierbar. Eine Umrechnungslogik kann nach gewissen Parametern ergänzt werden und sollte unkompliziert eingebunden werden können.