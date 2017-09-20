#include <SPI.h>
#include <MFRC522.h> 
//Pinos Reset e SS módulo MFRC522
#define SS_PIN 10
#define RST_PIN 9

//Dois leds
#define LG_PIN 7
#define LR_PIN 6

MFRC522 mfrc522(SS_PIN, RST_PIN);

Boolean resposta = false;

void setup(){
	Serial.begin(9600);
	SPI.begin();
	mfrc522.PCD_Init();

	pinMode(LG_PIN, OUTPUT);
	pinMode(LR_PIN, OUTPUT);
}

void loop(){
	// Look for new cards
  if ( ! mfrc522.PICC_IsNewCardPresent()) { return; }
  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) { return; }
  //Escreve UID na serial
  String conteudo= "";
  byte letra;
  for (byte i = 0; i < mfrc522.uid.size; i++) {
     Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
     Serial.print(mfrc522.uid.uidByte[i], HEX);
     conteudo.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     conteudo.concat(String(mfrc522.uid.uidByte[i], HEX));
  }

  //TODO

  conteudo.toUpperCase();
  if (conteudo.substring(1) == "AD 9B 06 7D" 
  || conteudo.substring(1) == "BC 9B 06 7D"
  || conteudo.substring(1) == "EE 9B 06 7D"
  || conteudo.substring(1) == "9D 9B 06 7D") {
  // uid ja pré-definido comparado com o lido na ocasião}
      resposta = true;
  }
  else {
  //só para garantir que resposta fique com o valor falso
    resposta = false
  }

  if (resposta){
    digitalWrite(LG_PIN, HIGH);
    digitalWrite(LG_PIN, LOW);
    delay(2000);
    digitalWrite(LG_PIN, LOW);
  }else{
    digitalWrite(LG_PIN, LOW);
    digitalWrite(LG_PIN, HIGH);
  }

}
