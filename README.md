## IRC BOT

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
* [cleanData.py](./cleanData.py)
   * Simple script to clean data and generate a list of words to be banned
* [BANNABLE_WORDS](./BANNABLE_WORDS)
  * List of words that can be banned.
* [BANNED_WORDS](./BANNED_WORDS)
  * The list included in BANNABLE_WORDS and all associated leet speach.

### Housekeeping
cleanData.py reads from BANNABLE_WORDS, removes duplicates, generates associated leetspeech phrases,
and writes out to BANNED_WORDS. If you want to add new phrases or words to ban, add them to the end of BANNABLE_WORDS
and then run [cleanData.py](./cleanData.py). They will be sorted,added, and associated leetspeach words will be added.

If you have any questions please reach out to me.
