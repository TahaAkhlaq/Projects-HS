// Define The Pins Used
const int trigPin = 9;
const int echoPin = 10;
const int buzzer = 11;
const int ledPin = 13;

// Define Variables 
long time;
int distance;
int safetyDistance;

//Setup
void setup() {
pinMode(trigPin, OUTPUT); // The trigPin is an Output
pinMode(echoPin, INPUT); // The echoPin is an Input
pinMode(buzzer, OUTPUT); // The buzzer is as an Output
pinMode(ledPin, OUTPUT); // The ledPin is an Output
Serial.begin(9600); // Starts the serial monitor
}


void loop() {
digitalWrite(trigPin, LOW); // trigPin is not activated
delayMicroseconds(2); // Add a delay


digitalWrite(trigPin, HIGH); // trigPin is activated
delayMicroseconds(10); //For 10 seconds
digitalWrite(trigPin, LOW); //trigPin is not activated


time = pulseIn(echoPin, HIGH); //The sound wave travels to the object and back in microseconds


distance= time*0.034/2; // Calculates the distance

safetyDistance = distance; 
if (safetyDistance <= 5){
  digitalWrite(buzzer, HIGH); //The buzzer is activated
  digitalWrite(ledPin, HIGH); //The LED light is activated
}
else{
  digitalWrite(buzzer, LOW); //The buzzer is not activated if the distance is greater than 5
  digitalWrite(ledPin, LOW); //The LED Light is not activated if the distance is greater than 5
}

// The distance is displayed on the Serial Monitor 
Serial.print("Distance: ");
Serial.println(distance);
}