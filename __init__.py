from mycroft import MycroftSkill, intent_file_handler


class Echo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('echo.intent')
    def handle_echo(self, message):
        self.speak_dialog('echo')


def create_skill():
    return Echo()

