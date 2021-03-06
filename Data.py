from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

You can use me to manage channels with tons of features. Use below buttons to learn more !

By @KGN_BOTS
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="ð  Êá´á´á´ÊÉ´ Êá´á´á´ ð ", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("â¨ sá´á´á´á´Êá´ â¨", url="https://t.me/KGN_OFFICIAL")],
        [
            InlineKeyboardButton("Êá´Êá´â", callback_data="help"),
            InlineKeyboardButton("ðª á´Êá´á´á´ ðª", callback_data="about")
        ],
        [InlineKeyboardButton("ð¤á´á´á´á´á´á´s", url="https://t.me/KGN_BOTS")],
    ]

    # Help Message
    HELP = """
Everything is self explanatory after you add a channel.
To add a channel use keyboard button 'Add Channels' or alternatively for ease, use `/add` command

â¨ **Available Commands** â¨

/about - About The Bot
/help - This Message
/start - Start the Bot

Alternative Commands
/channels - List added Channels
/add - Add a channel
/report - Report a Problem
    """

    # About Message
    ABOUT = """
**About This Bot** 

A telegram channel automation bot by @KGN_BOTS

Source Code : [Click Here](https://t.me/KGN_OFFICIAL)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : [ZAHID](https://t.me/KGN_OFFICIAL)
    """
