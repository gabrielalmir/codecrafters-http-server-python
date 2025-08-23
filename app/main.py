import server

API_HOST = "localhost"
API_PORT = 4221

def main():
    print("Server listing at localhost:4221")

    client, address = server.listen(API_HOST, API_PORT)
    data = server.parse_request(client)

    print(f'Connection accepted from {address}')
    server.route(client, data.target)

if __name__ == "__main__":
    main()
