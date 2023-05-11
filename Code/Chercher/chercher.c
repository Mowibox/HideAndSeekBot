#include "fichier.h"
#include <stdbool.h>


void scan(int g, int d){
	for (i = g; i <= d; i += ((d-g)/6) ) {
		if(capteurIR >= intensite_max){
			intensite_max = capteurIR;
			angle_imax = angle_servomoteur;
		}
	}
}


void scan_et_tourne(int g,int d){  //variables pas encore définies ; paramètres : plage de rotation
	scan(int g, int d);
	
	if (angle_imax =! 0 ){  // est la valeur initiale : la vmaleur max n'a pas changée
				tourner_angle_correspondant(angle_imax);
				angle_servomoteur = 0;
	}
}

void petite_danse(){
	arreter_les_roues();
	tour_gauche();
	tour_droite();
}

void tour_gauche(){
	tourner_a_gauche();
	tourner_a_gauche();
	tourner_a_gauche();
	tourner_a_gauche();
}


void tour_droite(){
	tourner_a_droite();
	tourner_a_droite();
	tourner_a_droite();
	tourner_a_droite();
}


void demi_tour(){
	tourner_a_gauche();
	tourner_a_gauche();
}



void chercher(){
	
	// variables locales : à dénifir en #define dans fichier h ?

	float intensite_max ;
	float angle_imax ;
	float valeur_min_IR = ; // à déterminer 
	float valeur_robot_trouve = ; //à déterminer
	bool scan_en_cours = false; 
	bool recherche_infrarouge_enclanchée = false;
	
	while ( capteurIR < valeur_robot_trouve){

		avancer_tout_droit(3); //pendant trois secondes (à voir)
		arreter_les_roues(); // pas necessaire car on n'avance plus mais on sait jamais c'est là
		

		// SCAN IR :

		
		if (capteurIR >= valeur_min_IR AND recherche_infrarouge_enclanchée = false) {
			bool recherche_infrarouge_enclanchee = true;	// inutile dans le code actuel mais je garde l'idée au cas où j'en ai besoin 
			arreter_les_roues();
			arreter_rotation_servomoteur();
			intensite_max = capteurIR ; 					 
			tourner_angle_correspondant(angle_servomoteur);
			reinitialiser_pos_servomoteur(); 				// prendre code sur internet 
			angle_imax = 0;
			scan_et_tourne();

			while ( capteurIR < valeur_robot_trouve){
				avancer_tout_droit(2);					// problème : et si il ne le trouve pas ? // pdt 2 sec
			}

			petite_danse();
			end; // arrêter le programme
		}

		
		
		// Scan US


		if (capteur_US_front == 1 AND capteurIR < valeur_robot_trouve){

			if (capteur_US_droit == 1 AND capteur_US_gauche ==0 ){
				tourner_a_gauche();
				longer_mur(); // ENCORE UN PBBBBBBBBBBBBBBB j'en peux plus : dans longer mur : il doit scanner
			}

			if (capteur_US_gauche ==1 AND capteur_US_droit == 0){
				tourner_a_droite();
				longer_mur(); // ENCORE UN PBBBBBBBBBBBBBBB j'en peux plus : dans longer mur : il doit scanner
			}
		
			if (capteur_US_right ==1 AND capteur_US_ left == 1){
				demi_tour(); 
			}
		}
		

	petite_danse();

	}

}

	