int sensor = A0;
int button = 4;
int touch = A1;
int rotary = A2;

void setup() {
	pinMode(sensor, INPUT);
	pinMode(button, INPUT);
	pinMode(touch, INPUT);
	pinMode(rotary, INPUT);
	Serial.begin(115200);
}

int pastSensorVal = 0;
int pastButtonVal = 0;
int pastTouchVal = 0;
int rotaryTime = 0;
void loop() {
	int sensorVal = analogRead(sensor);
	int buttonVal = digitalRead(button);
	int touchVal = digitalRead(touch);
	int rotaryVal = analogRead(rotary);
	
	int nowTime = millis();
	if (nowTime - rotaryTime > 1000) {
		Serial.print("rot:");
		Serial.println(rotaryVal);
		rotaryTime = nowTime;
	}
	
	if (pastButtonVal != buttonVal) {
		Serial.println("button");
		pastButtonVal = buttonVal;
	}	

	if (abs(sensorVal - pastSensorVal) > 200) {
		Serial.println(sensorVal);
		pastSensorVal = sensorVal;
	}

	if (pastTouchVal != touchVal) {
		Serial.println("touch");
		pastTouchVal = touchVal;
	}
}
