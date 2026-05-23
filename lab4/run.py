#! /usr/bin/env python3

import os 
import requests
import argparse

def send_descriptions(basepath, ip, port):

    folder = os.listdir(basepath)

    list = []

    for file in folder:
        with open(basepath + file, 'r') as f:
            list.append({"name": f.readline().rstrip("\n"),
            		"weight": int(f.readline().rstrip("\n").rsplit(" lbs", 1)[0]),
            		"description": f.readline().rstrip("\n"),
            		"image_name": file.rsplit(".", 1)[0] + ".jpeg"
            		})

    url = 'http://' + ip + ':' + port + '/feedback/'
    for item in list:
        resp = requests.post(url, json=item)


if __name__ == "__main__":
    # code that runs only when the file is executed directly

    basedir = os.getcwd() + '/supplier-data/descriptions/'
#    basedir = os.path.expanduser("~") + '/supplier-data/descriptions/'

    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", default=basedir)
    parser.add_argument("--ip", default="127.0.0.1")
    parser.add_argument("--port", default="80")
    args = parser.parse_args()

    send_descriptions(args.dir, args.ip, args.port)
