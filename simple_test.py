import json
import logging

import tomli

from renault.renault import RenaultVehicleClient

with open("config/renault_config.toml", "rb") as config_file:
    config = tomli.load(config_file)

# establish connection
car = RenaultVehicleClient(login_id=config["login_id"],
                           password=config["password"],
                           account_locale="de_AT",
                           backend_log_level=logging.DEBUG)

# query battery status
status = car.get_status(car.STATUS_BATTERY_ONLY)
print(json.dumps(status, indent=4))

# query custom data selection
status = car.get_status((
    car.StatusType.BATTERY,
    car.StatusType.COCKPIT,
))

print(json.dumps(status, indent=4))
