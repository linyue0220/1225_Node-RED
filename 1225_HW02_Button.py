[
    {
        "id": "db896933.0566f8",
        "type": "rpi-gpio in",
        "z": "753c5949.52c9f8",
        "name": "Button",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": true,
        "x": 110,
        "y": 160,
        "wires": [
            [
                "f344d40a.099148",
                "fd5a1c58.97b3a"
            ]
        ]
    },
    {
        "id": "9efc9f60.f76c6",
        "type": "rpi-gpio out",
        "z": "753c5949.52c9f8",
        "name": "GREEN LED",
        "pin": "11",
        "set": true,
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 630,
        "y": 180,
        "wires": []
    },
    {
        "id": "f344d40a.099148",
        "type": "debug",
        "z": "753c5949.52c9f8",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "payload",
        "x": 450,
        "y": 120,
        "wires": []
    },
    {
        "id": "fd5a1c58.97b3a",
        "type": "switch",
        "z": "753c5949.52c9f8",
        "name": "if input is 1",
        "property": "payload",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "1",
                "vt": "str"
            },
            {
                "t": "else"
            }
        ],
        "checkall": "true",
        "outputs": 2,
        "x": 270,
        "y": 180,
        "wires": [
            [
                "9d91b76f.e58938"
            ],
            [
                "62e5b413.b5725c"
            ]
        ]
    },
    {
        "id": "9d91b76f.e58938",
        "type": "change",
        "z": "753c5949.52c9f8",
        "name": "Change to 0",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "0",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 450,
        "y": 160,
        "wires": [
            [
                "9efc9f60.f76c6"
            ]
        ]
    },
    {
        "id": "62e5b413.b5725c",
        "type": "change",
        "z": "753c5949.52c9f8",
        "name": "Change to 1",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "1",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 450,
        "y": 200,
        "wires": [
            [
                "9efc9f60.f76c6"
            ]
        ]
    }
]
