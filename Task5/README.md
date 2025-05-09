Creat image with Flask-app(app.py) and run container 
docker run -p 6000:5000 my-python-flask-app (bound host port 6000 to container port 5000) 
Check work in terminal:

curl http://localhost:6000

return:

StatusCode        : 200
StatusDescription : OK
Content           : Hello, Flask!
RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 13
                    Content-Type: text/html; charset=utf-8
                    Date: Fri, 09 May 2025 18:17:51 GMT
                    Server: Werkzeug/2.3.8 Python/3.9.22

                    Hello, Flask!
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 13], [Content-Type, text/html;
                    charset=utf-8], [Date, Fri, 09 May 2025 18:17:51 GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 13
