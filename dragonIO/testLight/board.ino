int sensor = A0;

void setup() {
	pinMode(sensor, INPUT);
	Serial.begin(9600);
}

int pastSensorVal = 0;
void loop() {
	int sensorVal = analogRead(sensor);
	if (abs(sensorVal - pastSensorVal) > 200) {
		Serial.println(sensorVal);
		pastSensorVal = sensorVal;
	}
}
