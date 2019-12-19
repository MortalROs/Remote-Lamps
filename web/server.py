import BaseHTTPServer, SimpleHTTPServer
import ssl

ssl_key = "SSL KEY PATH"
ssl_certificate = "SSL CERTIFICATE PATH"

httpd = BaseHTTPServer.HTTPServer(('0.0.0.0', 80), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, keyfile=ssl_key, certfile=ssl_certificate, server_side=True)
httpd.serve_forever()
