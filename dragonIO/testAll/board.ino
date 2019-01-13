int light = A0;
int button = 4;
int touch = A1;
int rotary = A2;

typedef struct {
	int A, B, Click;
} Encoder;

void setup() {
	pinMode(light, INPUT);
	pinMode(button, INPUT);
	pinMode(touch, INPUT);
	pinMode(rotary, INPUT);
	Serial.begin(115200);
}

void testEncoder() {
	pinMode(10, INPUT);
	pinMode(11, INPUT);
	pinMode(12, INPUT);

	int v1 = digitalRead(10);
	int v2 = digitalRead(11);
	int v3 = digitalRead(12);

	Serial.print(v1);
	Serial.print(v2);
	Serial.println(v3);

	delay(100);
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

	testEncoder();
	
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
		Serial.print("touch:");
		Serial.println(touchVal);
		pastTouchVal = touchVal;
	}
}
