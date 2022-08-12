# scanner

#### Simple scanner to scan ports
- Usecase:

- This will show a help menu
```
 python3 scan_port.py -h
 or
 python3 scan_port.py --help

```

- Use this flag to pass ip (required)
```
 python3 scan_port.py -i 192.168.0.1
 or
 python3 scan_port.py --ip mysite.com

```

- Use this flag to pass port as argument ou a number of ports (not required)
- If don't pass any port, it will scan all possbile ports
```
 python3 scan_port.py -i 192.168.0.1 -p 192.168.0.1 -p 80
 or
 python3 scan_port.py  --ip mysite.com --port 21 22 25 80 8080

```

### The output will be something like this
```
-------------------------------------------------------
    ____  ____  ____  ___________ _________    _   __
   / __ \/ __ \/ __ \/_  __/ ___// ____/   |  / | / /
  / /_/ / / / / /_/ / / /  \__ \/ /   / /| | /  |/ / 
 / ____/ /_/ / _, _/ / /  ___/ / /___/ ___ |/ /|  /  
/_/    \____/_/ |_| /_/  /____/\____/_/  |_/_/ |_/   
                                                     


                     SCANNING PORTS

-------------------------------------------------------
|       PORTS                               STATUS    |
-------------------------------------------------------
|       Port 80                             [OPEN]    |
|       Port 21                             [OPEN]    |
|       Port 22                             [OPEN]    |
-------------------------------------------------------

```
