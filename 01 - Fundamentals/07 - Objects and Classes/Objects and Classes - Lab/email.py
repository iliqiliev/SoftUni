class Email:

    def __init__(self, sender: str, receiver: str, content: str) -> None:
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self) -> None:
        self.is_sent = True

    def get_info(self) -> str:
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


# messages is a list of Email objects that are created by iterating over
# the input until the word "Stop". each info is split into the 3 arguments
# of the Email object with the unpacking operator *
messages = [Email(*info.split()) for info in iter(input, "Stop")]

# call the send method for every object index in the list comprehension below
for index in [int(index) for index in input().split(", ")]:
    messages[index].send()

for message in messages:
    print(message.get_info())
