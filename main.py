
 # Bot Discord
 # Fait avec python 3.9.1 avec le module discord.py
 # Pseudo : PikaPika
 # Tag : #4626
 # Id : 851741312164298752



 # # # Block Module # # #
#
import discord
import time
import json
import os

from discord.ext import commands
#
 # # # Fin Du Block Module # # #



 # # # Block Variable # # #
#
bot = commands.Bot(command_prefix = "+", description = "Bot multi-fonction")
bot.remove_command("help")
#
 # # # Fin Du Block Variable # # #



 # # # Block Event # # #
#
@bot.event
async def on_ready():
	await bot.change_presence(activity = discord.Game(name = "+help"))
	print("Online, ready for use !")
	print("---")
	print('statut : "+help"')
	print("---")
	print("Pseudo : PikaPika | InDev")
	print("Tag : #4626")
	print("Id : 851741312164298752")
	print("----------")
	print("commandes :")
	print(" - +help")
	print(" - +InfoServeur")
	print(" - +ping")
	print(" - +ban {membre} {raison}")
	print(" - +kick {membre} {raison}")
	print(" - +rules")
	print("----------")
#
 # # # Fin Du Block Event # # #



 # # # Block Commandes # # #
#

# # # cms InfoServeur
@bot.command()
async def InfoServeur(ctx):
	serveur = ctx.guild
	nombreDeChainesTexte = len(serveur.text_channels)
	nombreDeChainesVocale = len(serveur.voice_channels)
	Description_du_serveur = serveur.description
	Nombre_de_personnes = serveur.member_count
	Nom_du_serveur = serveur.name
	embed = discord.Embed(title = "> Le serveur : **" + str(Nom_du_serveur) + "**", description = "> contient : *" + str(Nombre_de_personnes) + "* personnes !")
	embed.add_field(name = "> La description du serveur est : ", value = str(Description_du_serveur) )
	embed.add_field(name = "> Ce serveur possède : " + str(nombreDeChainesTexte) + " salon écrit", value = "> et " + str(nombreDeChainesVocale) + " salon vocaux.")
	await ctx.send(embed = embed)
	print('commande "InfoServeur" executer')
	print("---")
# # # fin InfoServeur

# # # cms ping
@bot.command(pass_context = True)
async def ping(ctx):
	before = time.monotonic()
	message = await ctx.send("Pong!")
	ping = (time.monotonic() - before) * 1000
	await message.edit(content=f"Pong!  **{int(ping)} ms**")
	print('commande "ping" executer')
	print("-")
	print(f'Ping {int(ping)}ms')
	print("---")
# # # fin ping

# # # cms kick / ban
@commands.has_permissions(kick_members = True)
@bot.command()
async def kick(ctx, user: discord.Member, *, reason = "Pas de raison"):
	await user.kick(reason = reason)
	kick = discord.Embed(title = f":boot: Kicked {user.name}!", description = f"Raison: {reason}\nBy: {ctx.author.mention}")
	await ctx.channel.send(embed = kick)
	print('commande "kick" executer par ' + str(ctx.author) + ' qui kick ' + str(user.name) + ' avec la raison : ' + str(reason))
	print("---")
@commands.has_permissions(ban_members = True)
@bot.command()
async def ban(ctx, user: discord.Member, *, reason="Pas de raison"):
	await user.ban(reason = reason)
	ban = discord.Embed(title=f":boom: Banned {user.name}!", description = f"Raison: {reason}\nBy: {ctx.author.mention}")
	await ctx.channel.send(embed = ban)
	print('commande "ban" executer')
	print("---")
# # # fin kick / ban

# # # cms rules
@bot.command()
async def rules(ctx):
	embed = discord.Embed(title = "***```Les règles de Discord```***", description = "Bonjour, les règles de Discord se trouve sur les lien suivent :\n\n> **ToS** **:** *** https://https://discord.com/terms ***\n\n> **Charte** **:** *** https://https://discord.com/guidelines ***")
	await ctx.send(embed = embed)
	print('commande "rules" executer')
	print("---")
# # # fin rules

#
 # # # Fin Du Block Commandes # # #



# # # # Block Token # # #
#
bot.run('ODUxNzQxMzEyMTY0Mjk4NzUy.YL8r6Q.QGw-OZVnEJ6xzue7GgWOury5NpA')
#
# # # # Fin Du Block Token # # #
