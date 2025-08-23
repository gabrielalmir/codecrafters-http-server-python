from . import server

DEFAULT_HOST = "localhost"
DEFAULT_PORT = 4221

def main(host = DEFAULT_HOST, port = DEFAULT_PORT):
    print(f"Server listing at {host}:{port}")
    conn, address = server.listen(host, port)

    with conn:
        data = server.parse_request(conn)
        print(f'Connection accepted from {address}')
        server.route(conn, data.target)

if __name__ == "__main__":
    main()
