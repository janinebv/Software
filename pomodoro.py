import tkinter as tk  # stellt die GUI-Komponenten bereit
from tkinter import messagebox  # für Fehlermeldungen

class PomodoroLogik:  # Timerlogik mit Phasen und Sitzungstyp (1 oder 2 Pomodoros)
    def __init__(self):
        
        # Standardwerte (werden über Sitzungstyp überschrieben)
        self.lern_sekunden = 25 * 60
        self.kurze_pause_sekunden = 5 * 60
        self.lange_pause_sekunden = 15 * 60

        self.verbleibende_sekunden = 0
        self.aktuelle_phase = "bereit"        # "bereit", "lernen", "kurze_pause", "lange_pause"

        self.abgeschlossene_pomodoros = 0
        self.pomodoros_bis_lange_pause = 4
        self.pomodoros_seit_langer_pause = 0

        self.pomodoros_pro_sitzung = 1       # 1 bei Standard, 2 bei Kombi

    def konfiguration_setzen(self, lern_sec, kurz_sec, lang_sec, pomodoros_pro_sitzung):  # Sitzungstyp-Settings setzen
        
        self.lern_sekunden = lern_sec
        self.kurze_pause_sekunden = kurz_sec
        self.lange_pause_sekunden = lang_sec
        self.pomodoros_pro_sitzung = pomodoros_pro_sitzung

    def lernphase_starten(self):  # Startet eine Lernphase
        
        self.aktuelle_phase = "lernen"
        self.verbleibende_sekunden = self.lern_sekunden

    def kurze_pause_starten(self):  # Startet eine kurze Pause
        
        self.aktuelle_phase = "kurze_pause"
        self.verbleibende_sekunden = self.kurze_pause_sekunden

    def lange_pause_starten(self):  # Startet eine lange Pause
        
        self.aktuelle_phase = "lange_pause"
        self.verbleibende_sekunden = self.lange_pause_sekunden

    def zuruecksetzen(self):  # Setzt Phase und Zähler zurück
        
        self.aktuelle_phase = "bereit"
        self.verbleibende_sekunden = 0
        self.pomodoros_seit_langer_pause = 0

    def nur_phase_zuruecksetzen(self):  # Setzt nur Phase/Restzeit zurück
        
        self.aktuelle_phase = "bereit"
        self.verbleibende_sekunden = 0

    def eine_sekunde_vergehen(self):  # Zählt eine Sekunde herunter, nutzt Sitzungstyp-Pomodoros
        
        if self.aktuelle_phase in ("lernen", "kurze_pause", "lange_pause") and self.verbleibende_sekunden > 0:
            self.verbleibende_sekunden -= 1

            if self.verbleibende_sekunden == 0:
                if self.aktuelle_phase == "lernen":
                    self.abgeschlossene_pomodoros += self.pomodoros_pro_sitzung
                    self.pomodoros_seit_langer_pause += self.pomodoros_pro_sitzung
                return True

        return False

    def phasenname_holen(self):  # Text für die aktuelle Phase
        
        if self.aktuelle_phase == "lernen":
            return "Lernphase"
        elif self.aktuelle_phase == "kurze_pause":
            return "Kurze Pause"
        elif self.aktuelle_phase == "lange_pause":
            return "Lange Pause"
        else:
            return "Bereit"

# GUI mit Sitzungstyp-Auswahl:

class PomodoroAnwendung:  # Fenster mit Sitzungstypen und Phasenlogik
    def __init__(self, root):
       
        self.root = root
        self.root.title("Pomodoro-Timer mit Sitzungstypen")
        self.root.resizable(False, False)

        self.logik = PomodoroLogik()
        self.timer_laueft = False

        self.farbe_lernen = "#ffcccc"
        self.farbe_pause = "#ccffcc"
        self.farbe_bereit = "#ffffff"

        self.gui_aufbauen()
        self.anzeige_aktualisieren()

    def gui_aufbauen(self):  # Erstellung der GUI inkl. Sitzungstypen
        
        einstellungen_frame = tk.LabelFrame(self.root, text="Einstellungen")
        einstellungen_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(einstellungen_frame, text="Sitzungstyp:").grid(row=0, column=0, sticky="w")

        self.var_sitzungstyp = tk.StringVar(value="demo_standard")  # Sitzungstyp-Variable

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

        self.rb_demo_standard.grid(row=0, column=1, columnspan=2, sticky="w")
        self.rb_demo_kombi.grid(row=1, column=1, columnspan=2, sticky="w")
        self.rb_standard.grid(row=2, column=1, columnspan=2, sticky="w")
        self.rb_kombi.grid(row=3, column=1, columnspan=2, sticky="w")

        tk.Label(einstellungen_frame, text="Lange Pause:").grid(row=4, column=0, sticky="w")
        self.var_lange_pause = tk.StringVar(value="15 Sekunden")
        lange_pause_optionen = ["15 Sekunden", "15 Minuten", "20 Minuten", "25 Minuten", "30 Minuten"]
        option_lange_pause = tk.OptionMenu(einstellungen_frame, self.var_lange_pause, *lange_pause_optionen)
        option_lange_pause.grid(row=4, column=1, sticky="w")

        status_frame = tk.LabelFrame(self.root, text="Aktueller Status")
        status_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        status_frame.grid_columnconfigure(0, weight=1)

        self.label_phase = tk.Label(status_frame, text="Phase: Bereit", font=("Arial", 14), anchor="center")
        self.label_phase.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        self.label_countdown = tk.Label(status_frame, text="00:00", font=("Arial", 24), anchor="center")
        self.label_countdown.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.label_nachricht = tk.Label(status_frame, text="", font=("Arial", 10), anchor="center", wraplength=320)
        self.label_nachricht.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        button_frame = tk.Frame(self.root)
        button_frame.grid(row=2, column=0, padx=10, pady=10)

        self.button_start = tk.Button(button_frame, text="Start", width=10, command=self.timer_starten)
        self.button_start.grid(row=0, column=0, padx=5)

        self.button_reset = tk.Button(button_frame, text="Reset", width=10, command=self.timer_zuruecksetzen)
        self.button_reset.grid(row=0, column=1, padx=5)

    def einstellungen_aus_gui_lesen(self):  # Sitzungstyp auslesen und an Logik übergeben
        
        sitzungstyp = self.var_sitzungstyp.get()

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

        self.logik.konfiguration_setzen(
            lern_sec=lern_sec,
            kurz_sec=kurz_sec,
            lang_sec=lang_sec,
            pomodoros_pro_sitzung=pomodoros_pro_sitzung,
        )

        return True

    def timer_starten(self):  # Startet Lernphase mit gewähltem Sitzungstyp
        
        if self.logik.aktuelle_phase == "bereit":
            if not self.einstellungen_aus_gui_lesen():
                return
            self.logik.lernphase_starten()
            self.label_nachricht.config(text="Lernphase gestartet.")
        self.timer_laueft = True
        self.anzeige_aktualisieren()
        self.timer_schritt()

    def timer_zuruecksetzen(self):  # Stoppt Timer und setzt alles zurück
        
        self.timer_laueft = False
        self.logik.zuruecksetzen()
        self.label_nachricht.config(text="Zurückgesetzt.")
        self.anzeige_aktualisieren()
        self.root.configure(bg=self.farbe_bereit)

    def timer_schritt(self):  # Wird jede Sekunde aufgerufen, solange der Timer läuft
        
        if not self.timer_laueft:
            return

        phase_beendet = self.logik.eine_sekunde_vergehen()
        self.anzeige_aktualisieren()

        if phase_beendet:
            if self.logik.aktuelle_phase == "lernen":
                if self.logik.pomodoros_seit_langer_pause >= self.logik.pomodoros_bis_lange_pause:
                    self.logik.pomodoros_seit_langer_pause = 0
                    self.logik.lange_pause_starten()
                    self.label_nachricht.config(text="Lernphase beendet – lange Pause beginnt!")
                else:
                    self.logik.kurze_pause_starten()
                    self.label_nachricht.config(text="Lernphase beendet – kurze Pause beginnt!")
            elif self.logik.aktuelle_phase in ("kurze_pause", "lange_pause"):
                self.label_nachricht.config(text="Pause beendet – drücke Start für die nächste Lernphase.")
                self.timer_laueft = False
                self.logik.nur_phase_zuruecksetzen()
                self.anzeige_aktualisieren()
                return

        self.root.after(1000, self.timer_schritt)

    def anzeige_aktualisieren(self):  # Aktualisiert Phase, Countdown und Hintergrund
        
        phasenname = self.logik.phasenname_holen()
        self.label_phase.config(text=f"Phase: {phasenname}")

        sekunden = self.logik.verbleibende_sekunden
        minuten = sekunden // 60
        rest = sekunden % 60
        self.label_countdown.config(text=f"{minuten:02d}:{rest:02d}")

        if self.logik.aktuelle_phase == "lernen":
            self.root.configure(bg=self.farbe_lernen)
        elif self.logik.aktuelle_phase in ("kurze_pause", "lange_pause"):
            self.root.configure(bg=self.farbe_pause)
        else:
            self.root.configure(bg=self.farbe_bereit)

# Start des Programms:

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroAnwendung(root)
    root.mainloop()