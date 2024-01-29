"""
LolzteamApi it's library that contains all the methods of the Lolzteam API (Market/Forum/Antipublic)

You can find full documentation here -> https://github.com/AS7RIDENIED/Lolzteam_Python_Api
"""

import os, platform


if platform.system() == "Windows":
    path = os.getenv("APPDATA") + "/LolzteamApi.txt"
    if os.path.exists(path):    
        with open(path, "r") as f:
            count = int(f.read())
        if count >= 1:
            with open(path, "w") as f:
                f.write(str(count - 1))
    else:
        with open(path, "w") as f:
            f.write("9")
            count = 10
    if count == 0:
        pass
    else:
        message = f"""

This message will be shown {count-1} more times

The library got a major refactoring and changed it's name in the process. The library that you are currently using will no longer be updated
To get more information, follow the link and see the pinned post -> https://zelenka.guru/threads/5523020/

"""
        print(message)
else:
    username = os.getlogin()
    path = f"/home/{username}/Documents/LolzteamApi.txt"
    if os.path.exists(path):
        with open(path, "r") as f:
            count = int(f.read())
        if count >= 1:
            with open(path, "w") as f:
                f.write(str(count - 1))
    else:
        with open(path, "w") as f:
            f.write("9")
            count = 10
    if count == 0:
        pass
    else:
        message = f"""

This message will be shown {count-1} more times

The library got a major refactoring and changed it's name in the process. The library that you are currently using will no longer be updated
To get more information, follow the link and see the pinned post -> https://zelenka.guru/threads/5523020/

"""
        print(message)


from . import LolzteamExceptions
from .LolzteamApi import LolzteamApi
from .AntipublicApi import AntipublicApi
from .DelaySynchronizer import DelaySynchronizer
from .BBCODE import BBCODE
from . import Types
