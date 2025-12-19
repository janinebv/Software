import tkinter as tk  # stellt die GUI-Komponenten bereit
from tkinter import messagebox  # für Popup-Fehlermeldungen und Hinweise

# Logik-Komponente (ohne GUI):

class PomodoroLogik:  # Timer- und Phasenlogik (Lernen, Pausen, Statistik)
    def __init__(self):  # Initialisiert Standardwerte für Zeiten, Phase und Statistik
        
        # Standardzeiten in Sekunden (werden später je nach Sitzungstyp überschrieben)
        self.lern_sekunden = 25 * 60          # Lernzeit pro Sitzung
        self.kurze_pause_sekunden = 5 * 60    # Dauer einer kurzen Pause
        self.lange_pause_sekunden = 15 * 60   # Dauer einer langen Pause

        # Aktueller Status
        self.verbleibende_sekunden = 0        # Restzeit in Sekunden
        self.aktuelle_phase = "bereit"        # "bereit", "lernen", "kurze_pause", "lange_pause"

        # Statistik
        self.abgeschlossene_pomodoros = 0     # Anzahl abgeschlossener Pomodoros
        self.gesamt_lern_sekunden = 0         # gesamte Lernzeit in Sekunden

        # Steuerung der langen Pause
        self.pomodoros_bis_lange_pause = 4    # nach wie vielen Pomodoros eine lange Pause kommt
        self.pomodoros_seit_langer_pause = 0  # Zähler seit der letzten langen Pause

        # wie viele Pomodoros in einer Sitzung stecken (1 Standard oder 2 Kombi)
        self.pomodoros_pro_sitzung = 1

        # Thema/Fach der aktuellen Sitzung
        self.thema = ""

        # Liste abgeschlossener Lerneinheiten [(thema, sekunden), ...]
        self.sitzungen = []

        # Lernzeit in der aktuell laufenden Lernphase (für Abbruch)
        self.aktuelle_lernsekunden_in_dieser_phase = 0

    def konfiguration_setzen(self, lern_sec, kurz_sec, lang_sec, pomodoros_pro_sitzung, thema):  # Konfiguration für nächste Sitzung setzen
        
        self.lern_sekunden = lern_sec
        self.kurze_pause_sekunden = kurz_sec
        self.lange_pause_sekunden = lang_sec
        self.pomodoros_pro_sitzung = pomodoros_pro_sitzung
        self.thema = thema.strip()

    def lernphase_starten(self):  # Startet eine neue Lernphase
        
        self.aktuelle_phase = "lernen"
        self.verbleibende_sekunden = self.lern_sekunden
        self.aktuelle_lernsekunden_in_dieser_phase = 0  # Startwert für diese Lernphase

    def kurze_pause_starten(self):  # Startet eine kurze Pause
        
        self.aktuelle_phase = "kurze_pause"
        self.verbleibende_sekunden = self.kurze_pause_sekunden

    def lange_pause_starten(self):  # Startet eine lange Pause
        
        self.aktuelle_phase = "lange_pause"
        self.verbleibende_sekunden = self.lange_pause_sekunden

    def zuruecksetzen(self):  # Setzt Phase und Zähler für lange Pause zurück (Statistik bleibt)
        
        self.aktuelle_phase = "bereit"
        self.verbleibende_sekunden = 0
        self.pomodoros_seit_langer_pause = 0
        self.aktuelle_lernsekunden_in_dieser_phase = 0

    def nur_phase_zuruecksetzen(self):  # Setzt nur die Phase/Restzeit zurück, Statistik bleibt
        
        self.aktuelle_phase = "bereit"
        self.verbleibende_sekunden = 0
        self.aktuelle_lernsekunden_in_dieser_phase = 0

    def abgebrochene_lernphase_speichern(self):  # Speichert Lernzeit, wenn eine Lernphase vorzeitig abgebrochen wird
        
        if self.aktuelle_phase == "lernen" and self.aktuelle_lernsekunden_in_dieser_phase > 0:
            gelernt = self.aktuelle_lernsekunden_in_dieser_phase  # tatsächlich gelernte Sekunden in dieser Phase

            # Gesamtlernzeit wurde bereits sekündlich erhöht, deshalb hier nichts mehr addieren
            if self.thema:
                if self.sitzungen and self.sitzungen[-1][0] == self.thema:
                    # gleiches Thema wie davor → Zeit hinzufügen
                    letztes_thema, letzte_sekunden = self.sitzungen[-1]
                    self.sitzungen[-1] = (letztes_thema, letzte_sekunden + gelernt)
                else:
                    # neues Thema bzw. anderes Thema → neuer Eintrag
                    self.sitzungen.append((self.thema, gelernt))

            # Kein abgeschlossener Pomodoro, daher:
            # - abgeschlossene_pomodoros NICHT erhöhen
            # - pomodoros_seit_langer_pause NICHT erhöhen

            self.aktuelle_lernsekunden_in_dieser_phase = 0  # zurücksetzen

    def eine_sekunde_vergehen(self):  # Zählt eine Sekunde herunter, aktualisiert Statistik bei Lernende
                                      # True = Phase gerade zu Ende gegangen, sonst False
                                     
        if self.aktuelle_phase in ("lernen", "kurze_pause", "lange_pause") and self.verbleibende_sekunden > 0:
            self.verbleibende_sekunden -= 1  # eine Sekunde abziehen

            if self.aktuelle_phase == "lernen":  # Lernsekunde zur Gesamtlernzeit addieren
                self.gesamt_lern_sekunden += 1
                self.aktuelle_lernsekunden_in_dieser_phase += 1  # Lernzeit dieser Phase erhöhen

            if self.verbleibende_sekunden == 0:  # Phase ist zu Ende
                if self.aktuelle_phase == "lernen":
                    # Pomodoros zählen (1 bei Standard, 2 bei Kombi)
                    self.abgeschlossene_pomodoros += self.pomodoros_pro_sitzung
                    self.pomodoros_seit_langer_pause += self.pomodoros_pro_sitzung

                    # Lerneinheit für Statistik speichern (hier komplette Lernphase)
                    gelernt = self.aktuelle_lernsekunden_in_dieser_phase
                    if self.thema:
                        if self.sitzungen and self.sitzungen[-1][0] == self.thema:
                            # gleiches Thema wie davor → Zeit hinzufügen
                            letztes_thema, letzte_sekunden = self.sitzungen[-1]
                            self.sitzungen[-1] = (letztes_thema, letzte_sekunden + gelernt)
                        else:
                            # neues Thema bzw. anderes Thema → neuer Eintrag
                            self.sitzungen.append((self.thema, gelernt))

                    self.aktuelle_lernsekunden_in_dieser_phase = 0  # nach abgeschlossener Phase zurücksetzen

                return True  # Phase (lernen/kurze_pause/lange_pause) ist beendet

        return False  # Phase läuft weiter

    def phasenname_holen(self):  # Text für die aktuelle Phase
        
        if self.aktuelle_phase == "lernen":
            return "Lernphase"
        elif self.aktuelle_phase == "kurze_pause":
            return "Kurze Pause"
        elif self.aktuelle_phase == "lange_pause":
            return "Lange Pause"
        else:
            return "Bereit"

    def statistik_text_holen(self):  # Baut den Anzeigetext für die Statistik zusammen
        
        gesamt_min = self.gesamt_lern_sekunden // 60
        gesamt_sek = self.gesamt_lern_sekunden % 60

        zeilen = [
            "Statistik dieser Sitzung:",
            f"Abgeschlossene Einheiten (Pomodoros): {self.abgeschlossene_pomodoros}",
            f"Gesamtlernzeit: {gesamt_min} Minuten ({gesamt_sek} Sekunden)",
            "Themen / Einheiten:"
        ]

        if self.sitzungen:
            for index, (thema, sekunden) in enumerate(self.sitzungen, start=1):
                m = sekunden // 60
                s = sekunden % 60
                thema_name = thema if thema else "-"
                zeilen.append(f" {index}. {thema_name}: {m} Min ({s} Sek)")
        else:
            zeilen.append(" - keine Einheiten erfasst")

        return "\n".join(zeilen)


# GUI-Komponente:

class PomodoroAnwendung:  # Erstellung des Fensters inkl. Logik und Steuerung
    def __init__(self, root):
        
        self.root = root
        self.root.title("Lern-Trainer (Pomodoro)")
        self.root.resizable(False, False)

        self.logik = PomodoroLogik()  # Logik-Objekt für Timer & Statistik
        self.timer_laueft = False     # Zeigt an, ob der Timer aktiv ist

        # Farben für Hintergrund je nach Phase
        self.farbe_lernen = "#ffcccc"
        self.farbe_pause = "#ccffcc"
        self.farbe_bereit = "#ffffff"

        self.gui_aufbauen()           # GUI-Elemente erstellen
        self.anzeige_aktualisieren()  # Startanzeige setzen

        # Fenstergröße fixieren (nicht kleiner skalieren)
        self.root.update_idletasks()
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())

        # Sitzungstyp-Auswahl je nach Pomodoro-Zähler anpassen
        self.sitzungstyp_optionen_aktualisieren()

    def gui_aufbauen(self):  # Erstellung der GUI-Elemente (Einstellungen, Status, Buttons, Statistik)
        
        # Einstellungen (Sitzungstyp, lange Pause, Thema)
        einstellungen_frame = tk.LabelFrame(self.root, text="Einstellungen")
        einstellungen_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(einstellungen_frame, text="Sitzungstyp:").grid(row=0, column=0, sticky="w")

        # Sitzungstyp als Radiobuttons (Demo & Normal)
        self.var_sitzungstyp = tk.StringVar(value="demo_standard")  # Standardauswahl: Demo Standard

        self.rb_demo_standard = tk.Radiobutton(
            einstellungen_frame,
            text="Demo Standard: 10 Sek lernen / 10 Sek Pause",
            variable=self.var_sitzungstyp,
            value="demo_standard",
        )
        self.rb_demo_kombi = tk.Radiobutton(
            einstellungen_frame,
            text="Demo Kombi: 20 Sek lernen / 20 Sek Pause",
            variable=self.var_sitzungstyp,
            value="demo_kombi",
        )
        self.rb_standard = tk.Radiobutton(
            einstellungen_frame,
            text="Standard: 25 Min lernen / 5 Min Pause",
            variable=self.var_sitzungstyp,
            value="standard",
        )
        self.rb_kombi = tk.Radiobutton(
            einstellungen_frame,
            text="Kombi: 50 Min lernen / 10 Min Pause",
            variable=self.var_sitzungstyp,
            value="kombi",
        )

        # Radiobuttons anordnen
        self.rb_demo_standard.grid(row=0, column=1, columnspan=2, sticky="w")
        self.rb_demo_kombi.grid(row=1, column=1, columnspan=2, sticky="w")
        self.rb_standard.grid(row=2, column=1, columnspan=2, sticky="w")
        self.rb_kombi.grid(row=3, column=1, columnspan=2, sticky="w")

        # Auswahl für lange Pause
        tk.Label(einstellungen_frame, text="Lange Pause:").grid(row=4, column=0, sticky="w")
        self.var_lange_pause = tk.StringVar(value="15 Sekunden")  # Standard: Demo lange Pause
        lange_pause_optionen = ["15 Sekunden", "15 Minuten", "20 Minuten", "25 Minuten", "30 Minuten"]
        option_lange_pause = tk.OptionMenu(einstellungen_frame, self.var_lange_pause, *lange_pause_optionen)
        option_lange_pause.grid(row=4, column=1, sticky="w")

        # Eingabefeld Thema/Fach
        tk.Label(einstellungen_frame, text="Thema/Fach:").grid(row=5, column=0, sticky="w")
        self.entry_thema = tk.Entry(einstellungen_frame, width=25)
        self.entry_thema.grid(row=5, column=1, columnspan=2, sticky="w")

        # Status / Countdown
        status_frame = tk.LabelFrame(self.root, text="Aktueller Status")
        status_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        status_frame.grid_columnconfigure(0, weight=1)  # Inhalt mittig

        self.label_phase = tk.Label(  # zeigt die aktuelle Phase an
            status_frame,
            text="Phase: Bereit",
            font=("Arial", 14),
            anchor="center",
            justify="center"
        )
        self.label_phase.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        self.label_countdown = tk.Label(  # zeigt den Countdown im Format MM:SS
            status_frame,
            text="00:00",
            font=("Arial", 24),
            anchor="center",
            justify="center",
            width=8
        )
        self.label_countdown.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.label_nachricht = tk.Label(  # Textfeld für Hinweise (z. B. Phase beendet)
            status_frame,
            text="",
            font=("Arial", 10),
            anchor="center",
            justify="center",
            wraplength=320,
            width=50
        )
        self.label_nachricht.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        # Buttons (Start, Pause, Reset, Lernen beenden)
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=2, column=0, padx=10, pady=10)

        self.button_start = tk.Button(button_frame, text="Start", width=10, command=self.timer_starten)
        self.button_start.grid(row=0, column=0, padx=5)

        self.button_pause = tk.Button(button_frame, text="Pause", width=10, command=self.timer_pausieren)
        self.button_pause.grid(row=0, column=1, padx=5)

        self.button_reset = tk.Button(button_frame, text="Reset", width=10, command=self.timer_zuruecksetzen)
        self.button_reset.grid(row=0, column=2, padx=5)

        self.button_beenden = tk.Button(
            button_frame,
            text="Lernen beenden",
            width=15,
            command=self.lernen_beenden
        )
        self.button_beenden.grid(row=1, column=0, columnspan=3, pady=(5, 0))

        # Statistik-Anzeige
        statistik_frame = tk.LabelFrame(self.root, text="Statistik dieser Sitzung")
        statistik_frame.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.label_statistik = tk.Label(statistik_frame, text=self.logik.statistik_text_holen(), justify="left")
        self.label_statistik.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    def sitzungstyp_optionen_aktualisieren(self):  # Aktiviert/Deaktiviert Sitzungstypen (max. 4 Pomodoros vor langer Pause)
        
        aktueller_zaehler = self.logik.pomodoros_seit_langer_pause
        limit = self.logik.pomodoros_bis_lange_pause
        verbleibend = limit - aktueller_zaehler  # wie viele Pomodoros noch möglich sind

        mapping = [  # Radiobutton, Modusname, Pomodoros dieser Sitzung
            (self.rb_demo_standard, "demo_standard", 1),
            (self.rb_standard, "standard", 1),
            (self.rb_demo_kombi, "demo_kombi", 2),
            (self.rb_kombi, "kombi", 2),
        ]

        # Sitzungstyp ausgrauen, wenn er zu viele Pomodoros bringen würde
        for rb, modus, anzahl in mapping:
            if anzahl <= verbleibend:
                rb.config(state="normal")
            else:
                rb.config(state="disabled")

        aktueller_modus = self.var_sitzungstyp.get()

        def pomodoros_fuer_modus(m):  # Hilfsfunktion: Anzahl Pomodoros je Modus
            if m in ("demo_standard", "standard"):
                return 1
            elif m in ("demo_kombi", "kombi"):
                return 2
            return 999

        # Falls aktueller Modus nicht mehr erlaubt ist → auf passenden Modus wechseln
        if pomodoros_fuer_modus(aktueller_modus) > verbleibend and verbleibend > 0:
            for rb, modus, anzahl in mapping:
                if anzahl <= verbleibend:
                    self.var_sitzungstyp.set(modus)
                    break

    def einstellungen_aus_gui_lesen(self):  # Sitzungstyp, lange Pause & Thema auslesen, an Logik übergeben
        
        sitzungstyp = self.var_sitzungstyp.get()

        # Zeiten und Pomodoros je Sitzungstyp setzen
        if sitzungstyp == "demo_standard":
            lern_sec = 10
            kurz_sec = 10
            pomodoros_pro_sitzung = 1
        elif sitzungstyp == "demo_kombi":
            lern_sec = 20
            kurz_sec = 20
            pomodoros_pro_sitzung = 2
        elif sitzungstyp == "standard":
            lern_sec = 25 * 60
            kurz_sec = 5 * 60
            pomodoros_pro_sitzung = 1
        elif sitzungstyp == "kombi":
            lern_sec = 50 * 60
            kurz_sec = 10 * 60
            pomodoros_pro_sitzung = 2
        else:
            messagebox.showerror("Fehler", "Bitte einen Sitzungstyp auswählen.")
            return False

        # Prüfen, ob mit dieser Sitzung mehr als 4 Pomodoros entstehen würden
        aktueller_zaehler = self.logik.pomodoros_seit_langer_pause
        limit = self.logik.pomodoros_bis_lange_pause
        if aktueller_zaehler + pomodoros_pro_sitzung > limit:
            messagebox.showerror(
                "Fehler",
                "Mit dieser Auswahl würdest du mehr als 4 Pomodoros vor der langen Pause planen.\n"
                "Bitte eine kleinere Sitzung wählen."
            )
            return False

        # Lange Pause-Option auslesen
        lange_pause_wahl = self.var_lange_pause.get()
        if lange_pause_wahl == "15 Sekunden":
            lang_sec = 15
        elif lange_pause_wahl == "15 Minuten":
            lang_sec = 15 * 60
        elif lange_pause_wahl == "20 Minuten":
            lang_sec = 20 * 60
        elif lange_pause_wahl == "25 Minuten":
            lang_sec = 25 * 60
        elif lange_pause_wahl == "30 Minuten":
            lang_sec = 30 * 60
        else:
            lang_sec = 15 * 60

        # Thema einlesen
        thema = self.entry_thema.get()

        # Konfiguration in die Logik übergeben
        self.logik.konfiguration_setzen(
            lern_sec=lern_sec,
            kurz_sec=kurz_sec,
            lang_sec=lang_sec,
            pomodoros_pro_sitzung=pomodoros_pro_sitzung,
            thema=thema,
        )

        return True

    def timer_starten(self):  # Startet Lernphase und Timer (oder setzt Timer fort)
        
        if self.logik.aktuelle_phase == "bereit":
            if not self.einstellungen_aus_gui_lesen():  # Einstellungen prüfen
                return
            self.logik.lernphase_starten()
            self.label_nachricht.config(text="Lernphase gestartet. Viel Erfolg!", fg="black")

        self.timer_laueft = True
        self.anzeige_aktualisieren()
        self.timer_schritt()

    def timer_pausieren(self):  # Pausiert den Timer (Zeit bleibt stehen)
        
        self.timer_laueft = False
        self.label_nachricht.config(text="Timer pausiert.", fg="black")

    def timer_zuruecksetzen(self):  # Stoppt den Timer und setzt Phase/Zähler zurück (aber speichert evtl. Lernzeit)
        
        # vor dem Zurücksetzen prüfen, ob wir gerade in einer Lernphase waren
        self.logik.abgebrochene_lernphase_speichern()

        self.timer_laueft = False
        self.logik.zuruecksetzen()
        self.label_nachricht.config(text="Zurückgesetzt. Bereit für eine neue Lernphase.", fg="black")
        self.anzeige_aktualisieren()
        self.root.configure(bg=self.farbe_bereit)
        self.sitzungstyp_optionen_aktualisieren()

    def lernen_beenden(self):  # Beendet die aktuelle Sitzung (speichert evtl. Lernzeit, Statistik bleibt sichtbar)
        
        # vor dem Beenden ggf. Teil-Lernzeit speichern
        self.logik.abgebrochene_lernphase_speichern()

        self.timer_laueft = False
        self.logik.zuruecksetzen()
        self.label_nachricht.config(text="Lerneinheit beendet. Gute Arbeit!", fg="black")
        self.anzeige_aktualisieren()
        self.root.configure(bg=self.farbe_bereit)
        self.sitzungstyp_optionen_aktualisieren()

    def timer_schritt(self):  # Wird jede Sekunde aufgerufen, solange der Timer läuft
        
        if not self.timer_laueft:
            return

        phase_beendet = self.logik.eine_sekunde_vergehen()  # Logik um 1 Sekunde fortschreiben
        self.anzeige_aktualisieren()

        if phase_beendet:
            beendete_phase = self.logik.aktuelle_phase

            if beendete_phase == "lernen":
                # Nach Lernphase: kurze oder lange Pause wählen
                if self.logik.pomodoros_seit_langer_pause >= self.logik.pomodoros_bis_lange_pause:
                    self.logik.pomodoros_seit_langer_pause = 0
                    self.logik.lange_pause_starten()
                else:
                    self.logik.kurze_pause_starten()

                self.phasenwechsel_meldung_zeigen("lernen")

            elif beendete_phase in ("kurze_pause", "lange_pause"):
                # Nach einer Pause → Sitzung fertig, Nutzer entscheidet neu
                self.phasenwechsel_meldung_zeigen(beendete_phase)
                self.timer_laueft = False
                self.logik.nur_phase_zuruecksetzen()
                self.anzeige_aktualisieren()
                self.sitzungstyp_optionen_aktualisieren()
                return

        # nächsten Tick in 1 Sekunde planen
        self.root.after(1000, self.timer_schritt)

    def anzeige_aktualisieren(self):  # Aktualisiert Phase, Countdown, Hintergrundfarbe und Statistik
        
        phasenname = self.logik.phasenname_holen()
        self.label_phase.config(text=f"Phase: {phasenname}")

        sekunden = self.logik.verbleibende_sekunden
        minuten = sekunden // 60
        rest_sekunden = sekunden % 60
        self.label_countdown.config(text=f"{minuten:02d}:{rest_sekunden:02d}")

        # Hintergrundfarbe je nach Phase
        if self.logik.aktuelle_phase == "lernen":
            self.root.configure(bg=self.farbe_lernen)
        elif self.logik.aktuelle_phase in ("kurze_pause", "lange_pause"):
            self.root.configure(bg=self.farbe_pause)
        else:
            self.root.configure(bg=self.farbe_bereit)

        # Statistik aktualisieren
        self.label_statistik.config(text=self.logik.statistik_text_holen())

    def phasenwechsel_meldung_zeigen(self, beendete_phase):  # Ton & Textausgabe bei Phasenwechsel
        
        try:
            self.root.bell()  # Systemton abspielen (falls unterstützt)
        except Exception:
            pass

        if beendete_phase == "lernen":
            # Lernphase zu Ende → Pause beginnt
            self.label_nachricht.config(
                text="Lernphase beendet – Zeit für eine Pause!",
                fg="red"
            )
        elif beendete_phase in ("kurze_pause", "lange_pause"):
            # Pause zu Ende → Nutzer wählt neue Sitzung
            self.label_nachricht.config(
                text="Pause beendet – wähle, ob du mit Demo Standard, Demo Kombi, 25/5 oder 50/10 weitermachen willst und drücke Start.",
                fg="green"
            )
        else:
            self.label_nachricht.config(text="", fg="black")


# Start des Programms:

if __name__ == "__main__":  # Eintrittspunkt des Programms
    root = tk.Tk()          # Hauptfenster erzeugen
    app = PomodoroAnwendung(root)  # Anwendung mit Logik & GUI starten
    root.mainloop()         # Ereignisschleife von tkinter starten

# Ende des Programms