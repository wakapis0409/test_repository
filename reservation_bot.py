# インストールした discord.py を読み込む
import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix='.')


class Date_class:
    def __init__(self):
        #持ち越し
        self.carryover_member = [[],[],[],[],[]]
        self.carryover_member_msg_id=[]
        #正常
        self.member =[[],[],[],[],[]]
        self.member_msg_id =[]
            




@client.event
async def on_ready():
    print("ログインしました")
    print("bot名:"+client.user.name)
    print("botID:"+str(client.user.id))
    print("discord.pyのver:"+str(discord.__version__))
    print("---------")





@client.command()
async def test(ctx):
    txt = "ok"
    lis = []
    lis.append("aaaa")
    lis.append("iiii")
    lis.append("uuuu")

    await ctx.send(lis)

    lis.pop(0)
    await ctx.send(lis)
    lis.pop(0)
    await ctx.send(lis)

        
    await ctx.send("test")
    try:
        await ctx.send(int("2"))       
    except Exception as e:
        await ctx.send(str(e))
        txt = "no"
        return

    await ctx.send("~~"+txt+"~~")
    
    
    

    
    


@client.event
async def on_reaction_add(reaction,user):
    msg = reaction.message

    if user.bot == True:
        pass
    else:
        for j in range(len(date_list)):
            for i in range(5):
                if msg.id == date_list[j].carryover_member_msg_id[i]:
                    date_list[j].carryover_member[i].append(user.name)
                    await msg.edit(content = "凸希望："+str(date_list[j].carryover_member[i]))
                    break
                if msg.id == date_list[j].member_msg_id[i]:
                    date_list[j].member[i].append(user.name)
                    await msg.edit(content = "凸希望："+str(date_list[j].member[i]))
                    break


    
            
    
@client.event
async def on_reaction_remove(reaction,user):
    msg = reaction.message

    if user.bot == True:
        pass
    else:
        for j in range(len(date_list)):
            for i in range(5):
                if msg.id == date_list[j].carryover_member_msg_id[i]:
                    date_list[j].carryover_member[i].remove(user.name)
                    await msg.edit(content = "凸希望："+str(date_list[j].carryover_member[i]))
                    break
                if msg.id == date_list[j].member_msg_id[i]:
                    date_list[j].member[i].remove(user.name)
                    await msg.edit(content = "凸希望："+str(date_list[j].member[i]))
                    break










#ボス名
boss_name = ["ワイバーン","ワイルドグリフォン","スカイワルキューレ","スピリットホーン","サジタリウス"]

#データクラス格納
date_list = []
date_laps = []

@client.event
async def on_message(message):
    if message.content.startswith("$"): 
        #発言者がbotではない
        if client.user != message.author:
            #　$○○
            try:
                laps = int(message.content[1:])
            except Exception as e:
                print(e)
                return


            
            date = Date_class()

            #古いデータの削除
            if len(date_list)>=3:
                date_list.pop(0)
                date_laps.pop(0)

            date_list.append(date)
            date_laps.append(laps)

            date_num = len(date_list)-1

            
            for i in range(5):
                num = "1⃣"
                if i ==0:
                    num = "1⃣"
                if i ==1:
                    num = "2⃣"
                if i ==2:
                    num = "3⃣"
                if i ==3:
                    num = "4⃣"
                if i ==4:
                    num = "5⃣"
                
                txt =[]
                txt.append("-------------------------------------------\n\n"+num+"　"+boss_name[i]+" （ "+str(laps)+"週目 ）"+"\n\n➀.持ち越し消化したい")
                txt.append("凸希望：[]")
                txt.append("➁.ここで凸したい")
                txt.append("凸希望：[]")
                
                
                await message.channel.send(txt[0])
                
                reserve1 = await message.channel.send(txt[1])            
                date_list[date_num].carryover_member_msg_id.append(reserve1.id)
                await reserve1.add_reaction('⏫')
                
                await message.channel.send(txt[2])

                reserve2 =await message.channel.send(txt[3])
                date_list[date_num].member_msg_id.append(reserve2.id)
                await reserve2.add_reaction('👀')
                
            await message.channel.send("-------------------------------------------")
            




    await client.process_commands(message)


# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NjU2NTE1MzgyMjczNzY5NTA1.Xfj3Nw.264fbCCAS94Tzmce7yun8NJGZec'


client.run(TOKEN)