""" Thanks to https://www.techbeamers.com/create-python-irc-bot/ for the tutorial this module comes from. """
import socket
import time

class IRC:

    irc = socket.socket()

    def __init__(self):
        # Define the socket
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, channel, msg):
        # Transfer data
        self.irc.send(bytes("PRIVMSG " + channel + " :" + msg + "\n", "UTF-8"))
    def quit(self, msg):
        # Quit bot
        self.irc.send(bytes("QUIT :" + msg + "\n", "UTF-8"))
    def connect(self, server, port, channel, botnick, botpass):
        # Connect to the server
        print("Connecting to: " + server)
        self.irc.connect((server, port))

        # Perform user authentication
        self.irc.send(bytes("USER " + botnick + " " + botnick +" " + botnick + " " + botnick + "\n", "UTF-8"))
        self.irc.send(bytes("NICK " + botnick + "\n", "UTF-8"))


        # join the channel
        self.irc.send(bytes("JOIN " + channel + "\n", "UTF-8"))

    def PONG():
        self.irc.send(bytes())

    def get_response(self):
        time.sleep(1)
        # Get the response
        resp = self.irc.recv(2040).decode("UTF-8")

        if resp.find("PING") != -1:
            self.irc.send(bytes("PONG :pingisn", "UTF-8"))

        return resp
