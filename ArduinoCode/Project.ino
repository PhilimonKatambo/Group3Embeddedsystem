#include <SPI.h>
#include <MFRC522.h>
#include <EEPROM.h>
#include <Servo.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#define SS_PIN 10
#define RST_PIN 7

LiquidCrystal_I2C lcd(0x27,16,2);

int room1 = 2;
int room2 = 3;
int room3 = 4;
int buzzerPin=9;
int greenLED=8;
int redLED=6;

int servoPin=5;
Servo myServo;
int servoPos=90;


String mode="Entry";

MFRC522 rfid(SS_PIN,RST_PIN);
MFRC522:: MIFARE_Key key;

void setup() {

  pinMode(9,OUTPUT);
  pinMode(room1,INPUT_PULLUP);
  pinMode(room2,INPUT_PULLUP);
  pinMode(room3,INPUT_PULLUP);
  pinMode(buzzerPin,OUTPUT);
  pinMode(greenLED,OUTPUT);
  pinMode(redLED,OUTPUT);

  myServo.attach(servoPin);

  Serial.begin(9600);
  SPI.begin();
  rfid.PCD_Init();
  Serial.println("RFID reader Initialized.");

  lcd.init();
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Door closed");
}

void loop() {

  int room1State=digitalRead(room1);
  int room2State=digitalRead(room2);
  int room3State=digitalRead(room3);

    if(Serial.available()){
    String received = Serial.readStringUntil('\n');
    if(received == "1"){
      Buzzing(1,servoPos,greenLED);
    }
    else if(received == "2"){
      Buzzing(2,servoPos,redLED);
    }
    else if(received == "Entry"){
      mode="Entry";
    }else if(received == "Registry"){
      mode="Registry";
    }
  }

  if(! rfid.PICC_IsNewCardPresent()){
    return;
  }

  if(! rfid.PICC_ReadCardSerial()){
    return;
  }


  MFRC522::PICC_Type piccType=rfid.PICC_GetType(rfid.uid.sak);

  if(mode=="Registry"){
    printHex(rfid.uid.uidByte, rfid.uid.size);
    Serial.println("");

    rfid.PICC_HaltA();
  }
  else if(mode=="Entry"){
    printHex2(rfid.uid.uidByte, rfid.uid.size, room1State, room2State, room3State);
    Serial.println("");

    rfid.PICC_HaltA();
  }

}

void printHex(byte *buffer, byte bufferSize){
  for (byte i=0; i<bufferSize; i++){
    Serial.print(buffer[i] < 0x10 ? " 0" : " ");
    Serial.print(buffer[i],HEX);
  }
}

void printHex2(byte *buffer, byte bufferSize, int room1State, int room2State, int room3State){
  if(room1State==LOW){
    for (byte i=0; i<bufferSize; i++){
      Serial.print(buffer[i] < 0x10 ? " 0" : " ");
      Serial.print(buffer[i],HEX);
    }

    Serial.print(" 1");
  }else if(room2State==LOW){
    for (byte i=0; i<bufferSize; i++){
      Serial.print(buffer[i] < 0x10 ? " 0" : " ");
      Serial.print(buffer[i],HEX);
    }

    Serial.print(" 2");
  }else if(room3State==LOW){
    for (byte i=0; i<bufferSize; i++){
      Serial.print(buffer[i] < 0x10 ? " 0" : " ");
      Serial.print(buffer[i],HEX);
    }

    Serial.print(" 3");
  }
}

void Buzzing(int buzz,int servoPos,int LED1){
  int delayTime1=1000;
  int delayTime2=100;
  
  if(buzz==1){
    myServo.write(160);
    lcd.clear();
    lcd.print("Door Open");
    digitalWrite(LED1,HIGH);
    digitalWrite(buzzerPin,HIGH);
    delay(delayTime1);
    digitalWrite(buzzerPin,LOW);
    delay(5000);

    lcd.clear();
    lcd.print("Door closed");
    myServo.write(90);
    digitalWrite(LED1,LOW);
  }
  else{
    lcd.clear();
    lcd.print("Invalid Card");
    lcd.setCursor(0, 1);
    lcd.print("Or Face");
    for(int i=1; i<=10; i++){
      digitalWrite(LED1,HIGH);
      digitalWrite(buzzerPin,HIGH);
      delay(delayTime2);
      digitalWrite(LED1,LOW);
      digitalWrite(buzzerPin,LOW);
      delay(delayTime2);
    }
    lcd.clear();
    lcd.print("Door closed");
  }
}


