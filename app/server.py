import asyncio
import socket

from app.observer_pattern import Subject, Observer

HOST = '127.0.0.1'
PORT = 65432

chat_server = Subject()


async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f'Подключение от {addr}')

    client_name = await reader.read(100)
    client_name = client_name.decode().strip()
    chat_client = Observer(client_name)

    chat_server.make_online(chat_client)

    while True:
        data = await reader.read(100)
        if not data:
            break
        message = data.decode().strip()
        print(f'Получено сообщение: {message} \n\n от {addr}')
        print('-----------------------------------------------')
        chat_server.notify(f"{client_name}: {message}")
    chat_server.make_offline(chat_client)
    writer.close()


async def start():
    server = await asyncio.start_server(handle_client, HOST, PORT)
    addr = server.sockets[0].getsockname()
    print(f'Сервер слушает на {addr}')

    async with server:
        await server.serve_forever()

