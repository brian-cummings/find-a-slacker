import logging.handlers
import os
import time

from gpiozero import MotionSensor

import caller

pir = MotionSensor(4)
pir_status = "Init"
motion_threshold_low = 10
motion_threshold_high = 60
motion_threshold = motion_threshold_low

file_path = os.getcwd()
logger = logging.getLogger("sensor")
log_handler = logging.handlers.RotatingFileHandler(file_path + "/logs/sensor.log", maxBytes=7168, backupCount=5)
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)


while True:
    count = 0
    motion_index = 0
    if pir_status or pir_status == "Init":
        motion_threshold = motion_threshold_low
    else:
        motion_threshold = motion_threshold_high
    while count < 120:
        if pir.motion_detected:
            motion_index = motion_index + 1
        count = count + 1
        time.sleep(.5)
    if motion_index > motion_threshold:
        motion = True
    else:
        motion = False
    if pir_status == motion:
        message = "PIRStatus: " + str(pir_status) +" | " + "Waiting " + str(motion_index)
        print(message)
        logger.info(message)
        time.sleep(5)
    else:
        pir_status = motion
        status_code = caller.slack_status(motion)
        if motion:
            message = "Motion Detected! (: " + str(motion_index)
            caller.slack_message (message)
            logger.info(message)
        else:
            message = "Motion NOT Detected! ): " + str(motion_index)
            caller.slack_message (message)

