#!/usr/bin/env python3

from sys import argv
import paho.mqtt.client as mqtt

# This is the Publisher

client = mqtt.Client()
client.connect("localhost",1883,60)
client.publish("topic/test", argv[1]);
client.disconnect();


