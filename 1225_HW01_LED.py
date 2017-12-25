[
    {
        "id": "a2e2506.213fab",
        "type": "rpi-gpio out",
        "z": "1bc06896.fee267",
        "name": "GREEN LED",
        "pin": "11",
        "set": true,
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 350,
        "y": 280,
        "wires": []
    },
    {
        "id": "9e9956f0.75fbb8",
        "type": "inject",
        "z": "1bc06896.fee267",
        "name": "On",
        "topic": "",
        "payload": "1",
        "payloadType": "str",
        "repeat": "",
        "crontab": "",
        "once": false,
        "x": 110,
        "y": 240,
        "wires": [
            [
                "a2e2506.213fab",
                "9ccd8e93.d8349"
            ]
        ]
    },
    {
        "id": "8ca8d1a8.9c46f",
        "type": "inject",
        "z": "1bc06896.fee267",
        "name": "Off",
        "topic": "",
        "payload": "0",
        "payloadType": "str",
        "repeat": "",
        "crontab": "",
        "once": false,
        "x": 110,
        "y": 320,
        "wires": [
            [
                "a2e2506.213fab",
                "9ccd8e93.d8349"
            ]
        ]
    },
    {
        "id": "9ccd8e93.d8349",
        "type": "debug",
        "z": "1bc06896.fee267",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "payload",
        "x": 350,
        "y": 200,
        "wires": []
    }
]
