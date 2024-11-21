import tkinter as tk
import random

# Définition des constantes
TAILLE_CELLULE = 40
NB_LIGNES = 20
NB_COLONNES = 30
longueur = NB_COLONNES * TAILLE_CELLULE
hauteur = NB_LIGNES * TAILLE_CELLULE

VIDE = 0
SNAKE = 1
POMME = 2

couleur_snake = "green"

# Classe Snake pour représenter le serpent
class Snake:
    def __init__(self, grille, i, j):
        # Initialisation de la direction du serpent et de son corps
        self.direction = (0, 1)  # Direction initiale : droite
        self.direction_cible = self.direction
        self.corps = [(i, j), (i, j - 1), (i, j - 2)]
        self.grille = grille

    def changer_direction(self, event):
        # Méthode pour changer la direction du serpent en réponse aux touches fléchées
        if event.keysym == "Up" and self.direction != (1, 0):
            self.direction_cible = (-1, 0)
        elif event.keysym == "Down" and self.direction != (-1, 0):
            self.direction_cible = (1, 0)
        elif event.keysym == "Left" and self.direction != (0, 1):
            self.direction_cible = (0, -1)
        elif event.keysym == "Right" and self.direction != (0, -1):
            self.direction_cible = (0, 1)

    def acquerir_cible(self):
        # Méthode pour obtenir la prochaine position cible du serpent en fonction de sa direction
        i_tete, j_tete = self.corps[0]
        di, dj = self.direction_cible
        i_cible = (i_tete + di) % NB_LIGNES
        j_cible = (j_tete + dj) % NB_COLONNES
        return i_cible, j_cible

    def deplacer(self, i_tete, j_tete):
        # Méthode pour déplacer le serpent
        self.direction = self.direction_cible
        self.corps.insert(0, (i_tete, j_tete))
        i_queue, j_queue = self.corps.pop()
        self.grille[i_queue][j_queue] = VIDE

        for i, j in self.corps:
            self.grille[i][j] = SNAKE

    def manger(self, i_tete, j_tete):
        # Méthode pour traiter le cas où le serpent mange une pomme
        self.direction = self.direction_cible
        self.corps.insert(0, (i_tete, j_tete))
        self.grille[i_tete][j_tete] = SNAKE

# Fonction pour générer une pomme aléatoirement dans la grille
def generer_pomme(grille):
    i, j = random.randint(0, NB_LIGNES - 1), random.randint(0, NB_COLONNES - 1)
    while grille[i][j] != VIDE:
        i, j = random.randint(0, NB_LIGNES - 1), random.randint(0, NB_COLONNES - 1)
    grille[i][j] = POMME


# Fonction représentant un tour de jeu
def tour_de_jeu():
    i_tete, j_tete = snake.acquerir_cible()

    if grille[i_tete][j_tete] == SNAKE:
        game_over()
        return
    elif grille[i_tete][j_tete] == POMME:
        snake.manger(i_tete, j_tete)
        generer_pomme(grille)
    else:
        snake.deplacer(i_tete, j_tete)

    dessiner_grille()
    fenetre.after(50, tour_de_jeu)

# Fonction pour fermer la fenetre
def quitter():
    fenetre.destroy()

# Fonction appelée en cas de fin de jeu
def game_over():
    # Création de la variable pour stocker la couleur choisie
    couleur_choisie = tk.StringVar()

    # Set la couleur du serpent comme la première option
    couleur_choisie.set(couleur_snake)

    canvas.create_text(
        (NB_COLONNES * TAILLE_CELLULE) // 2,
        (NB_LIGNES * TAILLE_CELLULE) // 2,
        text="Game Over",
        font=("Helvetica", 24),
        fill="white"
    )

    score = len(snake.corps) - 3
    canvas.create_text(
        (NB_COLONNES * TAILLE_CELLULE) // 2,
        (NB_LIGNES * TAILLE_CELLULE) // 2 + 40,
        text=f"Score : {score}",
        font=("Helvetica", 16),
        fill="white"
    )

    # Menu déroulant avec les couleurs disponibles
    menu_couleur = tk.OptionMenu(fenetre, couleur_choisie, "green", "red", "yellow", "purple", "white", "orange", "brown")
    canvas.create_window(
        (NB_COLONNES * TAILLE_CELLULE) // 2,
        (NB_LIGNES * TAILLE_CELLULE) // 2 + 80,
        window=menu_couleur
    )

    # Bouton Rejouer
    bouton_rejouer = tk.Button(fenetre, text="Rejouer", command=lambda: rejouer(couleur_choisie.get()))
    canvas.create_window(
        (NB_COLONNES * TAILLE_CELLULE) // 2,
        (NB_LIGNES * TAILLE_CELLULE) // 2 + 120,
        window=bouton_rejouer
    )

    # Bouton Quitter
    bouton_quitter = tk.Button(fenetre, text="Quitter", command=quitter)
    canvas.create_window(
        (NB_COLONNES * TAILLE_CELLULE) // 2,
        (NB_LIGNES * TAILLE_CELLULE) // 2 + 160,
        window=bouton_quitter
    )

    canvas.create_text(
        (NB_COLONNES * TAILLE_CELLULE) // 2,
        (NB_LIGNES * TAILLE_CELLULE) // 2 + 380,
        text="© 2024 - ROTAR Daniel & MERLEN Thomas",
        font=("Helvetica", 16),
        fill="white",
    )


def debut_du_jeu():
    # Création de la variable pour stocker la couleur choisie
    couleur_choisie = tk.StringVar()
    couleur_choisie.set("green")  # Couleur par défaut

    canvas.create_text(
        (NB_COLONNES * TAILLE_CELLULE) // 2,
        (NB_LIGNES * TAILLE_CELLULE) // 2,
        text="Bienvenue dans le Snake !",
        font=("Helvetica", 24),
        fill="white"
    )

    # Menu déroulant avec les couleurs disponibles
    menu_couleur = tk.OptionMenu(fenetre, couleur_choisie, "green", "red", "yellow", "purple", "white", "orange", "brown")
    canvas.create_window(
        (NB_COLONNES * TAILLE_CELLULE) // 2,
        (NB_LIGNES * TAILLE_CELLULE) // 2 + 40,
        window=menu_couleur
    )

    # Bouton Démarrer
    bouton_demarrer = tk.Button(fenetre, text="Démarrer", command=lambda: lancer_partie(couleur_choisie.get()))
    canvas.create_window(
        (NB_COLONNES * TAILLE_CELLULE) // 2,
        (NB_LIGNES * TAILLE_CELLULE) // 2 + 80,
        window=bouton_demarrer
    )

    canvas.create_text(
        (NB_COLONNES * TAILLE_CELLULE) // 2,
        (NB_LIGNES * TAILLE_CELLULE) // 2 + 380,
        text="© 2024 - ROTAR Daniel & MERLEN Thomas",
        font=("Helvetica", 16),
        fill="white",
    )

def lancer_partie(couleur):
    global grille, snake, couleur_snake
    couleur_snake = couleur  # Mettre à jour la variable globale
    grille = [[VIDE] * NB_COLONNES for k in range(NB_LIGNES)]
    snake = Snake(grille, NB_LIGNES // 2, NB_COLONNES // 2)
    generer_pomme(grille)
    canvas.delete("all")
    dessiner_grille()

    # Réactivation des liaisons clavier
    fenetre.bind("<Up>", snake.changer_direction)
    fenetre.bind("<Down>", snake.changer_direction)
    fenetre.bind("<Left>", snake.changer_direction)
    fenetre.bind("<Right>", snake.changer_direction)

    fenetre.after(50, tour_de_jeu)

# Fonction pour que l'user recommence une partie
def rejouer(couleur):
    global grille, snake, couleur_snake
    couleur_snake = couleur  # Mettre à jour la variable globale
    grille = [[VIDE] * NB_COLONNES for k in range(NB_LIGNES)]
    snake = Snake(grille, NB_LIGNES // 2, NB_COLONNES // 2)
    generer_pomme(grille)
    canvas.delete("all")
    dessiner_grille()

    # Réactivation des liaisons clavier
    fenetre.bind("<Up>", snake.changer_direction)
    fenetre.bind("<Down>", snake.changer_direction)
    fenetre.bind("<Left>", snake.changer_direction)
    fenetre.bind("<Right>", snake.changer_direction)

    fenetre.after(50, tour_de_jeu)

def dessiner_grille():
    global couleur_snake
    canvas.delete("all")

    for i in range(NB_LIGNES):
        for j in range(NB_COLONNES):
            x1, y1 = j * TAILLE_CELLULE, i * TAILLE_CELLULE
            x2, y2 = x1 + TAILLE_CELLULE, y1 + TAILLE_CELLULE

            if grille[i][j] == SNAKE:
                canvas.create_rectangle(x1, y1, x2, y2, fill=f"{couleur_snake}")
            elif grille[i][j] == POMME:
                canvas.create_oval(x1, y1, x2, y2, fill="red")

    # Affichage du score en haut à droite
    score = len(snake.corps) - 3
    canvas.create_text(
        (NB_COLONNES * TAILLE_CELLULE) - 10, 10,
        text=f"Score: {score}",
        anchor=tk.NE,  # Ancre le texte dans le coin supérieur droit
        font=("Helvetica", 12),
        fill="white"
    )

# Initialisation de la fenêtre tkinter
fenetre = tk.Tk()
fenetre.configure(bg="black")
fenetre.geometry(f"{longueur}x{hauteur}")
fenetre.resizable(0, 0)

# Initialisation de la grille du jeu
grille = [[VIDE] * NB_COLONNES for k in range(NB_LIGNES)]

# Initialisation du serpent
snake = Snake(grille, NB_LIGNES // 2, NB_COLONNES // 2)

# Initialisation de la pomme
generer_pomme(grille)

# Création du canevas pour afficher le jeu
canvas = tk.Canvas(fenetre, width=NB_COLONNES * TAILLE_CELLULE, height=NB_LIGNES * TAILLE_CELLULE, bg="black")
canvas.pack()

# Liaison des événements clavier aux méthodes du serpent
fenetre.bind("<Up>", snake.changer_direction)
fenetre.bind("<Down>", snake.changer_direction)
fenetre.bind("<Left>", snake.changer_direction)
fenetre.bind("<Right>", snake.changer_direction)
fenetre.bind("<Escape>", lambda event: quitter())

# Appel à debut_du_jeu pour afficher l'écran d'accueil au démarrage
debut_du_jeu()

# Affichage de la fenêtre
fenetre.title("Snake par ROTAR Daniel et MERLEN Thomas")
fenetre.mainloop()