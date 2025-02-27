# Illia
import json
import random
import tkinter as tk
from tkinter import messagebox

def wczytaj_pytania(plik="pytania.json"):
    with open(plik, "r", encoding="utf-8") as f:
        return json.load(f)

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Wiedzy")
        
        self.imie = None
        self.pytania = wczytaj_pytania()
        random.shuffle(self.pytania)
        
        self.indeks_pytania = 0
        self.punkty = 0
        
        self.wprowadzenie_imienia()
    
    def wprowadzenie_imienia(self):
        self.okno_imienia = tk.Toplevel(self.root)
        self.okno_imienia.title("Wprowadź swoje imię")
        
        self.label_imie = tk.Label(self.okno_imienia, text="Podaj swoje imię:", font=("Arial", 12))
        self.label_imie.pack(pady=10)

        self.entry_imie = tk.Entry(self.okno_imienia, font=("Arial", 12))
        self.entry_imie.pack(pady=10)

        self.btn_zatwierdz = tk.Button(self.okno_imienia, text="Zatwierdź", command=self.zatwierdz_imie, font=("Arial", 12))
        self.btn_zatwierdz.pack(pady=10)
    
    def zatwierdz_imie(self):
        self.imie = self.entry_imie.get()
        self.okno_imienia.destroy()
        self.tworz_gui()
        self.wyswietl_pytanie()
    
    def tworz_gui(self):
        self.label_pytanie = tk.Label(self.root, text="", font=("Arial", 14), wraplength=400)
        self.label_pytanie.pack(pady=10)

        self.var_odpowiedz = tk.StringVar()
        self.var_odpowiedz.set(None)

        self.przyciski_odp = []
        for litera in ["A", "B", "C", "D"]:
            btn = tk.Radiobutton(self.root, text="", variable=self.var_odpowiedz, value=litera, font=("Arial", 12))
            btn.pack(anchor="w", padx=20)
            self.przyciski_odp.append(btn)

        self.btn_potwierdz = tk.Button(self.root, text="Potwierdź", command=self.sprawdz_odpowiedz, font=("Arial", 12))
        self.btn_potwierdz.pack(pady=10)
    
    def wyswietl_pytanie(self):
        if self.indeks_pytania < len(self.pytania):
            pytanie = self.pytania[self.indeks_pytania]
            self.label_pytanie.config(text=f"Kategoria: {pytanie['kategoria']}\n{pytanie['pytanie']}")
            
            for i, litera in enumerate(["A", "B", "C", "D"]):
                self.przyciski_odp[i].config(text=f"{litera}: {pytanie['odpowiedzi'][litera]}")
        else:
            self.koniec_quizu()
    
    def sprawdz_odpowiedz(self):
        if not self.var_odpowiedz.get():
            messagebox.showwarning("Błąd", "Wybierz odpowiedź!")
            return
        
        poprawna = self.pytania[self.indeks_pytania]["poprawna_odpowiedz"]
        
        if self.var_odpowiedz.get() == poprawna:
            self.punkty += 1
            messagebox.showinfo("Wynik", "✔️ Brawo! Poprawna odpowiedź!")
        else:
            messagebox.showerror("Wynik", f"❌ Błędna odpowiedź! Poprawna: {poprawna}")
        
        self.indeks_pytania += 1
        self.var_odpowiedz.set(None)
        self.wyswietl_pytanie()
    
    def koniec_quizu(self):
        messagebox.showinfo("Koniec quizu", f"{self.imie}, Twój wynik: {self.punkty}/{len(self.pytania)}")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
