import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.js': 'application/javascript; charset=utf-8',
    '.json': 'application/json; charset=utf-8',
    '.html': 'text/html; charset=utf-8',
    '': 'application/octet-stream',
})

httpd = socketserver.TCPServer(("", PORT), Handler)
print(f"Serving HTTP on http://localhost:{PORT}")
httpd.serve_forever()
