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