devices = [
	{
		"id": 8,
		"name": "Curtain",
		"ip": "192.168.1.102",
		"state": 0,
		"device_key": "sqs20n7nI9mdio2mew",
		"typeId": 1,
		"command": "curtain",
		"description": "Moves up and down the curtain"
	},
	{
		"id": 9,
		"name": "Smart conditioner",
		"ip": "192.168.1.243",
		"state": 0,
		"device_key": "conD9mdc73om934",
		"typeId": 2,
		"command": "conditioner_main",
		"description": "Controls conditioner"
	},
	{
		"id": 10,
		"name": "ESP-01 Smart Socket",
		"ip": "192.168.1.144",
		"state": 0,
		"device_key": "knb78G^n03foi",
		"typeId": 2,
		"command": "socket",
		"description": "Controls Smart socket"
	},
	{
		"id": 18,
		"name": "water_sensor Kitchen",
		"ip": "192.168.1.130",
		"state": 0,
		"device_key": "Qsd2dfj7sdsegf40dg",
		"typeId": 1,
		"command": "water_sensor_kitchen",
		"description": "Turns on/off hall lights"
	},
	{
		"id": 19,
		"name": "water_sensor Toilet",
		"ip": "192.168.1.131",
		"state": 0,
		"device_key": "dfj7sdsegf40dg",
		"typeId": 1,
		"command": "water_sensor_toilet",
		"description": "Turns on/off hall lights"
	},
	{
		"id": 20,
		"name": "water_sensor van",
		"ip": "192.168.1.132",
		"state": 0,
		"device_key": "Qsd2dgwqzdsegf40dg",
		"typeId": 1,
		"command": "water_sensor_van",
		"description": "Turns on/off water sensor"
	},
	{
		"id": 21,
		"name": "Smart stove",
		"ip": "192.168.1.154",
		"state": 0,
		"device_key": "knb78G^n0sdf3foi",
		"typeId": 2,
		"command": "smart_stove",
		"description": "Controls stove"
	},
	{
		"id": 22,
		"name": "IoT TV Remote",
		"ip": "192.168.1.176",
		"state": 0,
		"device_key": "asdgdsf4567)N$3zx4a2",
		"typeId": 2,
		"command": "tv_remote",
		"description": "Controls Remote of smart tv that sends IR datas"
	},
	{
		"id": 23,
		"name": "Watt measurer of kitchen",
		"ip": "192.168.1.104",
		"state": 0,
		"device_key": "fuckwaddMeasurerKey",
		"typeId": 2,
		"command": "watt_measurer_kitchen",
		"description": "Measures the flow of current"
	},
	{
		"id": 24,
		"name": "Water measurer of kitchen",
		"ip": "192.168.1.223",
		"state": 0,
		"device_key": "jbhbnefb63bno2u1",
		"typeId": 2,
		"command": "water_measurer_kitchen",
		"description": "Measures the flow of water"
	},
	{
		"id": 25,
		"name": "Three mode switch",
		"ip": "192.168.1.209",
		"state": 0,
		"device_key": "lights_hash",
		"typeId": 2,
		"command": "three_mode_switch",
		"description": "Controls Two mode switch"
	},
	{
		"id": 26,
		"name": "Suw sensor",
		"ip": "192.168.1.130",
		"state": 0,
		"device_key": "pir_hash",
		"typeId": 1,
		"command": "water_pump",
		"description": "suw sensory dolandyrmak"
	},
	{
		"id": 27,
		"name": "IoT TV Remote",
		"ip": "192.168.1.177",
		"state": 0,
		"device_key": "alondatv2",
		"typeId": 2,
		"command": "tv_remote2",
		"description": "Controls Remote of smart tv that sends IR datas"
	},
	{
		"id": 28,
		"name": "Water measurer of kitchen2",
		"ip": "192.168.1.224",
		"state": 0,
		"device_key": "suwolceya1",
		"typeId": 2,
		"command": "water_measurer_kitchen2",
		"description": "Measures the flow of water"
	},
	{
		"id": 29,
		"name": "Door Lock",
		"ip": "192.168.1.100",
		"state": 0,
		"device_key": "door_hash",
		"typeId": 1,
		"command": "unlock_door",
		"description": "Unlock door"
	},
	{
		"id": 30,
		"name": "Gerkon",
		"ip": "192.168.1.149",
		"state": 0,
		"device_key": "gerkon_sensor_secret",
		"typeId": 1,
		"command": "ping_gerkon",
		"description": "GERKON OPEN/CLOSE"
	},
	{
		"id": 31,
		"name": "Gaz sensor",
		"ip": "192.168.1.145",
		"state": 0,
		"device_key": "gas_sensor_secret",
		"typeId": 1,
		"command": "gas_sensor",
		"description": "gas sensor, shows current gas status"
	},
	{
		"name": "Local binary test",
		"ip": "127.0.0.1:5000",
		"state": 0,
		"device_key": "23abcK238873244",
		"typeId": 1,
		"command": "test_local",
		"description": "Turns on/off Local test"
	},
	{
		"id": 999,
		"name": "Local Json to Args test",
		"ip": "127.0.0.1:5000",
		"state": 0,
		"device_key": "ase44f3f23f3",
		"typeId": 2,
		"command": "test_local_json",
		"description": "Json to args of local test func"
	}
]

pins = [
	{
		"id": 1,
		"name": "Socket1",
		"command": "socket1",
		"description": "Pin 2 of smart socket",
		"action": "0",
		"deviceId": 10,
	},
	{
		"id": 2,
		"name": "Socket2",
		"command": "socket2",
		"description": "Pin 2 of smart socket",
		"action": "0",
		"deviceId": 10,
	},
	{
		"id": 3,
		"name": "Socket3",
		"command": "socket3",
		"description": "Pin3 of smart socket",
		"action": "0",
		"deviceId": 10,
	},
	{
		"id": 4,
		"name": "Conditioner Mode HIGH",
		"command": "mode_high",
		"description": "Changes the conditioner operation power",
		"action": "0",
		"deviceId": 9,
	},
	{
		"id": 5,
		"name": "Conditioner Mode MED",
		"command": "mode_med",
		"description": "Changes the conditioner operation power",
		"action": "0",
		"deviceId": 9,
	},
	{
		"id": 6,
		"name": "Conditioner Mode LOW",
		"command": "mode_low",
		"description": "Changes the conditioner operation power",
		"action": "0",
		"deviceId": 9,
	},
	{
		"id": 7,
		"name": "Conditioner Auto/Manual switch",
		"command": "auto_manual_switch",
		"description": "Changes the use of manual or auto mode (Tel mode)",
		"action": "auto",
		"deviceId": 9,
	},
	{
		"id": 8,
		"name": "Temperature control",
		"command": "temperature",
		"description": "Controls room temperature according to command (ex.: 'heater:25:' or 'cooler:16:')",
		"action": "cooler:20:",
		"deviceId": 9,
	},	
	{
		"id": 14,
		"name": "Cooker heater 1",
		"command": "cooker1",
		"description": "Controls the cooker heaters timing.",
		"action": "0",
		"deviceId": 21,
	},
	{
		"id": 15,
		"name": "Cooker heater 2",
		"command": "cooker2",
		"description": "Controls the cooker heaters timing.",
		"action": "0",
		"deviceId": 21,
	},
	{
		"id": 16,
		"name": "Cooker heater 3",
		"command": "cooker3",
		"description": "Controls the cooker heaters timing.",
		"action": "0",
		"deviceId": 21,
	},
	{
		"id": 17,
		"name": "Cooker heater 4",
		"command": "cooker4",
		"description": "Controls the cooker heaters timing.",
		"action": "0",
		"deviceId": 21,
	},
	{
		"id": 18,
		"name": "Cooker power pin",
		"command": "power",
		"description": "Controls the cooker power source.",
		"action": "0",
		"deviceId": 21,
	},
	{
		"id": 19,
		"name": "Cooker Auto/Manual switch",
		"command": "auto_manual_switch",
		"description": "Changes the use of manual or auto mode (Tel mode)",
		"action": "auto",
		"deviceId": 21,
	},
	{
		"id": 87,
		"name": "IR Remote command",
		"command": "command",
		"description": "sends the command to arduino to manage TV",
		"action": "tvpower",
		"deviceId": 22,
	},
	{
		"id": 88,
		"name": "Three mode switch state1",
		"command": "pin1",
		"description": "Controls the light modes of three mode switch ESP (Use action=1 or action=2 or action=3)",
		"action": "0",
		"deviceId": 25,
	},
	{
		"id": 95,
		"name": "Three mode switch state2",
		"command": "pin2",
		"description": "Controls the light modes of three mode switch ESP (Use action=1 or action=3)",
		"action": "0",
		"deviceId": 25,
	},
	{
		"id": 96,
		"name": "Three mode switch state3",
		"command": "pin3",
		"description": "Controls the light modes of three mode switch ESP (Use action=1 or action=3)",
		"action": "0",
		"deviceId": 25,
	},
	{
		"id": 89,
		"name": "IR Remote command",
		"command": "command",
		"description": "sends the command to arduino to manage TV",
		"action": "tvpower",
		"deviceId": 27,
	},
	{
		"id": 998,
		"name": "Mirror switch",
		"command": "switch_mirror",
		"description": "Mirror actuator pin",
		"action": "0",
		"deviceId": 999,
	},
	{
		"id": 999,
		"name": "AI pin",
		"command": "switch_AI",
		"description": "Activates AI function",
		"action": "0",
		"deviceId": 999,
	}
]

device_types = [
	{
		"id": 1,
		"name": "ESP-01-binary",
		"description": "ESP8266 Binary data like '/control/1' or '/control/0'"
	},
	{
		"id": 2,
		"name": "ESP-JSON-to-Arguments",
		"description": "ESP8266 with several arguments provided from data in JSON"
	},
	{
		"id": 3,
		"name": "Esp8266-command-argument",
		"description": "ESP8266 with argument provided in 'control' from data in 'action' of JSON"
	}
]


sensors = [
	{
		"id": 1,
		"name": "Watt measurer sensor",
		"command": "watt_measurer",
		"description": "Measured amount of current",
		"value": "0.0",
		"deviceId": 23,
		"typeId": 1
	},
	{
		"id": 2,
		"name": "Water measurer sensor",
		"command": "water_measurer_sensor",
		"description": "Measured amount of water",
		"value": "0.0",
		"deviceId": 24,
		"typeId": 1,
	},
	{
		"id": 3,
		"name": "Water measurer sensor2",
		"command": "water_measurer_sensor",
		"description": "Measured amount of water",
		"value": "0.0",
		"deviceId": 28,
		"typeId": 1
	}
]
