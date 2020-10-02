class GreetingCard:

    def __init__(self):
        self._recipient = "Dana Ev"
        self._sender = "Eyal Ch"

    def greeting_msg(self):
        print(f"To: {self._recipient}, From: {self._sender}")


