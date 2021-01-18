# control your mouse using android sensors via node sensor app xml stream
import pyautogui
import socket
import bs4
import time
pyautogui.FAILSAFE = False
ip = '192.168.43.212'
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, 5555))
timeout = time.time() + 30   # 30 seconds from now
while True:
    test = 0
    rawdata = sock.recvfrom(5555)
    data = str(rawdata)
    sauce = bs4.BeautifulSoup(data, 'lxml')
    # print(sauce)
    aX = (float(sauce.find('accelerometer1').text))
    aY = (float(sauce.find('accelerometer2').text))
    aZ = (float(sauce.find('accelerometer3').text))
    gX = (float(sauce.find('gyroscope1').text))
    gY = (float(sauce.find('gyroscope2').text))
    gZ = (float(sauce.find('gyroscope3').text))
    pyautogui.moveRel(-aX * 5, aY * 2.5, duration=0.05)
    # print('Accelerometer: ' + str(aX) + ',' + str(aY) + ',' + str(aZ))
    # print('Gyroscope: ' + str(gX) + ',' + str(gY) + ',' + str(gZ))
    # time.sleep(0)
    if test == 5 or time.time() > timeout:
        break
    test = test - 1
# Avaialble sensros on redmi note 4
# gravity, light intensity, proximity, linear acceleration, rotation vector,
# acceleromater, gyroscope, magnetometer, noise level
