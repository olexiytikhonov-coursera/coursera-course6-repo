#! /usr/bin/env python3

import os 
import requests
import argparse

def send_reviews(basepath, ip, port):

    folder = os.listdir(basepath)

    list = []

    for file in folder:
        with open(basepath + file, 'r') as f:
            list.append({"title":f.readline().rstrip("\n"),
            		"name":f.readline().rstrip("\n"),
            		"date":f.readline().rstrip("\n"),
            		"feedback":f.read().rstrip("\n")})

    url = 'http://' + ip + ':' + port + '/feedback/'
    for item in list:
        resp = requests.post(url=, json=item)
        if resp.status_code != 201:
            raise Exception('POST error status={}'.format(resp.status_code))
        print('Created feedback ID: {}'.format(resp.json()["id"]))


if __name__ == "__main__":
    # code that runs only when the file is executed directly

    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", default="/data/feedback/")
    parser.add_argument("--ip", default="127.0.0.1")
    parser.add_argument("--port", default="80")
    args = parser.parse_args()

    send_reviews(args.dir, args.ip, args.port)
