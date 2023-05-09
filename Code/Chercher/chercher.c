#include "fichier.h"
#include <stdbool.h>

vovoid chercher(){
	
	float intensite_max ;
	float angle_imax ;
	float valeur_min_IR = ; / à déterminer 
	float valeur_robot_trouve = ; /à déterminer
	bool scan_en_cours = false;  /marhce toujours pas?
	int direction; 
	
	while ( capteurIR < valeur_robot_trouve){
		
		if (capteurIR >= valeur_min_IR){   
			arreter_les_roues();
			intensite_max = capteurIR ; 		
			angle_imax = angle_servomoteur;	/?		 
			tourner_angle_correspondant(angle_servomoteur);
			angle_servomoteur = 0; 				/on réinitialise la position  , prendre code sur internet 


			// deux prochains blocs à mettre dans une fonction scan_et_tourner()
			
			bool scan_en_cours = 1; 
			while (scan_en_cours == 1 ){
				scan(); /mettre en paramètre droite ou gauche (de 0 à 90 ou -90 à 0) fonction à deux paramètres
					if(capteurIR >= intensite_max){ / ça marche tjrs pas en fait, faudrait avoir un while scan???
						intensité_max = capteurIR;
						angle_imax = angle_servomoteur;
					}
				}
		
			if (angle_imax =! 0 ){  / est la valeur initiale : la vmaleur max n'a pas changée
				tourner_angle_correspondant(angle_imax);
				angle_servomoteur = 0;
			
					//elif ?? EN DEHORS DE SCAN ET TOURNE : que fais t il sinon ? avancer tout droit
		
		/continuer à avancer et à trouver le max jusqu'à trouver capteurIR = valeur robot trouvée
		// à faire
	
	
		if (capteur_US_front == 1){
			arreter_les_roues();
			scan_et_tourne(-90, 90); / fait un tour de 180°
			if (angle_imax ==0){
				demi_tour(); / pas forcément, voir si à droite ou à gauche on capte un truc)
			}
		
		if (capteur_US_right ==1 OR capteur_US_ left == 1){
			direction(); /retourne la direction droite ou gauche (0 gauche et 1 droite)
			longer_mur(direction); 
		}
	petite_danse();
}

	