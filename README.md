# Python Server Implementations

Various ways to create a Flask/non-Flask Server

_These tasks were created and solved by me._

Create a web app that handles the 3 tasks mentioned

The following consumes form data and returns text/html

- Python_Flask_Pure --> Runs as General Web Server -- Consumes any data

The following servers consume JSON data and returns JSON (therefore input curl args will differ to example)

- Python_Flask_Pure_API --> Runs as API that returns JSON
- Python_Flask_Connexion --> Runs as API that returns JSON
- Python_Flask_RestfulAPI --> Runs as API that returns JSON
- Python_FastAPI --> Runs as API that returns JSON

---

<br>

1. Only accepts GET Req, gives 405 on other methods

- 1a. on /hello endpoint, accepts only 1 incoming query parameter ("message") and returns the message

- 1b. if no query param or more than 1, return 400

```
$ curl -v http://127.0.0.1:4004/hello?message=Test
> GET /echo?message=Test HTTP/1.1
< HTTP/1.0 200 OK
< Content-Type: text/html; charset=utf-8
< Content-Length: 4
<
Test
```

---

<br>

2. A POST req to /tests endpoint with a body of set_message=Hello World and return nothing

- 2a. Must be authenticated using basic auth via header, return 401 if auth provided but incorrect

- 2b. if no authentication sent, return 401

- 2c. if not a POST req, return 405

- 2d. if no param or more than 1 param given in body, reject with 400

- 2e. after correctly sending to a req to this endpoint, set_message value should be returned in the header to responses to /hello endpoint

```
NAME=username
PASSWORD=password
cred="$( echo $NAME:$PASSWORD | base64 )"; curl -H "Authorization: Basic $cred"

$ curl -v -H "Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=" -d "set_message=Hello World" http://127.0.0.1:4004/tests
> POST /tests HTTP/1.1
> Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
> Content-Length: 12
> Content-Type: application/x-www-form-urlencoded
< HTTP/1.0 200 OK
< Content-Type: text/html; charset=utf-8
< Content-Length: 0
<
```

```
curl -H "Content-Type: application/json" -d '{"set_message":"Hello World"}' http://127.0.0.1:4004/tests
```

After Setting the set_message, the req and response to /hello will look like

```
$ curl -v http://127.0.0.1:4004/hello?message=Test
> GET /echo?message=Test HTTP/1.1
< HTTP/1.0 200 OK
< Content-Type: text/html; charset=utf-8
< Content-Length: 4
< set_message: Hello World
<
Test
```

---

<br>
3. A PUT req to /fixes/id/1 endpoint with a body of your choosing (Including set_message) and return everything submitted with a 201

- 3a. Must be authenticated via OAuth 2, return 401 if auth provided but incorrect
- 3b. if no authentication sent, return 403
- 3c. if not a PUT req, return 405
- 3d. if req is to the wrong id number, return 400
- 3e. if no data is provided, return a 400 error
- 3e. after correctly sending a req to this endpoint, If value of set_message is False or empty, header should not appear in response to /hello endpoint, otherwise it should.

```
$ curl -v -X PUT -H "Authorization: <OAuth_ACCESS_TOKEN>" -d "set_message=Hello World" -d "mymessage=sending req" -d "flask_app=True" http://127.0.0.1:4004/fixes/id/1
> POST /tests HTTP/1.1
> Authorization: OAuth <ACCESS_TOKEN>
> Content-Length: 12
> Content-Type: application/x-www-form-urlencoded
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: XXX
<
{"mymessage":"sending req", "flask_app":"True"}
```

# Env file

Create a `.env` file in each Python Directory as needed

```bash
# Example Env File Contents

BASIC_AUTHENTICATION="Basic dXNlcm5hbWU6cGFzc3dvcmQ="
OAUTH_AUTHENTICATION="Bearer eyJzdWIiOiJqYW5lZG9lQGV4YW1wbGUuY29tIiwibmFtZSI6IkphbmUgRG9lIiwiaWF0IjoxNTQ2MzAwODAwLCJleHAiOjE4OTM0NTYwMDB9"
```
