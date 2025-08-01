from communication import SmsSender


class TestableSmsSender(SmsSender):
    def __init__(self):
        super().__init__()
        self._send_called = False

    def send(self, schedule):
        print("Test용에서 send 실행")
        self._send_called = True

    @property
    def send_called(self) -> bool:
        return self._send_called
