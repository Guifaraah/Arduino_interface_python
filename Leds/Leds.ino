int led_Azul = 8;  //Atribuindo o pino digital 8 do arduino à variável ledAzul
int led_Vermelho = 4;  // Atribuindo o pino digital 4 do arduino à variável ledVermelho
int valor_recebido;  // Criando variável que se refere aos valores recebidos pela porta serial do arduino IDE.

void setup() {
  Serial.begin(9600);  // Baud rate ou velocidade dos dados recebidos.
  pinMode(led_Vermelho, OUTPUT);  // Define que o pino do ledVermelho/ledAzul funcionará como uma saída de sinal
  pinMode(led_Azul, OUTPUT);

}

void loop() {
  if(Serial.available() > 0)  // Essa função verifica se há algum valor chegando na porta serial  que seja maior que 0
  {
    valor_recebido = Serial.read();  // Se a afirmação acima for verdadeira, o valor lido na porta serial será atribuído à variável "valor_recebido"
  }
  if(valor_recebido == '0'){  
    digitalWrite(led_Vermelho,HIGH);  //ledVermelho liga.
  }
  else if(valor_recebido == '1'){
    digitalWrite(led_Vermelho,LOW);  //ledVermelho desliga
  }
  else if(valor_recebido == '2'){  // ledAzul liga
    digitalWrite(led_Azul,HIGH);
  }
  else if(valor_recebido == '3'){  //ledAzul desliga
    digitalWrite(led_Azul,LOW);
  }

}
//Lembrando que esses valores acima: 1, 0, 2 e 3... foram definidos no código em Python. Eles são a relação do usuário da interface com os botões de ligar e desligar
