#define echoPin 2 // Pin Echo de HC-SR04
#define trigPin 3 // Pin Trig de HC-SR04

void setup() {
  Serial.begin(9600); // Initialisation de la communication série
  pinMode(trigPin, OUTPUT); // Définition de la pin Trig comme une sortie
  pinMode(echoPin, INPUT); // Définition de la pin Echo comme une entrée
}

void loop() {
  digitalWrite(trigPin, LOW); // On met la pin Trig à LOW pendant 2 microsecondes
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH); // On met la pin Trig à HIGH pendant 10 microsecondes
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH); // On mesure la durée du signal Echo HIGH
  float distance = duration * 0.034 / 2; // On calcule la distance en cm
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  delay(1000); // On attend 1 seconde avant de mesurer à nouveau la distance
}
