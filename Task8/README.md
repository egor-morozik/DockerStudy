Use docker compose to build app with flask-app container, redis container, and network for it connetion
Start container with: docker-compose up --build
Test with: curl http://localhost:5000/get/unknown
GET: 
StatusCode        : 200                                                                                     
StatusDescription : OK                                                                                      
Content           : unknown = None                                                                          
RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 14
                    Content-Type: text/html; charset=utf-8
                    Date: Sat, 10 May 2025 09:40:50 GMT
                    Server: Werkzeug/2.3.8 Python/3.9.22

                    unknown = None
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 14], [Content-Type, text/html; charset=utf-8],   
                    [Date, Sat, 10 May 2025 09:40:50 GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 14