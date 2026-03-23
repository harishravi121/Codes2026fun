#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

// Set the LCD address to 0x27 for a 16 chars and 2 line display
LiquidCrystal_I2C lcd(0x27, 16, 2);

const int buttonPin = 2;     // Pin where the button is connected
int lastButtonState = HIGH;  // Previous state of the button

// Your list of strings
const char* options[] = {"Left", "Right", "Up", "Down", "Center"};
const int optionsCount = 5;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP); // Use internal pullup resistor
  
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Press Button!");
  
  // Seed the random generator with noise from an empty analog pin
  randomSeed(analogRead(0));
}

void loop() {
  int reading = digitalRead(buttonPin);

  // Check if the button is pressed (goes from HIGH to LOW)
  if (reading == LOW && lastButtonState == HIGH) {
    delay(50); // Simple debounce
    
    // Pick a random index
    int randomIndex = random(0, optionsCount);
    
    // Update the LCD
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Result:");
    lcd.setCursor(0, 1);
    lcd.print(options[randomIndex]);
  }
  
  lastButtonState = reading;
}
