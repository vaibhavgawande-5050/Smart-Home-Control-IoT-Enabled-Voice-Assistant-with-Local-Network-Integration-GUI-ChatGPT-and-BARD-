#ifdef ENABLE_DEBUG
  #define DEBUG_ESP_PORT Serial
  #define NODEBUG_WEBSOCKETS
  #define NDEBUG
#endif 

#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <SinricPro.h>
#include<SinricProSwitch.h>



const char* ssid = "VaibhavG";
const char* password = "vaibhav@5050";
const int red_light =5;  // D1
const int green_light=4; //D2
const int yellow_light=2;  // D4 and built in led

struct RelayInfo {
  String deviceId;
  String name;
  int pin;
};


std::vector<RelayInfo> relays = {
    {"659c326accc93539a11f1fb7", "Relay 1", D1},  
    {"659c32ecccc93539a11f2035", "Relay 2", D2},
    {"659f9843ccc93539a1210887", "Relay 3", D4},
};


#define APP_KEY    "6e61ac02-eaff-4cf5-8c35-87dde6e816ab"
#define APP_SECRET "4b11e499-e3ea-42c5-b861-66de299e1b35-a6d92f26-45d5-4681-bef2-4f69e19433a7"
#define BAUD_RATE  115200

WiFiServer server(80);


bool onPowerState(const String &deviceId, bool &state) {
  for (auto &relay : relays) {
    if (deviceId == relay.deviceId) {
      Serial.printf("Device %s turned %s\r\n", relay.name.c_str(), state ? "on" : "off");
      digitalWrite(relay.pin, state);
      return true;
    }
  }
  return false;
}


void setupRelayPins() {
  for (auto &relay : relays) {
    pinMode(relay.pin, OUTPUT);
  }
}


void setupWiFi() {
  Serial.printf("\r\n[Wifi]: Connecting");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.printf(".");
    delay(250);
  }
  Serial.printf("connected!\r\n[WiFi]: IP-Address is %s\r\n", WiFi.localIP().toString().c_str());
}

void setupSinricPro() {
  for (auto &relay : relays) {
    SinricProSwitch &mySwitch = SinricPro[relay.deviceId];
    mySwitch.onPowerState(onPowerState);
  }

SinricPro.onConnected([]() { Serial.printf("Connected to SinricPro\r\n"); });
  SinricPro.onDisconnected([]() { Serial.printf("Disconnected from SinricPro\r\n"); });

  SinricPro.begin(APP_KEY, APP_SECRET);
}


void setup() {
  Serial.begin(BAUD_RATE);
  setupRelayPins();
  setupWiFi();
  setupSinricPro();
  server.begin();
  delay(1000);
}

void handleHttpRequest(WiFiClient client) {
  String request = client.readStringUntil('\n');
  client.flush();
  Serial.println(request);
  Serial.println("Sending request . . . .");
  Serial.println("===========================================================");
  Serial.println("Client connected");

  if (request.indexOf("redlighton") != -1) {
    digitalWrite(red_light, HIGH);
    Serial.println("LED IS ON NOW");
  }
   else if (request.indexOf("redlightoff") != -1) {
    digitalWrite(red_light, LOW);
    Serial.println("LED IS OFF NOW");
  }

  if (request.indexOf("greenlighton") != -1) {
    digitalWrite(green_light, HIGH);
    Serial.println("LED IS ON NOW");
  }
   else if (request.indexOf("greenlightoff") != -1) {
    digitalWrite(green_light, LOW);
    Serial.println("LED IS OFF NOW");
  }

  if (request.indexOf("bulbon") != -1) {
    digitalWrite(yellow_light, LOW);
    Serial.println("LED IS ON NOW");
  }
   else if (request.indexOf("bulboff") != -1) {
    digitalWrite(yellow_light, HIGH);
    Serial.println("LED IS OFF NOW");
  }

  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type: text/html");
  client.println();
  client.println("OK");

  Serial.println("Client Disconnected");
  Serial.println("===========================================================");
  Serial.println("                              ");
}


void loop() {
  SinricPro.handle();

  WiFiClient client = server.available();
  if (client) {
    handleHttpRequest(client);
  }
}





























