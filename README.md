# RFID Web Authentication

Team Members: Miles Kirkbride, Will Bradley

## 1. Start frontend

Install node/npm:

https://nodejs.org/en/download/package-manager

Install dependencies:

```bash
'npm install'
```

Reconfigure IP addresses as needed. 

Serve webpage:

```bash
'npm start'
```

## 2. Start backend server

Install dependencies into a venv:

```bash
'pip3 install flask' 
'pip3 install flask_cors'
'pip3 install cryptography'
'pip3 install json'
'pip3 install requests'
'pip3 install sqlite3'
```

Reconfigure IP addresses as needed. 

Start server:

```bash
'python3 server.py'
```


## 3. Run rpi driver script

Install dependencies into a venv:

```bash
'pip3 install mfrc522'
'pip3 install cryptography'
'pip3 install json'
'pip3 install requests'
'pip3 install pprint'
```

Reconfigure IP addresses as needed. 

Run script:

```bash
'python3 rpi_driver.py'
```

## List of all libraries/frameworks

### Rpi:

    Python libraries
    - mfrc522
    - cryptography
    - json
    - requests
    - pprint


### Frontend:

    Frameworks
    - Node.js
    - React.js
    - Tailwind.css

    Npm packages
    - chart.js
    - react-chartjs-2
    - react-router-dom


### Backend:

    Database engine
    - Sqlite3

    Python libraries
    - flask
    - flask_cors
    - cryptography
    - requests

