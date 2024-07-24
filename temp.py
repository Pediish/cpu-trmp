
import time
import OPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)  


TEMP_THRESHOLD = 50

def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp_str = f.read()
    return int(temp_str) / 1000

try:
    while True:
        cpu_temp = get_cpu_temperature()
        if cpu_temp > TEMP_THRESHOLD:
            GPIO.output(18, GPIO.HIGH)
        if cpu_temp < TEMP_THRESHOLD-5:
            GPIO.output(18, GPIO.LOW)
        time.sleep(5)  
except KeyboardInterrupt:
    GPIO.cleanup()
