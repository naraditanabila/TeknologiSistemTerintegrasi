
# coding: utf-8

# In[ ]:


from http.server import HTTPServer, BaseHTTPRequestHandler
import base64
import ssl

USERS = [
    {
        "username": "test",
        "password": "test",
        "hash": base64.b64encode("test:test".encode('utf-8'))/decoe('utf-8')
    }
]

class AuthHandler(BaseHTTPRequestHandler):
    def require_auth(self):
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="dita site\r\n\r\n"')
        self.end_headers()
        
    def do_GET(self):
        auth = self.headers['Authorization']
        if not auth:
            return self.require_auth()
        
        hash_val = auth.split(' ')[1]
        for user in USERS:
            if user['hash'] == hash_val:
                self.send_response(200)
                self.end_headers()
                self.wfile.write("<html><body>Hi, {}!</body></html>".format(user['username']).encode('utf-8'))
                return
            
            return self.require_auth()
        
    if __name__ == "__main__":
        server_address = ("0.0.0.0",8883)
        httpd = HTTPServer(server_address, AuthHandler)
        httpd.socket = ssl.wrap_socket (httpd.socket,
            keyfile="/Users/naraditanabila/Documents/python/data/key.pem",
            sertfile='/Users/naraditanabila/Documents/python/data/certificate.pem',server_side=True)
        httpd.serve_forever()

