from datetime import datetime, timedelta

schedules = [
	# {
	# 	"id": 2,
	# 	"name": "TV on",
	# 	"typeId": 1,
	# 	"deviceId": 22,# to what device it belongs to
	# 	"pinId": 87, #Required pin to use
	# 	"device_command": "tv_remote", #which device to operate
	# 	"pin_action": "tvpower", #what action pin should get
	# 	"description": "Turns tv on when door opens"
	# },
	{
		"id": 1,
		"name": "Welcome sound",
		"typeId": 2,
		"deviceId": 10,
		"path": "you-wanna-come-in.wav",
		"description": "Says hello when triggered"
	},
	{
		"id": 3,
		"name": "Scheduled event 1",
		"typeId": 1,
		"deviceId": 10,
		"pinId": 1,
		"device_command": "tvpower",
		"pin_action": "power_off",
		"description": "Turns off tv on specified time",
		"on_time": datetime.now() + timedelta(minutes = 2)
	}
]

# curl --header "Content-Type: application/json" --request POST --data '{"command":"tv_remote","pins":[{"command":"command","action":"tvpower"}]}' http://127.0.0.1:5000/esp/JsonToArg/
