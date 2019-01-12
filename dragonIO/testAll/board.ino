int light = A0;
int button = 4;
int touch = A1;
int rotary = A2;

void setup() {
	pinMode(light, INPUT);
	pinMode(button, INPUT);
	pinMode(touch, INPUT);
	pinMode(rotary, INPUT);
	Serial.begin(115200);
}

int pastLightVal = 0;
int pastButtonVal = 0;
int pastTouchVal = 0;
int rotaryTime = 0;
int pastRotaryVal = 0;
void loop() {
	int lightVal = analogRead(light);
	int buttonVal = digitalRead(button);
	int touchVal = digitalRead(touch);
	int rotaryVal = analogRead(rotary);
	
	int nowTime = millis();
	if (nowTime - rotaryTime > 1000) {
		if (abs(rotaryVal - pastRotaryVal) > 5) {
			Serial.print("rot:");
			Serial.println(rotaryVal);
			pastRotaryVal = rotaryVal;
		}
		rotaryTime = nowTime;
	}
	
	if (pastButtonVal != buttonVal) {
		Serial.print("button:");
		Serial.println(buttonVal);
		pastButtonVal = buttonVal;
	}	

	if (abs(lightVal - pastLightVal) > 200) {
		Serial.print("light:");
		Serial.println(lightVal);
		pastLightVal = lightVal;
	}

	if (pastTouchVal != touchVal) {
		Serial.println("touch");
		pastTouchVal = touchVal;
	}
}
