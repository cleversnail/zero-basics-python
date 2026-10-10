def do_connect():
    import network 
    wifi = network.WLAN(network.STA_IF)  
    if not wifi.isconnected(): #判断WIFI连接状态
        print('connecting to network...')
        wifi.active(True) 
        wifi.connect('ssid', 'pass') #essid为WIFI名称,password为WIFI密码
        while not wifi.isconnected():
            pass 
    print('network config:', wifi.ifconfig())

do_connect()