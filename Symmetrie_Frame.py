import tkinter as tk

class Symmetrie_Frame(tk.Frame):

    __funktion = None

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.NSEW)
        self.update()

    def update(self, neu_funktion = None):
        if neu_funktion is not None:
            self.__funktion = neu_funktion
        self.createWidgets()

    def createWidgets(self):
        for widget in self.winfo_children():
            widget.destroy()

        if self.__funktion != None:
            tk.Label(self, text="Symmetrie comming soon..."+self.__funktion.funktion_user_kurz).grid(row=0,column=0)
        else:
            tk.Label(self, text="Für Symmetrieerkennung Funktion oben eingeben").grid(row=0, column=0)