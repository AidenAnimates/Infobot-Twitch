from twitchio.ext import commands
import json
import random

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token='irc token', client_id='not used', nick='twitch name of the bot', prefix='prefix of your choice',
                         initial_channels=['streamer'])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)

    # Commands use a different decorator
    @commands.command(name='hello')
    async def my_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')
    
    @commands.command(name='channelamt')
    async def camt(self, ctx):
        await ctx.send(f'The channels that use me are: {self.initial_channels}')
    
    @commands.command(name='say')
    async def saythings(self, ctx, *, word = None):
        word = str(word)
        await ctx.send(word)
    
    @commands.command(name='lurk')
    async def lurk(self ,ctx):
        await ctx.send(f'{ctx.author.name}, Thank you for lurking!')
    
    @commands.command(name='bal')
    async def bal(self, ctx):
        await open_account(ctx.author.name)
        user = ctx.author.name
        users = await get_bank_data()
    
        wallet_amt = users[str(user)]["wallet"]
        bank_amt = users[str(user)]["bank"]
        inv_amt = users[str(user)]["Inventory"]
        
        
        await ctx.send(f"{ctx.author.name}'s balance, Wallet = {wallet_amt}, Bank = {bank_amt}, Tokens = {inv_amt}")
    
        with open("infobank.json","w") as f:
            json.dump(users,f)
    
    @commands.command(name='beg')
    async def beg(self, ctx):
        user = ctx.author.name
    
        users = await get_bank_data()
    
        earnings = random.randrange(329)
    
        negearnings = random.randrange(56)
    
        if earnings > negearnings:
            await ctx.send(f"A karen attempted to murder you, You pressed charges and got ${earnings}")
        else:
            await ctx.send(f"A karen murdered you, the karen got away with it and you got nothing.")
        if earnings > negearnings:
            users[str(user)]["wallet"] += earnings
        else:
            users[str(user)]["wallet"] += 0
        
        with open("infobank.json","w") as f:
            json.dump(users,f)
    
    @commands.command(name='shop')
    async def shop(self, ctx):
        await ctx.send("Shop: Token Of Epicness, id: tokenofepicness, Price: 10000")
    
    @commands.command(name='buy')
    async def buy(self, ctx, item = None):
        users = await get_bank_data()
        
        await open_account(ctx.author.name)
        
        item = str(item)
        
        if item == "tokenofepicness" and users[str(ctx.author.name)]["wallet"] > 10000:
            users[str(ctx.author.name)]["wallet"] -= 10000
            users[str(ctx.author.name)]["Inventory"] += 1
            await ctx.send('ok i guess you bought a token of epicness')
        
        with open("infobank.json","w") as f:
            json.dump(users,f)
    
    @commands.command(name='help')
    async def yesmannnn(self, ctx):
        await ctx.send(f"Commands are: " + ", ".join([c for c in bot.commands]))
    
    @commands.command(name='rob')
    async def rob(self,ctx,stateduser = None):
        users = await get_bank_data()
        
        await open_account(ctx.author.name)
        await open_account(stateduser)
        
        
        
        earnings = random.randrange(users[str(member.id)]["wallet"])
        oppoearnings = random.randrange(users[str(ctx.author.id)]["wallet"])
        
        luck = random.randrange(10)
        stateduser = str(stateduser)
        
        if luck > 5:
            users[str(ctx.author.name)]["wallet"] += earnings
            users[str(stateduser)]["wallet"] -= earnings
            await ctx.send(f"lol {ctx.author.name} robbed {humanfluushdljf} and got ${earnings}")
        if luck < 5:
            users[str(ctx.author.name)]["wallet"] -= oppoearnings
            users[str(stateduser)]["wallet"] += oppoearnings
            await ctx.send(f"lol {ctx.author.name} robbed {humanfluushdljf} and got caught, {ctx.author.name} lost ${oppoearnings}")
        
        with open("infobank.json","w") as f:
            json.dump(users,f)

    

async def get_bank_data():
    with open("infobank.json","r") as f:
        users = json.load(f)
    return users
   
async def open_account(user):
        
    users = await get_bank_data()
    
    if str(user) in users:
        return False
    else:
        users[str(user.name)] = {}
        users[str(user.name)]["wallet"] = 100
        users[str(user.name)]["bank"] = 0
        users[str(user.name)]["Inventory"] = 0
    
    with open("infobank.json","w") as f:
        json.dump(users,f)
    return True

bot = Bot()
bot.run()
