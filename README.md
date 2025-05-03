# minecraft-rcon-discord-bot
This is basically a fork of https://github.com/RayNieport/mconBot, a bit updated, and with better "security" (made in collaboration with ChatGPT ;).

## Main changes from the original mconBot:
 - i've only "moved over" the simple python version, not the docker image
 - main python file a bit updated for discord's new standards (this means adding the init shit)
 - removing commands.json, now the bot just runs whatever command you give it, no different role management (user, mod, admin)
 - now using the /send slash command (with ephemeral response)
 - insted of role names, now using discord user IDs

## General description (from mconBot):
mconBot allows you and your friends to easily control your Minecraft server from the comfort of Discord!
Minecraft servers use a protocol called __[RCON](https://wiki.vg/RCON)__ to accept remote commands. If you're hosting your own server, you may have seen RCON mentioned in the server.properties file.

However, using RCON has some issues:
1. Port forwarding RCON to control your server over the internet is not very secure.
2. The RCON "user" has permission to run the full suite of Minecraft __[commands](https://minecraft.wiki/w/Commands)__, without any restrictions.
3. There is only one RCON "user", so your friends can't log in to moderate the server unless you give them the credentials for unrestricted RCON access.

To solve these problems, mconBot does the following:
1. Uses Discord as an interface to eliminate the need for port forwarding or a VPN (mconBot is intended to be hosted on the same LAN as your Minecraft server). 
2. Solves permission issues using a three-tiered system of Users, Moderators, and Administrators. Higher tiers allow more sensitive commands to be executed.

### How does it work:
__First__, enable RCON by editing the __[server.properties](https://minecraft.wiki/w/Server.properties)__ file of your Minecraft server:
```
enable-rcon=true
rcon.password=<your passord>
rcon.port=25575
broadcast-rcon-to-ops=<optional, true|false>
```
__Second__, clone the git respository to the machine you want to run the bot on:
```
git clone https://github.com/w4sb0y/minecraft-rcon-discord-bot
```

__Third__, install __[python 3](https://www.python.org/downloads/)__ , then navigate to the cloned repository and install the necessary dependencies:
```
pip3 install -r requirements.txt
```

__Fourth__, create your instance of the bot at the __[Discord Developer Portal](https://discord.com/developers/applications)__:

__Fifth__, modify __mconBot/src/.env__ in the cloned repository:
1. Paste the Discord Token aquired above into the appropriate field.
2. Fill in your Minecraft server's IP and RCON password. If you're not using the default RCON port (25575), you can also change that.
3. Change the discord user ID(s) to be able to use the bot.

__Sixth__, head into __src/__ in the cloned repository and start up the bot:
```
python3 bot.py
```



# Some example images:

![img](https://zip.xd.hu/file/1Nc48G.png)
![img](https://zip.xd.hu/file/uDvVge.png)
![img](https://zip.xd.hu/file/Rn5Rmv.png)
![img](https://zip.xd.hu/file/MrnDOU.png)
![img](https://zip.xd.hu/file/wHHk9Q.png)

