TAILLE_GRILLE = 48*40
TAILLE_CASE = 48
 
#RESOLUTION = (48 * TAILLE_CASE+432 , 40 * TAILLE_CASE + 80 )  # Ajustez la taille de la fenêtre (1200,720)
RESOLUTION = (1200, 720)
RESOLUTION_JEU = (RESOLUTION[0], RESOLUTION[1] +50)

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0) #chevalier
VERT = (0, 255, 0) #archer
BLEU = (0, 0, 255) #mage


COULEUR_GRILLE = (255,255,255,0)
COULEUR_FOND = BLANC  # Définition de la couleur de fond
 


coordonnee_start = [[(3*TAILLE_CASE,3*TAILLE_CASE),(4*TAILLE_CASE,4*TAILLE_CASE),(5*TAILLE_CASE,5*TAILLE_CASE),(5*TAILLE_CASE,6*TAILLE_CASE),(6*TAILLE_CASE,5*TAILLE_CASE)],
                    [(10*TAILLE_CASE,10*TAILLE_CASE),(13*TAILLE_CASE,10*TAILLE_CASE),(12*TAILLE_CASE,10*TAILLE_CASE),(15*TAILLE_CASE,11*TAILLE_CASE),(12*TAILLE_CASE,13*TAILLE_CASE)]]

#nombre de troupe
nb_troupe = 5

archer_b_path = "assets/unites/archer_b.png"
archer_r_path = "assets/unites/archer_r.png"
archer_j_path = "assets/unites/archer_j.png"

chevalier_b_path = "assets/unites/chevalier_b.png"
chevalier_r_path = "assets/unites/chevalier_r.png"
chevalier_j_path = "assets/unites/chevalier_j.png"

mage_b_path = "assets/unites/mage_b.png"
mage_r_path = "assets/unites/mage_r.png"
mage_j_path = "assets/unites/mage_j.png"
