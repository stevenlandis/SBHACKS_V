int light = A0;
int button = 4;
int touch = A1;
int rotary = A2;

typedef struct {
	int A, B, Click;
} Encoder;
int encoderState = 0;

Encoder encoder = {11, 12, 10};

int cnt = 0;

void updateEncoderState(int a, int b) {
	switch(encoderState) {
	case 0:
		if (!a && b) {
			encoderState = 1;
			return;
		} else if (a && !b) {
			encoderState = 4;
			return;
		}
		break;
	case 1:
		if (!a && !b) {
			encoderState = 2;
			return;
		}
		break;
	case 2:
		if (a && !b) {
			encoderState = 3;
			return;
		}
		break;
	case 3:
		if (a && b) {
			encoderState = 0;
			Serial.println("encoder:0");
			return;
		}
		break;
	case 4:
		if (!a && !b) {
			encoderState = 5;
			return;
		}
		break;
	case 5:
		if (!a && b) {
			encoderState = 6;
			return;
		}
		break;
	case 6:
		if (a && b) {
			encoderState = 0;
			Serial.println("encoder:1");
			return;
		}
		break;
	}
	// if control flow reaches here, reset to 0
	encoderState = 0;
}

void setup() {
	pinMode(light, INPUT);
	pinMode(button, INPUT);
	pinMode(touch, INPUT);
	pinMode(rotary, INPUT);
	pinMode(encoder.A, INPUT);
	pinMode(encoder.B, INPUT);
	pinMode(encoder.Click, INPUT);
	Serial.begin(115200);
}

void testEncoder() {
	int v1 = digitalRead(10);
	int v2 = digitalRead(11);
	int v3 = digitalRead(12);

	Serial.print(v1);
	Serial.print(v2);
	Serial.println(v3);

	delay(100);
}

int pastLightVal = 10000;
int pastButtonVal = 0;
int pastTouchVal = 0;
int rotaryTime = -10000;
int pastRotaryVal = 10000;
Encoder pastEncoder = {1,1,1};
void loop() {
	int lightVal = analogRead(light);
	int buttonVal = digitalRead(button);
	int touchVal = digitalRead(touch);
	int rotaryVal = analogRead(rotary);
	Encoder encoderVal = {
		digitalRead(encoder.A),
		digitalRead(encoder.B),
		digitalRead(encoder.Click)
	};

	if (pastEncoder.Click != encoderVal.Click) {
		Serial.print("click:");
		Serial.println(!encoderVal.Click);
		pastEncoder.Click = encoderVal.Click;
	}

	if (pastEncoder.A != encoderVal.A || pastEncoder.B != encoderVal.B) {
		updateEncoderState(encoderVal.A, encoderVal.B);
		pastEncoder.A = encoderVal.A;
		pastEncoder.B = encoderVal.B;
	}
	
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
		//Serial.println(cnt);
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
