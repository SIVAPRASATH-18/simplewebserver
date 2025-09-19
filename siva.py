from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
       
    </head>
    <body>
        <h1 align="center"> Device Specification-25016007 </h1>
        <table border="4" align="center" >
            <tr>
                <th>S.NO.</th>
                <th>device specification</th>
                <th>details</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Lenovo LOQ</td>
                <td>12GB RAM , 512GB SSD</td>
            </tr>
            <tr>
                <td>2</td>
                <td>acer</td>
                <td>16GB RAM ,512GB SSD</td>
            </tr>
            <tr>
                <td>3</td>
                <td>HP</td>
                <td>12GB ram,1tb ssd</td>
            </tr>
            <tr>
                <td>4</td>
                <td>asus</td>
                <td>8gb RAM,512GB SSD</td>
            </tr>
            <tr>
                <td>5</td>
                <td>lenovo thinkpad</td>
                <td>12GB RAM,512GB SSD</td>
            </tr>
        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()