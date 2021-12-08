import paho.mqtt.client as mqtt 
import time

# callback-funktio, jota kutsutaan, kun uusi tilattu viesti saapuu
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

#broker_address="test.mosquitto.org"
broker_address="broker.hivemq.com"

client = mqtt.Client("MeasurementSubscriberPMABC") # avaa yhteys brokerille
client.on_message=on_message # asetetaan callback-funktio

client.connect(broker_address) #avataa yhteys brokerille
client.loop_start() # aloitetaan kuuntelusilmukka

# tilataan viesti, jonka topic on ”meas”
client.subscribe("my_topicpm") 

time.sleep(100) # odotetaan 100 s
client.loop_stop() # lopetetaan kuuntelu
