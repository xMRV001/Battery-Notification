print("----------------------------------")
print("    This Code Was Made By MRV     ")
print("----------------------------------")

import time

# py -m pip install psutil - it's responsible for battery information.

import psutil

# py -m pip install py-notifier - it's responsible for pop up a notification.

from pynotifier import Notification

# infinity loop so it can be always-on mode and check the battery till the if condition match.
    
while True:

    try:

        # Battery sensor.

        battery = psutil.sensors_battery()

        # Laptop power plugged or no.

        plugged = battery.power_plugged

        # Battery Percent as percent.

        percent = battery.percent

        # The condtion for notification is => if the laptop battery percent lower than 30% and it's not plugged to power.

        if percent <= 100 and plugged != True:

            # Here if our confition is True python will send notification to the user.

            Notification(
                
                # Notification title

                title = "Battery Low",

                # Notification description 

                description = " Please Use Charger Battery Is %" + str(percent), # str here because the + can't concatenate int it has to be str.
                
                # Here how long the notification will appear , default is 10 secondes you can change it to any number you want.

                duration = 10,

                # and finally the send notification method.

            ).send()
            
            # after all this break the infinity loop and stop checking for battery

            break

        # here the except common base class for all non-exit exceptions.

    except Exception as e:

        continue    