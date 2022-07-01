import os
import glob
import time
import RPi.GPIO as GPIO
import pip
import paho.mqtt.client as paho
from gpiozero import PWMLED


GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

LED_PIN = 23
led = PWMLED(16)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

dir = '/sys/bus/w1/devices/'
fldr = glob.glob(dir + '28*')[0]
file = fldr + '/w1_slave'

topic = "mqtttest"
broker = "34.238.119.94"
borkerPort = "1883"
msg = "test"

def on_publish_func(client,userdata,mid):
        print("message published")


def raw():
        f = open(file, 'r')
        lines = f.readlines()
        f.close()
        return lines

def temp_reading():
        lines = raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)


        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp_c = float(temp_string) / 1000.0
                temp_f = temp_c * 9.0 / 5.0 + 32.0
                if temp_c > 40 and temp_c < 50:
                    led.value = 1
                elif temp_c > 30 and temp_c < 40:
                    led.value = 0.7
                elif temp_c > 20 and temp_c < 30:
                    led.value = 0.5
                elif temp_c > 10 and temp_c < 20:
                    led.value = 0.3
                elif temp_c < 10:
                    led.value = 0.1
        return temp_c, temp_f


while True:
	 print(temp_reading())
	 GPIO.output(LED_PIN, GPIO.HIGH)
	 time.sleep(1)
	 GPIO.output(LED_PIN, GPIO.LOW)
	 time.sleep(1)
	 client = paho.Client("mqtttest2")
	 client.on_publish = on_publish_func
	 client.connect(broker)
	 client.publish(topic, payload=str(temp_reading()), qos=0, retain=True)
