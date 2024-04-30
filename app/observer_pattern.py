class Subject:
    def __init__(self):
        self.observers = []

    def make_online(self, observer):
        self.observers.append(observer)

    def make_offline(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        # TODO : отправка сообщения клиенту
        print(f'Пользователю {self.name} отправлено сообщение: {message}')


# class ChatServer(Subject):
#     def __init__(self):
#         super().__init__()
#         self.clients = []
#
#     def add_client(self, client):
#         self.clients.append(client)
#         self.attach(client)
#
#     def remove_client(self, client):
#         self.clients.remove(client)
#         self.detach(client)
#
#     def broadcast_message(self, message):
#         self.notify(message)


