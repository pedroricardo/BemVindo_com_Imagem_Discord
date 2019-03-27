import discord
import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageOps

client = discord.Client()
# BY PR#4003
@client.event
async def on_ready():
    print('BOT ONLINE - Olá Mundo!')
    print(client.user.name)
    print(client.user.id)
    print('--------PR-------')

@client.event
async def on_member_join(member):
# Adicione o Id do canal onde o bot enviará as imgs de bem vindo!
    canal = client.get_channel("Id_do_canal")

    url = requests.get(member.avatar_url)
    avatar = Image.open(BytesIO(url.content))
    avatar = avatar.resize((130, 130));
    bigsize = (avatar.size[0] * 3,  avatar.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(avatar.size, Image.ANTIALIAS)
    avatar.putalpha(mask)

    output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    output.save('avatar.png')

    fundo = Image.open('bemvindo.png')
    fonte = ImageFont.truetype('BebasNeue.ttf',70)
    escrever = ImageDraw.Draw(fundo)
    escrever.text(xy=(180,164), text=member.name,fill=(0,0,0),font=fonte)
    fundo.paste(avatar, (40, 90), avatar)
    fundo.save('1.png')

    await client.send_file(canal, '1.png')



client.run('Digite_seu_token')
