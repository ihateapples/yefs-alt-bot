import discord

ihateapples_id = "1102729020526829628" # so basically right here you put the id of the person you want to control the bot. not really a selfbot if u think of it like that, but its something.

class YefClient(discord.Client):
    async def on_ready(self):
        print('Yefing in as', self.user)

    async def on_message(self, message):
        author_id = str(message.author.id)
        
        if author_id == ihateapples_id:
            if message.content == '>random':
                await message.channel.send('Embrace the yef with a random Garfield comic: https://gocomics.com/random/garfield') # you can change these commands if you want i actually dont really care.
            elif message.content == '>help':
                yef_message = """
                **Commands**
                > `❓` | **>help**: Summon the mighty Yef guide.
                > `🐈` | **>random**: Inflict a Garfield comic upon the world.
                > `🏓` | **>ping**: Challenge the bot's yefic latency.
                """
                await message.channel.send(yef_message)
            elif message.content == '>ping':
                latency = round(self.latency * 1000)  # Convert to yefiseconds
                await message.channel.send(f'Yef! Bot latency is {latency}ms')

yef_client = YefClient()
token = 'discord-token-here' # replace discord-token-here with your actual discord token. not really yours i recommend using an alternative account. 2 actually. for the controller account and the selfbot account.
yef_client.run(token)
