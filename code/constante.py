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

#image_path
archer_path = "assets/tiles/dungeon_crawl/monster/deep_elf_master_archer.png"
chevalier_path = "assets/tiles/dungeon_crawl/monster/deep_elf_knight_new.png"
mage_path = "assets/tiles/dungeon_crawl/monster/deep_elf_mage.png"
