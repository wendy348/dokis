import discord, random, asyncio, chalk
from discord.ext import commands as client
from Cogs.config import conf

class Event(client.Cog): #Silly man class leave alone thx

    def __init__(self, bot):
         self.b = bot

    @client.Cog.listener()
    async def on_ready(self): #When the bot is ready
        print("\n")
        print(chalk.green(f"[SUCCESS] Connected to Discord as: {self.b.user}"))
        if conf.sharding is False: #If sharding is disabled
            print(chalk.red(f"[WARNING] Sharding: Disabled"))
        elif conf.sharding is True: #If sharding is Enabled
            print(chalk.green("[INFO] Sharding: Enabled"))
            print(chalk.yellow(f"[INFO] Using SHARD's {self.b.shard_ids}")) #Shows us how many shards we are currently using

        print(chalk.cyan(f"[INFO] Config name: '{conf.name}'")) #Shows us the name defined in the config
        print(chalk.cyan(f"[INFO] Defualt Prefix: 'Prefix 1: {conf.prefix1} | Prefix 2: {conf.prefix2}'")) #Shows us the 2 prefixes defined in the config
        print(chalk.cyan("[INFO] Are you braindead: Most Likely")) #Yup
        print(chalk.cyan(f"[INFO] I'm currently in [{len(self.b.guilds)}] server(s).")) #Shows us how many servers we are in
        aaa = True
        for guild in self.b.guilds: #Set all guild the doki is in to have triggers enabled on startup otherwise they no be in list which means triggers are off.
            conf.w_tog_on.insert(0, guild.id)
        while aaa: #A loop to make the game activity change every 900 seconds
            for list in conf.playing_msg:
                await self.b.change_presence(activity=discord.Game(name=list))
                await asyncio.sleep(900)

    @client.Cog.listener()
    async def on_guild_join(self,guild):
        conf.w_tog_on.insert(0, guild.id)
        # Remember to add a message here
    
    @client.Cog.listener()
    async def on_message(self,message):
        # ------------------------------------------------------------------------------------------------------------------------------------------------
        name_words = ["cinnamon bun", "best girl"]
        name_list = ["Did someone mention me?", "You rang?", "Are you guys talking about me?"]

        goodmorning_words = ["goodmorning", "goodmorning,", "goodmorning!", "good morning", "Good Morning", "Good morning"]
        goodmorning_list = ["Good morning! I hope you slept well!~", "Morning, everyone!", "Goooooooood morning!~", "Morning, Sunshine!~"]

        goodafternoon_words = ["goodafternoon", "goodafternoon,", "goodafternoon!", "good afternoon", "Good Afternoon", "Good afternoon"]
        goodafternoon_list = ["Good afternoon!", "Afternoon?? Shoot! I'm late for school again!", "Good afternoon, indeed!", "Afternoon!"]

        goodnight_words = ["goodnight", "gn", "goodnight,", "goodnight!", "good night", "Good Night", "Good night"]
        goodnight_list = ["Goodnight! Sleep tight! Don't let the bedbugs bite!~", "Nighty night!~", "Sleep well!", "Goodnight!"]

        breakfast_words = ["breakfast", "b2"]
        breakfast_list = ["i want breakfast"]

        hang_words = ["hang", "hanging", "hung", "hanged"]
        hang_list = [":unamused:", "Hey! Stop acting like a meanie!", ":rolling_eyes:", "I thought we were better than this...", "Ha, ha. Funny. Can you sense my sarcasm?"]
        suicide_list = ["H-Hey! There's no need to do that, I promise you! Someone out there still wants you to keep going, I'm sure!", "If I'm reading this right, then it sounds like you're thinking of doing something terrible. Please, don't do it!", "Listen, I've been where you are. You'll get through it, I promise.", "Here, this is the National Suicide Prevention Lifeline. They'll be able to help you, I promise! 1-800-273-8255"]

        kill_words = ["kill"]

        meanie_words = ["meanie"]
        meanie_list = ["Do we have a meanie in the server? If so, please stop.", "Cease your bulli, you meanie!", "Boo! You meanie..."]

        confused_list = ["????????", "Maybe try something I actually understand?"]

        # ------------------------------------------------------------------------------------------------------------------------------------------------
        mct =  message.content.lower().split(" ") # (MCT | Message Contents)
        for word in mct:
            if message.content.lower() in name_words:
                if message.author.bot:
                    pass

                else:    
                    if message.guild.id in conf.w_tog_on: 
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed) 
                        await message.channel.send(random.choice(name_list)) 
                        return
                    else:
                        pass

            if word.lower() in breakfast_words:
                if message.author.bot:
                    return
                    
                if message.guild.id in conf.w_tog_on:
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed) 
                    await message.channel.send(random.choice(breakfast_list)) 
                    return
                else:
                    pass

            if word.lower() in goodmorning_words:
                if message.author.bot:
                    pass
                else:    
                    if message.guild.id in conf.w_tog_on: 
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed) 
                        await message.channel.send(random.choice(goodmorning_list)) 
                        return
                    else:
                        pass

            if word.lower() in goodafternoon_words:
                if message.author.bot:
                    pass
                else:    
                    if message.guild.id in conf.w_tog_on: 
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed) 
                        await message.channel.send(random.choice(goodafternoon_list)) 
                        return
                    else:
                        pass

            if word.lower() in goodnight_words:
                if message.author.bot:
                    pass
                else:    
                    if message.guild.id in conf.w_tog_on: 
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed) 
                        await message.channel.send(random.choice(goodnight_list)) 
                        return
                    else:
                        pass


            if word.lower() in meanie_words:
                if message.author.bot:
                    pass
                else:    
                    if message.guild.id in conf.w_tog_on: 
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed) 
                        await message.channel.send(random.choice(meanie_list)) 
                        return
                    else:
                        pass

            if word.lower() in hang_words:
                if message.guild.id not in conf.w_tog_on:
                    pass

                if message.author.bot:
                    pass

                elif message.content.upper().startswith(f"<@{self.b.user.id}>"):
                    pass

                elif "myself" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send(random.choice(suicide_list))
                    return
                    
                else:
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send(random.choice(hang_list))
                    return

            if word.lower() in kill_words:
                if message.guild.id not in conf.w_tog_on:
                    pass

                if message.author.bot:
                    pass

                if message.author.id is conf.natsuki_id:
                    pass

                elif message.content.upper().startswith(f"<@{self.b.user.id}>"):
                    pass

                elif "myself" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send(random.choice(suicide_list))
                    return

                else:
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send("Can we change the topic to something more wholesome please?")
                    return
                        
            # -------------------------------------------------------Tagging-------------------------------------------------------
        if message.content.lower().startswith(f"<@{self.b.user.id}>") or message.content.lower().startswith(f"<@!{self.b.user.id}>"):
            if len(message.content.lower().split(" ")) == 1:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send("Yes?")
                return

            else:
                message1 = message.content.lower().split(" ")[1]

                if "hi" in message.content.lower() or "hello" in message.content.lower() or "hey" in message.content.lower():
                    hello_list = ["Hi!", "Hello!", "Hiiiiii!~", "Hello, human person!"]                    
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(hello_list))
                    return

                elif "i love you" in message.content.lower() or "ily" in message.content.lower():
                    love_list = ["Aww! I love you too!", "Thank you so much!~", "I love you too! :smile:", ":blush:", "I don't really deserve your love, but I'm flattered, anyway!"]                    
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(love_list))
                    return 

                elif "good night" in message.content.lower() or "goodnight" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(goodnight_list))
                    return

                elif "good morning" in message.content.lower() or "goodmorning" in message.content.lower():
                    goodmorning_list = ["Good morning! I hope you slept well!~", "Morning, everyone!", "Goooooooood morning!~", "Morning, Sunshine!~"]                    
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(goodmorning_list))
                    return

                elif "good afternoon" in message.content.lower() or "goodafternoon" in message.content.lower():
                    goodafternoon_list = ["Good afternoon!", "Afternoon?? Shoot! I'm late for school again!", "Good afternoon, indeed!", "Afternoon!"]                    
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(goodafternoon_list))
                    return

                elif "you are" in message.content.lower() or "you're" in message.content.lower():
                    if "pretty" in message.content.lower() or "beautiful" in message.content.lower() or "cute" in message.content.lower():
                        cute_list = ["Awww! Thank you so much! :blush:", "I know you are, but what am I? :stuck_out_tongue_closed_eyes:", "Y-You really think so? Aww!~", "How sweet! Thank you so much!"]                    
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(cute_list))
                    return

                elif "i apologise" in message.content.lower() or "sorry" in message.content.lower() or "i apologize" in message.content.lower():
                    apology_list = ["It's okay; I forgive you!", "Well, alright. As long as you promise to behave yourself!", "Thank you for apologizing!", "Okay. Just try not to do it again!"]                    
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(apology_list))
                    return 

                elif 'loves you' in message.content.lower():
                    member = message.content.split(" ")[1]
                    love_tag_list = [f"Aww! Well, you can tell {member} that I love them, too!", f"{member} does? Well, that's so sweet to hear!", f"And I love {member}, too! :heart:", f"Yay! I'm loved by {member}!"]
                    if 'nigger' in message.content.lower():
                        return

                    elif member == "everyone" or member == "@everyone" or member == "@here" or member == "everybody": #as seen in original
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)
                        await message.channel.send("R-really? EVERYONE? Oh, my!")
                        return

                    elif member == "loves":
                        await message.channel.send("Ehh?")
                        return

                    elif member.lower() == f'<@{conf.natsuki_id}>': #Natsuki
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send("Awww, she does??")
                        return
                        
                    elif member.lower() == f'<@{conf.yuri_id}>': #Yuri
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send("Well, of course she does! Yuri loves everybody!")
                        return
                    elif member.lower() == f'<@{conf.monika_id}>': #Monika
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send("Yay! I'm glad she does!")
                        return

                    elif member.lower() == f'<@{conf.mc_id}>': #MC
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)
                        await message.channel.send("Yay! My best friend loves me!!! :heart:")
                        return

                    else:
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)  
                        await message.channel.send(random.choice(love_tag_list))
                        return

                elif "syka blyat" in message.content.lower() or "pidor ebony" in message.content.lower():
                    russian_list = ["I don't speak Russian, but I'm assuming that's a compliment, to which I say thank you!", "Sorry, I only know English, despite being Japanese.", "Hehehe. That sounds funny."]
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send(random.choice(russian_list))
                    return 
                    
                elif "i'm sick" in message.content.lower() or "puke" in message.content.lower() or "not feeling good" in message.content.lower() or "not feeling great" in message.content.lower():
                    gwell_list = ["Don't worry! I'm sure you'll feel better soon!", "Aww... get plenty of rest, and eat a lot of healthy foods!"]
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)  
                    await message.channel.send(random.choice(gwell_list))
                    return 

                elif "best doki" in message.content.lower() or "best girl" in message.content.lower():
                    if "monika" in message1.lower() or "natsuki" in message1.lower() or "yuri" in message1.lower() or message1 == f"<@{conf.monika_id}>" or message1 == f"<@{conf.natsuki_id}>" or message1 == f"<@{conf.yuri_id}>":
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)
                        await message.channel.send("Well, I respect your opinion!")
                        return 

                    elif message1 == "is" or message1 == f"<@{conf.sayori_id}>" or message1 == "you" or message1 == "you're":
                        async with message.channel.typing():
                            await asyncio.sleep(conf.type_speed)
                        await message.channel.send("S-Stop it! That's not true!")
                        return

                elif "test" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send("Testing, testing! 1-2-1-2 testing!")

                else:
                    async with message.channel.typing():
                        await asyncio.sleep(conf.type_speed)
                    await message.channel.send(random.choice(confused_list))


            # -------------------------------------------------------Tagging-------------------------------------------------------




        # -------------------------------------------------------Interactions with other Doki's!-------------------------------------------------------

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.natsuki_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.natsuki_id: 
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Hehehe! You give the best hugs, Natsuki!")

        if "s-shut up! no she doesn't!" in message.content.lower() and message.author.id == conf.natsuki_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Oh, yes I do!")

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.yuri_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.yuri_id: 
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Aww, thank you, Yuri!")

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.monika_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.monika_id: 
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Ehehe! I love your hugs, Monika! You should give them more often!")

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.mc_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send(f"Aww you're such a sweetheart, <@{conf.mc_id}>")

        if "s-shut up! no i don't!" in message.content.lower() and message.author.id == conf.natsuki_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Awww... :(")

        if "h-hey! Don't hug so hard, Sayori!" in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Oops! I'm sorry!")

        if "haha. well, she is a loving soul." in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("You bet your booty I am! :yum:")
                
        if "who the hell is sayori? i don't know any sayoris..." in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Yuri, it's me! Sayori! Your friend and Vice President of the Literature Club!")
            
        if "what the fuck?? ***i'm*** the vice president, you stupid bitch! and i'm no friend of yours!!" in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send(":disappointed_relieved: :cold_sweat: :confounded: :sob:")
                
        if "i'm sorry, who are you? and why are you hugging me?" in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("I-It's me, Sayori! And I-I just wanted to hug you!")
                
        if "sorry, but i don't know you. please get your messy, stupid self away from me." in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("O-Okay... I'm sorry... :pensive:")

        if "ahaha!~ well, after everything that's happened between us, that's nice to hear!" in message.content.lower() and message.author.id == conf.monika_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Hey, everyone deserves forgiveness! Even you, Monika!")

        if "finnnnnnne, sayori." in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send(f"YAY! *keeps hugging <@{conf.mc_id}>*")

        if "hey, sayori?" in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send(f"Yes, <@{conf.mc_id}>?")

        if "i-i love you, sayori" in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("I-I do too! *hugs MC*")
    
        # -------------------------------------------------------Interactions with other Doki's!-------------------------------------------------------







        
def setup(bot):
    bot.add_cog(Event(bot))
