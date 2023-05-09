#include "hide.h"
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

//variables associées aux composants
int frontCaptor = 0; // distance en cm
int leftCaptor = 0; // idem
int rightCaptor = 0; // idem
bool leftWheel = 0; // 0 = roule pas, 1 = roule
bool rightWheel = 0; // idem

//variable de l'algo
srand(time(NULL)); // Initialisation de la donnée seed pour la valeur aleatoire du nombre de mur rencontré (je comprend pas les erreurs, j'ai recopié un exemple de code pour les chiffres aléatoires d'internet)
const int nbrWallExpected = rand()%5;
int nbrWall = 0;
const int dirWall = rand()%2;
int nbrTurned = 0;
bool isSeekingWall = false;
bool isSeekingPos = false;
bool isHidden = false;



void Rotate(int angle) {
	if (angle > 0) {
		//temps de rotation des roues à determiner en fonction de l'angle
		leftWheel = 1;
		rightWheel = -1;
	}
	if (angle < 0) {
		//temps de rotation des roues à determiner en fonction de l'angle
		leftWheel = -1;
		rightWheel = 1;
	}
	 
}

void TurnAngle(int dir) { //fonction pour faire tourner le robot autour d'un angle d'un mur
	if (dir == 1) {
		Rotate(45);
		MoveForward(1);
		if (rightCaptor > 10) {
			Rotate(45);
		}
	}
	else {
		Rotate(-45);
		MoveForward(1);
		if (leftCaptor > 10) {
			Rotate(-45);
		}


	}
}
void GetCloser(int dir) {

}

void RollAway(int dir) {

}

void MoveForward(float time) {
	//durant time secondes :
	leftWheel = 1;
	rightWheel = 1;
	// on arrete ensuite les roues apres time secondes
	leftWheel = 0;
	rightWheel = 0;
}

void SeekAnotherWall() {
	Turn(rand(360));
	while (isSeekingWall = true) {
		moveForward(1);
		if (frontCaptor < 5) {
			isSeekingWall = false;
		}
	}


	
}

void Hiding() {


	while (isHidden == false) {
		while (nbrWall =! nbrWallExpected) { //cherche le mur
			
			if (frontCaptor < 5){
				nbrWall += 1;
				Turn(rand()%360);
			}
		}
		if (dirWall == 1) { Rotate(-45); }
		else { TurnRight(45); }
		isSeekingPos = true;
		while (isSeekingPos == true) {
			if (dirWall == 1){
				if (rightCaptor > 10 && nbrTurned =! 4){
					TurnAngle(dirWall);
					nbrTurned += 1;
				}
				else {
					SeekAnotherWall();
				}
				if (rightCaptor > 5) {
					GetCloser(dirWall);
				}
				else if (rightCaptor < 3) {
					RollAway(dirWall);
				}
				else {
					MoveForward(1);
				}
			}
			if (dirWall == 0) {
				if (leftCaptor > 10 && nbrTurned =! 4) {
					TurnAngle(dirWall);
					nbrTurned = nbrTurned + 1;
				}
				else {
					SeekAnotherWall();
				}
				if (leftCaptor > 5) {
					GetCloser(dirWall);
				}
				else if (leftCaptor < 3) {
					RollAway(dirWall);
				}
				else {
					MoveForward(1);
				}
				
			}
			if (frontCaptor < 3) {
				isSeekingPos = 0;
				isHidden = 1;
			}
		}
	}
}
