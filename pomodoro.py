import tkinter as tk  # stellt die GUI-Komponenten bereit

class PomodoroLogik: # Lernphase mit fester Dauer (10 Sekunden)
    def __init__(self):
        
        self.lern_sekunden = 10              # Dauer der Lernphase (Demo: 10 Sekunden)
        self.verbleibende_sekunden = 0       # Restzeit in Sekunden
        self.aktuelle_phase = "bereit"       # "bereit" oder "lernen"

    def lernphase_starten(self): # Startet eine neue Lernphase
        
        self.aktuelle_phase = "lernen"
        self.verbleibende_sekunden = self.lern_sekunden

    def zuruecksetzen(self): # Setzt Pomodoro und Restzeit zurück auf den Ausgangszustand
        
        self.aktuelle_phase = "bereit"
        self.verbleibende_sekunden = 0

    def eine_sekunde_vergehen(self): # Zählt eine Sekunde herunter.
                                     # True = wenn die Lernphase gerade zu Ende gegangen ist, sonst False
                                     
        if self.aktuelle_phase == "lernen" and self.verbleibende_sekunden > 0:
            self.verbleibende_sekunden -= 1
            if self.verbleibende_sekunden == 0:
                # Lernphase ist fertig, zurück auf "bereit"
                self.aktuelle_phase = "bereit"
                return True
        return False

    def phasenname_holen(self): # Text für die aktuelle Pomodoro-Phase
        
        if self.aktuelle_phase == "lernen":
            return "Lernphase"
        else:
            return "Bereit"

# Erstellung GUI:

class PomodoroAnwendung: # Erstellung des Fensters inkl. vorheriger Logik
    def __init__(self, root):
       
        self.root = root
        self.root.title("Einfacher Pomodoro-Timer")
        self.root.resizable(False, False)

        self.logik = PomodoroLogik()
        self.timer_laueft = False  # Zeigt, ob der Timer aktiv ist

        self.gui_aufbauen()
        self.anzeige_aktualisieren()

    def gui_aufbauen(self): # Erstellung der GUI-Elemente
        
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        # Phase-Label
        self.label_phase = tk.Label(frame, text="Phase: Bereit", font=("Arial", 14))
        self.label_phase.pack(pady=5)

        # Countdown
        self.label_countdown = tk.Label(frame, text="00:10", font=("Arial", 24))
        self.label_countdown.pack(pady=5)

        # Buttons
        button_frame = tk.Frame(frame)
        button_frame.pack(pady=5)

        self.button_start = tk.Button(button_frame, text="Start", width=10, command=self.timer_starten)
        self.button_start.grid(row=0, column=0, padx=5)

        self.button_reset = tk.Button(button_frame, text="Reset", width=10, command=self.timer_zuruecksetzen)
        self.button_reset.grid(row=0, column=1, padx=5)

        # Nachricht-Label
        self.label_nachricht = tk.Label(frame, text="", font=("Arial", 10))
        self.label_nachricht.pack(pady=5)

    def timer_starten(self): # Startet die Lernphase und den Timer
        
        if self.logik.aktuelle_phase == "bereit":
            self.logik.lernphase_starten()
            self.label_nachricht.config(text="Lernphase gestartet.")
        self.timer_laueft = True
        self.anzeige_aktualisieren()
        self.timer_schritt()

    def timer_zuruecksetzen(self): # Stoppt den Timer und setzt alles zurück
        
        self.timer_laueft = False
        self.logik.zuruecksetzen()
        self.label_nachricht.config(text="Zurückgesetzt.")
        self.anzeige_aktualisieren()

    def timer_schritt(self): # Wird jede Sekunde aufgerufen, solange der Timer läuft.
                             # Zählt die Zeit herunter und aktualisiert die Anzeige
        
        if not self.timer_laueft:
            return

        phase_beendet = self.logik.eine_sekunde_vergehen()
        self.anzeige_aktualisieren()

        if phase_beendet:
            self.timer_laueft = False
            self.label_nachricht.config(text="Lernphase beendet.")

        # nächsten Schritt in 1 Sekunde planen
        self.root.after(1000, self.timer_schritt)

    def anzeige_aktualisieren(self): # Aktualisiert Phase-Text und Countdown-Anzeige
        
        phasenname = self.logik.phasenname_holen()
        self.label_phase.config(text=f"Phase: {phasenname}")

        sekunden = self.logik.verbleibende_sekunden
        minuten = sekunden // 60
        rest_sekunden = sekunden % 60
        self.label_countdown.config(text=f"{minuten:02d}:{rest_sekunden:02d}")

# Start des Programms:

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroAnwendung(root)
    root.mainloop()