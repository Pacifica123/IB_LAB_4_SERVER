import asyncio
import socket

HOST = '127.0.0.1'
PORT = 65432


# TODO : перенсти в Observer
async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f'Подключение от {addr}')

    while True:
        data = await reader.read(100)
        if not data:
            break
        message = data.decode()
        print(f'Получено сообщение: {message} от {addr}')
        writer.write(data)
        await writer.drain()


async def start():
    server = await asyncio.start_server(handle_client, HOST, PORT)
    addr = server.sockets[0].getsockname()
    print(f'Сервер слушает на {addr}')

    async with server:
        await server.serve_forever()

