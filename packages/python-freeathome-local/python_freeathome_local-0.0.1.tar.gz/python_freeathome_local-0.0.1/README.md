# python_freeathome_local

The datamodel of the Free@Home Rest-API is setup the following way:
- The root-node is a SysAp
- The SysAp contains devices and a floorplan
- Each device has 1 to many channels (the behaviour of a channel is defined by the FunctionID)
- A channel has 0 to many Input- and Output-Datapoints (the behaviour of a datapoint is defined by the PairingID)
- An Input-Datapoint is used to set a value (e.g. turn on a switch)
-- To change the value of an such a datapoint a PUT-call is needed
- An Output-Datapoint shows the current state (e.g. switch is on)
-- All modifications are reported through a websocket-connection
- A device and a channel can have 0 to many parameters (the function of a parameter is defined by the ParameterID)

## Drawback
The major drawback I see so far regarding the Rest-API is that the parameters can't be controlled.
E.g. the WeatherStation has a parameter called 'par0039' (TRANSMISSION_INTERVAL), which defines how often updated values are send. This interval can be changed in the mobile app, but not through the Rest-API, additionally (what is even more worse) any modifications are not reported through the websocket. This means that after the initial load of the configuration any modifications to the parameters through the mobile app are not recognized by this library :(

## Implemented channels
| Name | Inputs | Outputs |
|--|--|--|
| BrightnessSensor | - | BrightnessLevel (float) - state<br>BrightnessAlarm (bool) |
| RainSensor       | - | RainAlarm (bool) - state<br>RainSensorActivationPercentage (float)<br>rainSensorFrequency (float) |
| TemperatureSensor | - | OutdoorTemperature (float) - state<br>FrostAlarm (bool) |
| WindSensor | - | WindSpeed (float) - state<br>WindAlarm (bool)<br>WindForce (float) |
| Trigger | TimedStartStop - press | - |
| SwitchActuator | SwitchOnOff(bool) - turnOn/turnOff<br>Forced(bool)<br>TimedStartStop(bool)<br>TimedMovement(bool) | InfoOnOff (bool) - state<br>InfoForce (bool)<br>InfoError (bool) |
| WindowDoorSensor | - | WindowDoor (bool) - state |
| MovementDetector | InfoOnOff | InfoOnOff (bool) - state<br>BrightnessLevel (float)<br>TimedMovement (bool)<br>TimedPresence (bool) |
| SwitchSensor | - | SwitchOnOff (bool) - state |
