/*
Code by Dr. Harish with LCD shield to display random sentances and revise math!
Can be used in schools and homes! Costs 1000 re to make and can be sold @ 1250 with profit or hobbyists can make it..
Can add school or home name in sentances which come up..

Auto problems display in scientific calculators based on a button like this code would be a great sale including integrands exponents etc.
*/
// include the library code:
#include <LiquidCrystal.h>

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 8, en = 9, d4 = 4, d5 = 5, d6 = 6, d7 = 7;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  
  lcd.setCursor(0, 0);
  lcd.print("Measuring c/10^8 in m/s  ");}
  lcd.setCursor(1,0);
  // Print a message to the LCD.
  randomSeed(analogRead(0));
}

void loop() {
   float c;
   L=10km;
  Loopnumberaim=10000;
  ontime=1; //ms
  timedelay=L*Loopnumberaim/c*1000;



  digitalwrite(LEDpin,HIGH);
  delay(ontime);
  digitalwrite(LEDpin,LOW);
  delay(timedelay);
  digitalwrite(GAPDpin,HIGH);
  delay(1);
  if(GAPDsignal==1){
  c=L*Loopnumberaim/1000/timedelay
  lcd.Print(c)
    }



}
  
  
}
