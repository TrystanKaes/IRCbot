## BASIC IRC BOT

This bot currently checks each message received in the chat for the list of banned words and if the 'chatter' uses banned words, reprimands them. It also tracks a trailing time range of chat messages and updates the list in real time. If the user spams chat, it reprimands them.


### File Structure
* [bot.py](./bot.py)
  * To Run: 'python3 bot.py'
* [IRC_bot.py](./IRC_bot.py)
  * IRC class handles all discussion with the server.
* [functions.py](./functions.py)
  * Contains auxillary functions that are used in bot.py.
* [workers.py](./workers.py)
  * Contains class definitions for all multithreaded workers.
* [BANNED_WORDS](./BANNED_WORDS)
  * This is self explanatory.
