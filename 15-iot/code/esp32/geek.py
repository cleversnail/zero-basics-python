import dht
import machine
from time import sleep

from ssd1306 import SSD1306_I2C

from umqtt.simple import MQTTClient


dht11_data = machine.Pin(5)
d = dht.DHT11(dht11_data)


i2c = machine.SoftI2C(scl=machine.Pin(7), sda=machine.Pin(8))
# print(i2c.scan()) # 从机地址60

oled = SSD1306_I2C(128, 64, i2c, addr=60)

# oled.text('Hello World', 0, 20)
# oled.show()

fonts= {
    "温": [0x0F,0x88,0x4F,0x08,0x0F,0x80,0x5F,0x15,0x35,0x55,0x95,0x3F,0x80,0x80,0x80,0x80,0x80,0x00,0xC0,0x40,0x40,0x40,0x40,0xE0],
    "度": [0x02,0x7F,0x48,0x7F,0x48,0x4F,0x40,0x5F,0x48,0x44,0x43,0x9C,0x00,0xE0,0x80,0xE0,0x80,0x80,0x00,0xC0,0x40,0x80,0x00,0xE0],
}

def chinese(ch_str, x_axis, y_axis, ch_size=12):
    ''' 刷单字到屏幕像素点
    Args:
        ch_str  单字或连接汉字
        x_axis,y_axis  定位点
        ch_size  单字大小，默认12，最大16
    '''
    global oled
    offset_ = 0
    for k in ch_str:
        byte_data = fonts[k]
        print(fonts[k], "offset=", offset_)
        for y in range(0, ch_size):
            # 进制转换、补全
            a_ = '{:0>8b}'.format(byte_data[y])
            b_ = '{:0>8b}'.format(byte_data[y+ch_size])
            # 绘制像素点 （按取模软件的行列式方式）
            for x in range(0, 8):
                oled.pixel(x_axis + offset_ + x, y + y_axis, int(a_[x]))
                oled.pixel(x_axis + offset_ + x + 8, y + y_axis, int(b_[x]))
        offset_ += ch_size


# 20ms周期 50hz
# 0.5ms 为0度
# 2.5ms为180度依次增加

sg90 = machine.PWM(machine.Pin(2),freq=50, duty=0)


server = "broker-cn.emqx.io" 
c = MQTTClient("umqtt_client", server)
c.connect()



while True:
    d.measure()
    temp = d.temperature()
    print(f'temperature is {temp} °C')
    oled.fill(0)
    chinese('温度',0,20)
    oled.text(f'{d.temperature(temp)} ', 32, 20)
    chinese('度', 64, 20)
    oled.show()
    c.publish(b"foo_topic", temp)
    sleep(2)
    sg90.duty(70)



c.disconnect()