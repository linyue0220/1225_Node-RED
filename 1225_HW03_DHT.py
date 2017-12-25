[
    {
        "id": "2ebe6d92.0452b2",
        "type": "inject",
        "z": "19811d99.8e80d2",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "x": 110,
        "y": 160,
        "wires": [
            [
                "eef871ba.8d657"
            ]
        ]
    },
    {
        "id": "eef871ba.8d657",
        "type": "function",
        "z": "19811d99.8e80d2",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey: \"Sj30Beaw0VrZv973\"\n};\n\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 240,
        "y": 200,
        "wires": [
            [
                "8d110aab.278ae8",
                "56cc65b7.6ad60c"
            ]
        ]
    },
    {
        "id": "7740a4ef.5b8ffc",
        "type": "http response",
        "z": "19811d99.8e80d2",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 570,
        "y": 220,
        "wires": []
    },
    {
        "id": "8d110aab.278ae8",
        "type": "http request",
        "z": "19811d99.8e80d2",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "url": "http://api.mediatek.com/mcs/v2/devices/DYG8620y/datachannels/Temperature/datapoints.csv",
        "tls": "",
        "x": 370,
        "y": 240,
        "wires": [
            [
                "7740a4ef.5b8ffc",
                "a8c0e2e0.30e16"
            ]
        ]
    },
    {
        "id": "a8c0e2e0.30e16",
        "type": "debug",
        "z": "19811d99.8e80d2",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 590,
        "y": 180,
        "wires": []
    },
    {
        "id": "56cc65b7.6ad60c",
        "type": "http request",
        "z": "19811d99.8e80d2",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "url": "http://api.mediatek.com/mcs/v2/devices/DYG8620y/datachannels/Humidity/datapoints.csv",
        "tls": "",
        "x": 370,
        "y": 160,
        "wires": [
            [
                "a8c0e2e0.30e16",
                "7740a4ef.5b8ffc"
            ]
        ]
    }
]
