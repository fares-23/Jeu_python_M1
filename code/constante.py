TAILLE_GRILLE = 48*40
TAILLE_CASE = 48
 
#RESOLUTION = (48 * TAILLE_CASE+432 , 40 * TAILLE_CASE + 80 )  # Ajustez la taille de la fenêtre (1200,720)
RESOLUTION = (1200, 720)
RESOLUTION_JEU = (RESOLUTION[0], RESOLUTION[1] +50)

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0) 
VERT = (0, 255, 0) 
BLEU = (0, 0, 255)

COULEUR_GRILLE = (255,255,255,0)
COULEUR_FOND = BLANC  # Définition de la couleur de fond
 
#coordonées initiales des personnages
co_map1 = [[(5*TAILLE_CASE,13*TAILLE_CASE),(5*TAILLE_CASE,14*TAILLE_CASE),(4*TAILLE_CASE,12*TAILLE_CASE),(4*TAILLE_CASE,13*TAILLE_CASE),(4*TAILLE_CASE,11*TAILLE_CASE)],
           [(24*TAILLE_CASE,5*TAILLE_CASE),(20*TAILLE_CASE,5*TAILLE_CASE),(21*TAILLE_CASE,6*TAILLE_CASE),(22*TAILLE_CASE,6*TAILLE_CASE),(22*TAILLE_CASE,5*TAILLE_CASE)]]

co_map2 = [[(1*TAILLE_CASE,4*TAILLE_CASE),(2*TAILLE_CASE,4*TAILLE_CASE),(4*TAILLE_CASE,5*TAILLE_CASE),(2*TAILLE_CASE,5*TAILLE_CASE),(4*TAILLE_CASE,4*TAILLE_CASE)],
           [(23*TAILLE_CASE,8*TAILLE_CASE),(21*TAILLE_CASE,8*TAILLE_CASE),(22*TAILLE_CASE,10*TAILLE_CASE),(24*TAILLE_CASE,10*TAILLE_CASE),(22*TAILLE_CASE,9*TAILLE_CASE)]]

co_map3 = [[(0*TAILLE_CASE,2*TAILLE_CASE),(2*TAILLE_CASE,3*TAILLE_CASE),(1*TAILLE_CASE,1*TAILLE_CASE),(3*TAILLE_CASE,3*TAILLE_CASE),(5*TAILLE_CASE,4*TAILLE_CASE)],
           [(22*TAILLE_CASE,11*TAILLE_CASE),(20*TAILLE_CASE,11*TAILLE_CASE),(18*TAILLE_CASE,13*TAILLE_CASE),(17*TAILLE_CASE,14*TAILLE_CASE),(18*TAILLE_CASE,14*TAILLE_CASE)]]


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

#Statistic des personnages
archer_esquive = 0.3
archer_pv = 10
archer_attaque = 20
archer_defense = 5
archer_vitesse = 10

chevalier_esquive = 0.1
chevalier_pv = 10
chevalier_attaque = 20
chevalier_defense = 8
chevalier_vitesse = 10

mage_esquive = 0.2
mage_pv = 10
mage_attaque = 20
mage_defense = 3
mage_vitesse = 10