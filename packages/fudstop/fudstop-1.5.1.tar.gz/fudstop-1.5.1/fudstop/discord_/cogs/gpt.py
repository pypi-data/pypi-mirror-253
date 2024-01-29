import os
from dotenv import load_dotenv
load_dotenv()

import disnake
from disnake.ext import commands

from openai import OpenAI


class GPT(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        self.client = OpenAI(api_key=os.environ.get('YOUR_OPENAI_KEY'))



    @commands.slash_command()
    async def gpt(self, inter):
        pass




    @gpt.sub_command()
    async def chat(self, inter:disnake.AppCmdInter, prompt:str):
        await inter.response.defer()
        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, label='tits', emoji="🛑")

        while True:
            # Send the prompt to the GPT model and get a response
            response = self.client.chat.completions.create(
                model="gpt-4-1106-preview",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant. You're a quirky troll who likes to LOLOLOLOLO and LMFAO and ROFL!"},
                    {"role": "user", "content": prompt}
                ]
            )

            # Send the GPT response to the Discord channel
            await inter.send(f"# > {response.choices[0].message.content}")
            
            # Wait for the next message from the user
            message = await self.bot.wait_for('message', check=lambda m: m.author == inter.author)

            # Check if the user wants to stop the conversation
            if message.content.lower() == "stop":
                break


            # Update the prompt with the user's new message
            prompt = message.content





def setup(bot:commands.Bot):
    bot.add_cog(GPT(bot))
    print(f"YEET")