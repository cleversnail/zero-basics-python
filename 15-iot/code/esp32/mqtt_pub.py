# https://github.com/micropython/micropython-lib/tree/master/micropython/umqtt.simple

from umqtt.simple import MQTTClient

server = "broker-cn.emqx.io" 
c = MQTTClient("umqtt_client", server)
c.connect()
c.publish(b"foo_topic", b"hello")
c.disconnect()