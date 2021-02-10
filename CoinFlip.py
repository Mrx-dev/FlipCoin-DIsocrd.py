import discord
from discord.ext import commands, tasks
import random
import asyncio
client = commands.Bot(command_prefix='your prefix')


@client.command(aliases=['flip', 'flipping'])
async def flip_command(ctx):
    try:
        cancel = False
        await ctx.message.delete()
        EmbedHead = discord.Embed(
            description='what you choose? (Heads/Tails)', color=random.randint(0, 0xffffff))
        EmbedHead.set_footer(text='You have 1 min to choose!')
        headORtail = await ctx.send(embed=EmbedHead)
        message = await client.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=60)
        if str(message.content.lower()) == 'heads':
            user_choose = message.content
            await message.delete()
            fliping = await ctx.send(f'Flipping. ')
            await asyncio.sleep(1)
            await fliping.edit(content=f'Flipping.. ')
            await asyncio.sleep(1)
            await fliping.edit(content=f'Flipping... ')
            chooses = ['heads', 'tails']
            random_select = random.choice(chooses)
            await fliping.delete()
            if user_choose == random_select:
                await headORtail.delete()
                choose_embed = discord.Embed(color=0x2ecc71)
                choose_embed.add_field(
                    name='User Choose :bust_in_silhouette:', value=f'**{user_choose}**', inline=True)
                choose_embed.add_field(
                    name='Bot Choose :robot:', value=f'**{random_select}**', inline=True)
                choose_embed.set_author(
                    name='You Win', icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/check-mark-button_2705.png')
                await ctx.send(embed=choose_embed)
            else:
                await headORtail.delete()
                choose_embed = discord.Embed(color=0xe74c3c)
                choose_embed.add_field(
                    name='User Choose :bust_in_silhouette:', value=f'**{user_choose}**', inline=True)
                choose_embed.add_field(
                    name='Bot Choose :robot:', value=f'**{random_select}**', inline=True)
                choose_embed.set_author(
                    name='You Lose', icon_url='https://images.emojiterra.com/mozilla/512px/274c.png')
                await ctx.send(embed=choose_embed)
        if str(message.content.lower()) == 'tails':
            user_choose = message.content
            await message.delete()
            fliping = await ctx.send(f'Flipping. ')
            await asyncio.sleep(1)
            await fliping.edit(content=f'Flipping.. ')
            await asyncio.sleep(1)
            await fliping.edit(content=f'Flipping... ')
            chooses = ['heads', 'tails']
            random_select = random.choice(chooses)
            await fliping.delete()
            if user_choose == random_select:
                choose_embed = discord.Embed(color=0x2ecc71)
                choose_embed.add_field(
                    name='User Choose :bust_in_silhouette:', value=f'**{user_choose}**', inline=True)
                choose_embed.add_field(
                    name='Bot Choose :robot:', value=f'**{random_select}**', inline=True)
                choose_embed.set_author(
                    name='You Win', icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/check-mark-button_2705.png')
                choose_embed.set_footer(
                    text=ctx.author.name, icon_url=ctx.author.icon_url)
                await ctx.send(embed=choose_embed)
            else:
                choose_embed = discord.Embed(color=0xe74c3c)
                choose_embed.add_field(
                    name='User Choose :bust_in_silhouette:', value=f'**{user_choose}**', inline=True)
                choose_embed.add_field(
                    name='Bot Choose :robot:', value=f'**{random_select}**', inline=True)
                choose_embed.set_author(
                    name='You Lose', icon_url='https://images.emojiterra.com/mozilla/512px/274c.png')
                choose_embed.set_footer(
                    text=ctx.author.name, icon_url=ctx.author.icon_url)
                await ctx.send(embed=choose_embed)
        else:
            try:
                cancel = True
                await headORtail.delete()
                temp_message = await ctx.send('Try again wrong choose')
                await temp_message.delete(delay=2)
            except:
                pass
    except asyncio.TimeoutError:
        if not cancel:
            await headORtail.edit(content='The Time is end try again')


# token
client.run('token')
