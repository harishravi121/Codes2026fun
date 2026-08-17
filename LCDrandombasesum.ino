  /*
  Code by Dr. Harish with LCD shield 
  */
  
  // include the library code:
  #include <LiquidCrystal.h>
  #include<stdio.h>
  #include<stdlib.h>
  #include<string.h>
  // initialize the library by associating any needed LCD interface pin
  // with the arduino pin number it is connected to
  const int rs = 8, en = 9, d4 = 4, d5 = 5, d6 = 6, d7 = 7;
  LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
  char MF=127;
  char hhh[20];
  int base=7;
  void setup() {
    // set up the LCD's number of columns and rows:
    lcd.begin(16, 2);
    // Print a message to the LCD.
    randomSeed(analogRead(0));
  }
  
  void loop() {
    // set the cursor to column 0, line 1
    // (note: line 1 is the second row, since counting begins with 0):
    lcd.setCursor(0, 0);
     base=random(5)+2;
    lcd.print(base);
    lcd.print("base ");
    
    int b;
    int c;
    int d;
   
    b=int(random(23));
    c=int(random(42));
    d=b+c;
    
        lcd.print(itoa(b,hhh,base));
      lcd.print(" + ");
      lcd.print(itoa(c,hhh,base));
      lcd.setCursor(0, 1);
      
        lcd.print(" = ");
        lcd.print(itoa(d,hhh,base));
        lcd.print("    ");
        delay(4000);
        lcd.clear();
      
  }
