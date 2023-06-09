from main import db

from main.models import (
	Master_device,
	Device,
	Sensor,
	Resident,
	City,
	Region,
	Flat,
	House,
	Pin,
	Device_type,
	Sensor_type,
	Trigger,
	QR_code,
	Room,
	Schedule,
	Sensor_record,
	Resident_type,
)

from main.db_migration_data.devices_config import master_devices, devices, pins, sensors
from main.db_migration_data.default_devices_config import device_types, sensor_types, triggers, resident_types
from main.db_migration_data.locale_config import cities, regions, houses, flats, rooms
from main.db_migration_data.residents_config import residents, qr_codes
from main.db_migration_data.schedules_config import schedules


# saving old record before migration
cached_records = []
try:
	cached_records = [record.json(withDates = False) for record in Sensor_record.query.all()]
except Exception as ex:
	print(ex)

db.drop_all()
db.create_all()


for city in cities:
	db_city = City(**city)
	db.session.add(db_city)

for region in regions:
	db_region = Region(**region)
	db.session.add(db_region)

for house in houses:
	db_house = House(**house)
	db.session.add(db_house)

for flat in flats:
	db_flat = Flat(**flat)
	db.session.add(db_flat)

for resident in residents:
	db_resident = Resident(**resident)
	db.session.add(db_resident)

for qr_code in qr_codes:
	db_qr_code = QR_code(**qr_code)
	db.session.add(db_qr_code)

for room in rooms:
	db_room = Room(**room)
	db.session.add(db_room)

for schedule in schedules:
	db_schedule = Schedule(**schedule)
	db.session.add(db_schedule)

for device in master_devices:
	db_device = Master_device(**device)
	db.session.add(db_device)

for device in devices:
	db_device = Device(**device)
	db.session.add(db_device)

for pin in pins:
	db_pin = Pin(**pin)
	db.session.add(db_pin)

for sensor in sensors:
	db_sensor = Sensor(**sensor)
	db.session.add(db_sensor)

for device_type in device_types:
	db_device_type = Device_type(**device_type)
	db.session.add(db_device_type)

for sensor_type in sensor_types:
	db_sensor_type = Sensor_type(**sensor_type)
	db.session.add(db_sensor_type)

for trigger in triggers:
	db_trigger = Trigger(**trigger)
	db.session.add(db_trigger)

for resident_type in resident_types:
	db_resident_type = Resident_type(**resident_type)
	db.session.add(db_resident_type)

if cached_records:
	for record in cached_records:
		db_sensor_record = Sensor_record(**record)
		db.session.add(db_sensor_record)


db.session.commit()