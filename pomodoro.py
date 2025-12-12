import tkinter as tk  # stellt die GUI-Komponenten bereit

class PomodoroLogik:  # Lernphase mit kurzer und langer Pause (Demo-Werte)
    def __init__(self):
        
        self.lern_sekunden = 10               # Demo: 10 Sekunden lernen
        self.kurze_pause_sekunden = 5         # Demo: 5 Sekunden kurze Pause
        self.lange_pause_sekunden = 15        # Demo: 15 Sekunden lange Pause

        self.verbleibende_sekunden = 0        # Restzeit in Sekunden
        self.aktuelle_phase = "bereit"        # "bereit", "lernen", "kurze_pause", "lange_pause"

        self.abgeschlossene_pomodoros = 0     # Anzahl abgeschlossener Pomodoros
        self.pomodoros_bis_lange_pause = 4    # nach 4 Pomodoros → lange Pause
        self.pomodoros_seit_langer_pause = 0  # Zähler seit letzter langer Pause

    def lernphase_starten(self):  # Startet eine neue Lernphase
        
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

    def eine_sekunde_vergehen(self):  # Zählt eine Sekunde herunter, aktualisiert Pomodoros
        
        if self.aktuelle_phase in ("lernen", "kurze_pause", "lange_pause") and self.verbleibende_sekunden > 0:
            self.verbleibende_sekunden -= 1

            if self.verbleibende_sekunden == 0:
                if self.aktuelle_phase == "lernen":
                    self.abgeschlossene_pomodoros += 1          # ein Pomodoro fertig
                    self.pomodoros_seit_langer_pause += 1       # Zähler erhöhen
                return True                                     # Phase ist zu Ende

        return False                                            # Phase läuft weiter

    def phasenname_holen(self):  # Text für die aktuelle Phase
        
        if self.aktuelle_phase == "lernen":
            return "Lernphase"
        elif self.aktuelle_phase == "kurze_pause":
            return "Kurze Pause"
        elif self.aktuelle_phase == "lange_pause":
            return "Lange Pause"
        else:
            return "Bereit"

# GUI mit Phasen:

class PomodoroAnwendung:  # Fenster mit Phasen-Anzeige und Farben
    def __init__(self, root):
       
        self.root = root
        self.root.title("Pomodoro-Timer mit Phasen")
        self.root.resizable(False, False)

        self.logik = PomodoroLogik()
        self.timer_laueft = False  # Zeigt, ob der Timer aktiv ist

        self.farbe_lernen = "#ffcccc"  # Hintergrund für Lernphase
        self.farbe_pause = "#ccffcc"   # Hintergrund für Pausen
        self.farbe_bereit = "#ffffff"  # Hintergrund für Bereitschaft

        self.gui_aufbauen()
        self.anzeige_aktualisieren()

    def gui_aufbauen(self):  # Erstellung der GUI-Elemente
        
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        self.label_phase = tk.Label(frame, text="Phase: Bereit", font=("Arial", 14))
        self.label_phase.pack(pady=5)

        self.label_countdown = tk.Label(frame, text="00:00", font=("Arial", 24))
        self.label_countdown.pack(pady=5)

        self.label_info = tk.Label(frame, text="Pomodoros seit letzter langer Pause: 0", font=("Arial", 10))
        self.label_info.pack(pady=5)

        button_frame = tk.Frame(frame)
        button_frame.pack(pady=5)

        self.button_start = tk.Button(button_frame, text="Start", width=10, command=self.timer_starten)
        self.button_start.grid(row=0, column=0, padx=5)

        self.button_reset = tk.Button(button_frame, text="Reset", width=10, command=self.timer_zuruecksetzen)
        self.button_reset.grid(row=0, column=1, padx=5)

        self.label_nachricht = tk.Label(frame, text="", font=("Arial", 10))
        self.label_nachricht.pack(pady=5)

    def timer_starten(self):  # Startet Lernphase oder fährt Timer fort
        
        if self.logik.aktuelle_phase == "bereit":
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
                # entscheiden, ob kurze oder lange Pause
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

    def anzeige_aktualisieren(self):  # Aktualisiert Phase, Countdown, Info und Hintergrund
        
        phasenname = self.logik.phasenname_holen()
        self.label_phase.config(text=f"Phase: {phasenname}")

        sekunden = self.logik.verbleibende_sekunden
        minuten = sekunden // 60
        rest = sekunden % 60
        self.label_countdown.config(text=f"{minuten:02d}:{rest:02d}")

        self.label_info.config(
            text=f"Pomodoros seit letzter langer Pause: {self.logik.pomodoros_seit_langer_pause}"
        )

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