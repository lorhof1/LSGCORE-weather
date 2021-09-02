#beginning of app Weather
def lsg_weather_http_get(url):
    Download = ''
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            try:
                Download = Download + (str(data, 'utf8'))
            except:
                break
        else:
            break
    s.close()
    return Download.split('\n', 12)[-1]

def LSGCORE_weather():
    try:
        import socket
    except:
        print()

    ip = lsg_weather_http_get('http://api.ipify.org/')
    location_data = lsg_weather_http_get('http://ip-api.com/line/' + ip)
    location = location_data.split('\n')[2]

    weather_report = (lsg_weather_http_get('http://wttr.in/' + location))
    weather = weather_report.split('\n')[-6].split(' ')[-1]

    drawBG()
    infoBar()
    display.draw_text(10, 10, 'Weather in ' + location + ':', font, color565(255, 255, 255), 0, False, 1)
    display.draw_text(10, 40, weather, big_font, color565(255, 255, 255), 0, False, 1)
    display.draw_text(10, 100, 'Location from IP adress | Hold to exit', font, color565(255, 255, 255), 0, False, 1)
    if getInteraction() == 'hold':
        home()
    else:
        LSGCORE_weather()
appNames.append('Weather')
appIDs.append(LSGCORE_weather)
#end of app Weather

