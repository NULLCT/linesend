#!/usr/bin/env python3

import requests
import atexit

def sendLine():
    with open("token.txt") as tokenfile:
        line_notify_api = 'https://notify-api.line.me/api/notify'
        headers = {'Authorization': f'Bearer {tokenfile.read()}'}
        print("token: "+tokenfile.read())
        data = {'message': f'{words[0:-1]}'}

        requests.post(line_notify_api, headers = headers, data = data)

words = "\n"

atexit.register(sendLine)

while 1:
    words+=input()+"\n";
