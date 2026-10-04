
import customtkinter as ctk

fen = ctk.CTk()

fen.title("Calculatrice")
fen.resizable(False, False)
fen.geometry("360x530+400+100")


def ajouter(valeur):
    label.insert(ctk.END, valeur)


def nettoyer():
    label.delete(0, ctk.END)


def calculer():
    try:
        expression = label.get()
        resultat = eval(expression)

        label.delete(0, ctk.END)
        label.insert(ctk.END, str(resultat))

    except:
        label.delete(0, ctk.END)
        label.insert(ctk.END, "Erreur")


label = ctk.CTkEntry(
    fen,
    justify="right",
    font=("Arial", 20)
)

label.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=(20, 20),
    ipady=10,
    sticky="nsew"
)


boutons = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["0", "00", "000", "/"],
    ["C", "%", ".", "="]
]


for i in range(5):
    for j in range(4):

        valeur = boutons[i][j]

        if valeur == "=":
            but = ctk.CTkButton(
                fen,
                text=valeur,
                font=("Arial", 20),
                fg_color="green",
                text_color="white",
                width=70,
                height=60,
                command=calculer
            )

        elif valeur == "C":
            but = ctk.CTkButton(
                fen,
                text=valeur,
                font=("Arial", 20),
                fg_color="red",
                text_color="white",
                width=70,
                height=60,
                command=nettoyer
            )

        else:
            but = ctk.CTkButton(
                fen,
                text=valeur,
                font=("Arial", 20),
                fg_color="orange",
                text_color="white",
                width=70,
                height=60,
                command=lambda v=valeur: ajouter(v)
            )

        but.grid(
            row=i + 1,
            column=j,
            padx=5,
            pady=5
        )


fen.mainloop()