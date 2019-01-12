int button_pin = A0;

void setup() {
    pinMode(button_pin, INPUT);
	Serial.begin(9600);
}

bool last_button = false;
int count = 0;
void loop() {
	bool button = digitalRead(button_pin);
	if (last_button != button) {
		Serial.print(count++);
		Serial.println(" pressed");
		last_button = button;
	}
}
