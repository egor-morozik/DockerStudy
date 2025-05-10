Creat image with Flask-app(app.py) that use redis to use set and get values operation in DB (redis) that run in another container
Start network with docker network create app-network
Than start redis container: docker run -d --name redis --network app-network redis
Start app container: docker run -d --name flask --network app-network -p 5000:5000 my-app-with-redis
And test with:

curl http://localhost:5000/set/mykey/myvalue


StatusCode        : 200
StatusDescription : OK
Content           : Set mykey = myvalue
RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 19
                    Content-Type: text/html; charset=utf-8
                    Date: Sat, 10 May 2025 09:01:36 GMT
                    Server: Werkzeug/2.3.8 Python/3.9.22

                    Set mykey = myvalue
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 19], [Content-Type, text/html;
                    charset=utf-8], [Date, Sat, 10 May 2025 09:01:36 GMT]...}
Images            : {}
InputFields       : {}                                                                                  Links             : {}                                                                                  ParsedHtml        : mshtml.HTMLDocumentClass                                                            RawContentLength  : 19                                                                                  



curl http://localhost:5000/get/mykey


StatusCode        : 200
StatusDescription : OK
Content           : mykey = myvalue
RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 15
                    Content-Type: text/html; charset=utf-8
                    Date: Sat, 10 May 2025 09:01:47 GMT
                    Server: Werkzeug/2.3.8 Python/3.9.22

                    mykey = myvalue
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 15], [Content-Type, text/html;
                    charset=utf-8], [Date, Sat, 10 May 2025 09:01:47 GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 15