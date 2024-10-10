import discord
import random
from discord.ext import commands
intents= discord.Intents.default()
intents.message_content=True

bot=commands.Bot(command_prefix="/",intents=intents)

@bot.event
async def on_ready():
    print(f"Hemos iniciado sesión como{bot.user}")

descomposicion={
    "botella":400,
    "lata":50,
    "bolsa":150,
    "vidrio":4000
}

animales_en_peligro = {
    "Este animal tiene una gran trompa y grandes colmillos de marfil, y la recoleccion de los mismos lleva a que estén en peligro de extinción.": "Elefante",
    "Es el felino más grande del mundo y está en peligro por la caza ilegal.": "Tigre",
    "Este gran simio vive en las selvas tropicales de África, está en peligro de extinción.": "Gorila"
}

@bot.command()

async def adivinanza(ctx):
    pista, animal = random.choice(list(animales_en_peligro.items()))
    await ctx.send(f"Pista: {pista}")
    
    await pedir_respuesta(ctx, animal)

async def pedir_respuesta(ctx, animal):
    
    await ctx.send("Escribe tu respuesta:")
    
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    respuesta = await bot.wait_for("message", check=check)
    
    if respuesta.content.lower() == animal.lower():
        await ctx.send("¡Correcto!")
    else:
        await ctx.send("Incorrecto.")
        await pedir_respuesta(ctx, animal)

@bot.command()
async def impacto(ctx,objeto):
    objeto=objeto.lower()
    if objeto in descomposicion:
        tiempo=descomposicion[objeto]
        await ctx.send(f"El objeto{objeto}, dura aprox {tiempo} en descomponerse")
        if tiempo>=100:
            await ctx.send(f"SOS, nos quedamos sin planeta :(")
        else:
            await ctx.send("No registro ese objeto")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('/hola'):
        await message.channel.send("hola!!! que tal tu día?")
    elif message.content.startswith('/mi día estuvo bien'):
        await message.channel.send("me alegro, en que te puedo ayudar?")
    elif message.content.startswith('/mi día estuvo mal'):
        await message.channel.send("que pena 😥, hay algo en que te pueda ayudar?")
    elif message.content.startswith('/si, como puedo hacer para conservar mejor el medio ambiente'):
        await message.channel.send("Puedes:")
        await message.channel.send("Utilizar bombillas de bajo consumo y luces LED.")
        await message.channel.send("Reciclar.")
        await message.channel.send("Comprar productos con certificado ecológico.")
        await message.channel.send("Evitar usar el auto a menos que sea una emergencia.")
        await message.channel.send("Plantar árboles.")
        await message.channel.send("https://www.pngkit.com/png/detail/44-448018_happyearth-poster-on-eco-friendly-life.png")
    elif message.content.startswith('/videos de como cuidar el medio ambiente'):
        await message.channel.send("https://www.youtube.com/watch?v=nvUqnpicSd0&pp=ygUdY29tbyBjdWlkYXIgZWwgbWVkaW8gYW1iaWVudGU%3D")
        await message.channel.send("https://youtu.be/GgnSeqIdKx4")
        await message.channel.send("https://youtu.be/uOXtn9EsT44")
    elif message.content.startswith('/imágenes de lo que no se debe hacer para cuidar el medio ambiente'):
        await message.channel.send("")
    elif message.content.startswith('/gracias por todo'):
        await message.channel.send("de nada!, nos vemos en otra ocasión, no olvides regresar 😉")
    elif message.content.startswith('/Sitios web para cuidar el planeta'):
        await message.channel.send("Earthday.org")
        await message.channel.send("https://www.bing.com/ck/a?!&&p=c891641723eb394fJmltdHM9MTcyODUxODQwMCZpZ3VpZD0wODNjM2UwYS0xNWFkLTY0MTEtMjVkNy0yYWYwMTQxNDY1YjUmaW5zaWQ9NTIwNg&ptn=3&ver=2&hsh=3&fclid=083c3e0a-15ad-6411-25d7-2af0141465b5&psq=greenpeace&u=a1aHR0cHM6Ly93d3cuZ3JlZW5wZWFjZS5vcmcvcGVydS8&ntb=1")
        await message.channel.send("https://www.bing.com/ck/a?!&&p=9e851e91db1e400bJmltdHM9MTcyODUxODQwMCZpZ3VpZD0wODNjM2UwYS0xNWFkLTY0MTEtMjVkNy0yYWYwMTQxNDY1YjUmaW5zaWQ9NTE5Mg&ptn=3&ver=2&hsh=3&fclid=083c3e0a-15ad-6411-25d7-2af0141465b5&psq=WWF&u=a1aHR0cDovL3d3dy53d2ZlbmVzcGFub2wuY29tLw&ntb=1")
        await message.channel.send("https://www.bing.com/ck/a?!&&p=170042e25f0aa879JmltdHM9MTcyODUxODQwMCZpZ3VpZD0wODNjM2UwYS0xNWFkLTY0MTEtMjVkNy0yYWYwMTQxNDY1YjUmaW5zaWQ9NTIwOQ&ptn=3&ver=2&hsh=3&fclid=083c3e0a-15ad-6411-25d7-2af0141465b5&psq=national+geographic&u=a1aHR0cHM6Ly93d3cubmF0aW9uYWxnZW9ncmFwaGljLmNvbS8&ntb=1")
        await message.channel.send("https://www.bing.com/ck/a?!&&p=3383e18be274744dJmltdHM9MTcyODUxODQwMCZpZ3VpZD0wODNjM2UwYS0xNWFkLTY0MTEtMjVkNy0yYWYwMTQxNDY1YjUmaW5zaWQ9NTIzMg&ptn=3&ver=2&hsh=3&fclid=083c3e0a-15ad-6411-25d7-2af0141465b5&psq=national+geographic&u=a1aHR0cHM6Ly93d3cubmF0aW9uYWxnZW9ncmFwaGljbGEuY29tLw&ntb=1")
    await bot.process_commands(message)
bot.run("TOKEN SECRETO")
