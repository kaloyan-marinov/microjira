# Set up the project

```
$ python3 --version
Python 3.8.3

$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install --upgrade pip
(venv) $ pip install -r requirements.txt
```

# Serve the application and issue requests to it

```
# Launch one terminal instance and, in it, start serving the application:

(venv) $ FLASK_APP=application.py flask run
```

```
# Launch a second terminal instance and, in it, issue a request to the application:

$ curl \
    --verbose \
    localhost:5000 \
    | json_pp

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying ::1...
* TCP_NODELAY set
* Connection failed
* connect to ::1 port 5000 failed: Connection refused
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> GET / HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.64.1
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 27
< Server: Werkzeug/2.0.2 Python/3.8.3
< Date: Wed, 10 Nov 2021 12:11:49 GMT
< 
{ [27 bytes data]
100    27  100    27    0     0   3000      0 --:--:-- --:--:-- --:--:--  3000
* Closing connection 0
{
   "message" : "Hello World!"
}
```