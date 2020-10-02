from Gcard import GreetingCard


class BirthdayCard(GreetingCard):

    def __init__(self):
        GreetingCard.__init__(self)
        self._sender_age = 0

    def greeting_msg(self):
        GreetingCard.greeting_msg(self)
        print(f"Happy {self._sender_age} Birthday!")