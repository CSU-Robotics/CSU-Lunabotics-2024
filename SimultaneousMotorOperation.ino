#include <SPI.h>
#include <WiFi.h>
#include <WiFiUdp.h>


/* Define Pins */
// Motor 1 pins
int PUL_1 = 6; // PUL pin
int DIR_1 = 7; // DIR pin
// Motor 2 pins
int PUL_2 = 9;
int DIR_2 = 8;

/* Variables */
int pd = 500; // Pulse delay period 500
//int spd = A0; // Potentiometer
boolean setdir_1 = LOW, setdir_2 = LOW; // Set direction

long last_step_1, last_step_2, currTime;
int step_dur_1=500, step_dur_2=500;
bool on_1 = LOW, on_2 = HIGH;
int right_steps = 0, left_steps = 0;
long last_udp_check = 0;


int status = WL_IDLE_STATUS;
char ssid[] = "and"; //  your network SSID (name)
char pass[] = "lunabotics";    // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;            // your network key Index number (needed only for WEP)

unsigned int localPort = 2000;      // local port to listen on

char packetBuffer[255];
/* Interrupt Handler */ 

WiFiUDP Udp;

void setup() {
  pinMode (PUL_1, OUTPUT);
  pinMode (PUL_2, OUTPUT);

  pinMode (DIR_1, OUTPUT);
  pinMode (DIR_2, OUTPUT);
  
  Serial.begin(9600);

  while (status != WL_CONNECTED) {

    Serial.print("Attempting to connect to SSID: ");

    Serial.println(ssid);

    // Connect to WPA/WPA2 network. Change this line if using open or WEP network:

    status = WiFi.begin(ssid,pass);

    // wait 10 seconds for connection:

  }

  Serial.println("Connected to wifi");

  printWifiStatus();

  Udp.begin(localPort);

}

void loop() {
  //pd = 100;
  //pd = map((analogRead(spd)),0,1023,2000,50);


  currTime = micros();
  if (currTime - last_udp_check > 200000)
  {
    if (get_input())
    {
      set_movement_1();
      set_movement_2();
    }
    last_udp_check = currTime;
  }

  if (step_dur_1 < 450)
    step1();
  if (step_dur_2 < 450)
    step2();
/*
  digitalWrite(DIR_1, setdir);
  digitalWrite(DIR_2, !setdir);

  digitalWrite(PUL_1, HIGH);
  digitalWrite(PUL_2, HIGH);

  delayMicroseconds(pd);

  digitalWrite(PUL_1, LOW);
  digitalWrite(PUL_2, LOW);

  delayMicroseconds(pd);*/
}

bool get_input()
{
  int packetSize = Udp.parsePacket();
  if (packetSize)
  {
    int len = Udp.read(packetBuffer, 255);

    if (len > 0) {

      packetBuffer[len] = 0;

    }
   // Serial.println("Contents:");

   // Serial.println(packetBuffer);

    return true;
  }
  return false;
}

/*bool get_input()
{
  String s;
  if (Serial.available() > 0)
  {
    s = Serial.readString();
    s.toCharArray(packetBuffer, 5);
    return true;
  }
  return false;
}*/

void set_movement_1()
{ 
  char val[3]; 
  for (int i = 0; i < 2; i++)
    val[i] = packetBuffer[i];
  val[2] = '\0';
  int temp = atoi(val);
  temp -= 50;
  if (temp < 0)
    setdir_1 = LOW;
  else
    setdir_1 = HIGH;

  step_dur_1 = map(abs(temp), 0, 50, 500, 75);
  //Serial.println(step_dur_1);
}

void set_movement_2()
{ 
  char val[3]; 
  for (int i = 0; i < 2; i++)
    val[i] = packetBuffer[i+2];
  val[2] = '\0';
  int temp = atoi(val);
  temp -= 50;
  if (temp < 0)
    setdir_2 = LOW;
  else
    setdir_2 = HIGH;

  step_dur_2 = map(abs(temp), 0, 50, 500, 75);
}

void step1()
{
  if (currTime - last_step_1 > step_dur_1)
    halfPulse1();
}

void halfPulse1()
{
  on_1 = !on_1;
  digitalWrite(DIR_1, setdir_1);
  digitalWrite(PUL_1, on_1);
  last_step_1 = currTime;
}

void step2()
{
  if (currTime - last_step_2 > step_dur_2)
    halfPulse2();
}

void halfPulse2()
{
  on_2 = !on_2;
  digitalWrite(DIR_2, setdir_2);
  digitalWrite(PUL_2, on_2);
  last_step_2 = currTime;

}

void printWifiStatus() {

  // print the SSID of the network you're attached to:

  Serial.print("SSID: ");

  Serial.println(WiFi.SSID());

  // print your WiFi shield's IP address:

  IPAddress ip = WiFi.localIP();

  Serial.print("IP Address: ");

  Serial.println(ip);
}



