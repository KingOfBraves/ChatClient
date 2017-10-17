from MyWrappers import test_wrapper

#Holds information about the chatlog
class ChatLog():

    def __init__(self, height):
        self.height = height
        self.log = []


    def add_chat(self, user, chat):
        self.log.append({"user" : user,
                      "chat" : chat})

    def get_latest_chat(self):
        return self.log[-self.height:]


#User class holds the values for the user
class User():

    def __init__(self, username):
        self.username = username

    def __str__(self):
        return self.username

    def update_username(self, username):
        self.username = username


@test_wrapper
def update_chatlog(chatlog, user, input):
    chatlog.add_chat(str(user), input)


@test_wrapper
def print_chatlog(chatlog):
    for log in chatlog.get_latest_chat():
        print(log['user'] + ": " + log['chat'])


def test_chatlog():
    chat = ChatLog(3)
    user = User("Chad")
    print chat
    update_chatlog(chat, user, "Test 1")
    print_chatlog(chat)
    update_chatlog(chat, user, "Test 2")
    update_chatlog(chat, user, "Test 3")
    print_chatlog(chat)
    update_chatlog(chat, user, "Test 4")
    update_chatlog(chat, user, "Test 5")
    print_chatlog(chat)


if __name__ == '__main__':
    test_chatlog()
