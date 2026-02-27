# import socket;
# from urlib.parse import urlparse;
# from urlib.parse import parse_qs;
# from datetime import datetime;
# HOST='127.0.0.1'
# PORT=8000


# def build_response(status_code,body, content_type='text/html'):
#     status_messages={
#         200:"OK",
#         404:'NOT FOUND',
#         500:'INTERNAL SERVER ERROR'
#     }

#     status_line=f"HTTP/1.1 {status_code} {status_messages[status_code]}\r\n"

#     headers = (
#         f"Date: {datetime.utcnow()}\r\n"
#         f"Server: CustomPythonSocketServer\r\n"
#         f"Content-Type: {content_type}\r\n"
#         f"Content-Length: {len(body.encode())}\r\n"
#         f"Connection: close\r\n"
#         "\r\n"
#     )
    
#     return (status_line+headers+body).encode()


# def handle_request(request):
#     lines = request.split("\r\n")
#     request_line = lines[0]

#     try:
#         youmethod, path, version =request_line.split()
#     except:
#         return build_response(400, "<h1>400 Bad Request</h1>")
    
#     parsed_url=urlparse(path)
#     route=parsed_url.path
#     query_params=parse_qs(parsed_url.query)

#     if route=='/':
#         body='''        <html>
#             <body>
#                 <h1>Home Page</h1>
#                 <p>Try /about or /hello?name=Muqeet</p>
#             </body>
#         </html>
#         '''
#         return build_response(200,body)
#     elif route=='/about':
#         body="""
#         <html>
#             <body>
#                 <h1>About Page</h1>
#             </body>
#         </html>
#         """

#         return  build_response(200,body)
    
#     elif route=='/hello':
#         name = query_params.get("name", ["Guest"])[0]
#         body = f"""
#         <html>
#             <body>
#                 <h1>Hello, {name} 👋</h1>
#             </body>
#         </html>
#         """
#         return build_response(200, body)

#     else:
#         return build_response(404, "<h1>404 Not Found</h1>")
    

#     def start_server():
#         server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#         server_socker.bind((HOST,PORT))
#         server_socket.listen(5) 
#         print(f"Server running on http://{HOST}:{PORT}")

#         while True:
#         client_socket, address = server_socket.accept()
#         print(f"Connection from {address}")

#         request = client_socket.recv(4096).decode()
#         print("----- REQUEST -----")
#         print(request)

#         response = handle_request(request)

#         client_socket.sendall(response)
#         client_socket.close()


# if __name__ == "__main__":
#     start_server()





import socket
from urllib.parse import urlparse, parse_qs
from datetime import datetime

HOST = "127.0.0.1"
PORT = 8080

def build_response(status_code, body, content_type="text/html"):
    status_messages = {
        200: "OK",
        404: "Not Found",
        400: "Bad Request"
    }

    status_line = f"HTTP/1.1 {status_code} {status_messages[status_code]}\r\n"

    headers = (
        f"Date: {datetime.utcnow()}\r\n"
        f"Server: CustomPythonSocketServer\r\n"
        f"Content-Type: {content_type}\r\n"
        f"Content-Length: {len(body.encode())}\r\n"
        f"Connection: close\r\n"
        "\r\n"
    )

    return (status_line + headers + body).encode()


def handle_request(request_text):
    lines = request_text.split("\r\n")
    request_line = lines[0]

    try:
        method, path, version = request_line.split()
    except:
        return build_response(400, "<h1>400 Bad Request</h1>")

    parsed_url = urlparse(path)
    route = parsed_url.path
    query_params = parse_qs(parsed_url.query)

    if route == "/":
        body = """
        <html>
            <body>
                <h1>Home Page</h1>
                <p>Try /about or /hello?name=Muqeet</p>
            </body>
        </html>
        """
        return build_response(200, body)

    elif route == "/about":
        body = """
        <html>
            <body>
                <h1>About Page</h1>
            </body>
        </html>
        """
        return build_response(200, body)

    elif route == "/hello":
        name = query_params.get("name", ["Guest"])[0]
        body = f"""
        <html>
            <body>
                <h1>Hello, {name} 👋</h1>
            </body>
        </html>
        """
        return build_response(200, body)

    else:
        return build_response(404, "<h1>404 Not Found</h1>")


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"Server running on http://{HOST}:{PORT}")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address}")

        request = client_socket.recv(4096).decode()
        print("----- REQUEST -----")
        print(request)

        response = handle_request(request)

        client_socket.sendall(response)
        client_socket.close()


if __name__ == "__main__":
    start_server()