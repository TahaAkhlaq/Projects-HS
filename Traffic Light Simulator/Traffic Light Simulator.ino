Skip to content
        Search or
    jump to…
                Pull requests
                    Issues
                        Marketplace
                            Explore

            @TahaAkhlaq
                Nexuist /
            Arduino -
        Traffic - Light Public Code Issues Pull requests Actions Projects Security Insights Arduino - Traffic - Light / main.ino @Nexuist Nexuist Renamed files and began drawing circuit Latest commit 30fe8aa on Aug 13,
    2016 History 1 contributor 151 lines(136 sloc) 5.1 KB

    /*
     Excerpt from: https://www.arduino.cc/en/Reference/AnalogWrite
      "The PWM outputs generated on pins 5 and 6 will have higher-than-expected duty cycles. This is because of interactions with the millis() and delay() functions, which share the same internal timer used to generate those PWM outputs."
      I was having issues with the red light not turning off all the way, and I guess now I know why.
     */
    const int potIntensity = A0,
              btnChangeLight = 9, btnChangeMode = 8;
enum LIGHT
{
  RED = 5,
  YELLOW = 4,
  GREEN = 3
};
enum MODE
{
  BLINK,
  FADE,
  STAY_ON
};
LIGHT currentLight = RED;
MODE currentMode = STAY_ON;

/* Typical startup. Called once on boot. */
void setup()
{
  Serial.begin(9600);
  pinMode(RED, OUTPUT);
  pinMode(YELLOW, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(potIntensity, INPUT);
  pinMode(btnChangeLight, INPUT);
  pinMode(btnChangeMode, INPUT);
}

/* Sets the brightness of each light to zero.
Since there is only one light on at a time, this could be optimized by only turning off the currently illuminated light, but that adds complexity. */
void resetLights()
{
  analogWrite(RED, 0);
  analogWrite(YELLOW, 0);
  analogWrite(GREEN, 0);
}

/* Return the current potentiometer value. analogRead returns a number between 0 and 1023, but analogWrite accepts a value from 0 to 255. This function solves that discrepancy. */
int pot()
{
  return map(analogRead(potIntensity), 0, 1023, 0, 255);
}

/*
  A note on debounce:
  The two functions below are called every loop iteration. The loop runs extremely fast. As a result, pressing the button once can trigger more than one change because the button will still register as being pressed in the next iteration. The solution to this is a debounce.
  When the button is pressed, debounce is set to true. When debounce is true, the function will not return true, so the light/mode will not be changed. Debounce is reset when the button is detected as unpressed.
  For optimization, these two methods could be combined into one. This could add more complexity, however, as two debounces would need to be used rather than one.
*/
bool shouldChangeLight()
{
  static bool debounce = false; // Static variables preserve their value across function calls
  bool light = digitalRead(btnChangeLight);
  if (light && !debounce)
  {
    debounce = true;
    return true;
  }
  if (!light)
    debounce = false;
  return false;
}

bool shouldChangeMode()
{ // Identical to shouldChangeLight() except for the pin constant
  static bool debounce = false;
  bool mode = digitalRead(btnChangeMode);
  if (mode && !debounce)
  {
    debounce = true;
    return true;
  }
  if (!mode)
    debounce = false;
  return false;
}

/*
  A note on millis():
  Traditionally, If you want to wait for some time on Arduino, you'd use delay(). For this application, delay() presents a problem: it blocks the loop, so that pressing the buttons or changing the pot do not cause any visible changes until after the delay is over. I wanted these changes to be dealt with as soon as they happened.
  millis() returns the amount of milliseconds since the program started running. By applying modulo operations to it (such as millis() % 500) and checking if the result is 0, we can ensure that certain portions of our code are only executed in regular intervals. For example, the last few lines of code in loop():
    if (millis() % 1000 == 0) {
      Serial.println(pot());
    }
  ...Will only be run every second, and therefore the serial console will not be spammed.
*/
void executeCurrentMode()
{
  static int brightness = 0;
  static bool shouldIncrement = true;
  switch (currentMode)
  {
  case STAY_ON:
    analogWrite(currentLight, pot());
    break;
  case BLINK:
    if (millis() % 250 == 0)
    {
      brightness = 0;
    }
    if (millis() % 500 == 0)
    {
      brightness = pot();
    }
    analogWrite(currentLight, brightness);
    break;
  case FADE:
    if (millis() % 20 == 0)
    {
      /*
        Following code can be optimized like so:
        brightness = brightness + (shouldIncrement ? 1 : -1);
        shouldIncrement = (brightness >= 255 ? false : true);
      */
      if (shouldIncrement)
        brightness++;
      if (!shouldIncrement)
        brightness--;
      if (brightness >= 255)
        shouldIncrement = false;
      if (brightness <= 0)
        shouldIncrement = true;
    }
    analogWrite(currentLight, brightness);
    break;
  }
}

/*
  A note on switch:
  In this application switch statements are used to determine what mode/light to switch to based on the current mode/light. This can probably be optimized by iterating over the enums.
*/
void loop()
{
  // Acquire values
  if (shouldChangeLight())
  {
    resetLights();
    switch (currentLight)
    {
    case RED:
      currentLight = GREEN;
      break;
    case YELLOW:
      currentLight = RED;
      break;
    case GREEN:
      currentLight = YELLOW;
      break;
    }
  }
  if (shouldChangeMode())
  {
    switch (currentMode)
    {
    case STAY_ON:
      currentMode = BLINK;
      break;
    case BLINK:
      currentMode = FADE;
      break;
    case FADE:
      currentMode = STAY_ON;
      break;
    }
  }
  executeCurrentMode();
  if (millis() % 1000 == 0)
  {
    Serial.println(pot());
  }
}
Footer
© 2022 GitHub, Inc.Footer navigation
                        Terms
                            Privacy
                                Security
                                    Status
                                        Docs
                                            Contact GitHub
                                                Pricing
                                                    API
                                                        Training
                                                            Blog
                                                                About
                                                                    Arduino -
                    Traffic - Light / bill - of - materials.html at master · Nexuist / Arduino - Traffic - Light Arduino - Traffic - Light / main.ino at master · Nexuist / Arduino - Traffic - Light