#!/usr/bin/python3.6

from ftntlib import FortiManagerJSON

ip = '10.20.30.31'
login = 'admin'
password = 'xxxxxxxxx'

url='sys/proxy/json'
resource="/api/v2/monitor/user/detected-device/select?&vdom=root&expand_child_macs=true&with_fortilink=true&with_fortiap=true&with_endpoint=true&with_dhcp=true&width_user=true"

data= {'target': ["adom/root/device/OT60FR"], 'action': 'get','resource':resource }


api = FortiManagerJSON()
api.login(ip, login, password)
api.debug('on')
status,mydata = api.execute(url,data)
print(mydata[0]['response']['results'])
api.debug('off')
api.logout()

