class HelloPy:
    def __init__(self, username) -> None:
        self.user = username

    def sayHello(self):
        print(f"Hello {self.user}!")

    def goodMorning(self):
        print(f"Good Morning {self.user}!")
