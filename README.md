#SelfBotPy Documentation
Overview
SelfBotPy is a Python-based Discord self-bot designed to automate certain tasks for a Discord account. Built using the discord.py library, it enables users to perform various actions like message purging, user banning, and avatar cloning.

Features
Purge: Delete all messages from a specific channel.
Ronyban: Ban users by a simple command.
Avatar: Clone user avatars or gifs.
Installation
Clone the repository:
bash
Copiar
Editar
git clone https://github.com/caducrs/selfbotpy
Install required dependencies:
bash
Copiar
Editar
pip install -r requirements.txt
Replace the token in the script with your Discord account token.
Usage
After setting up, run the bot:

bash
Copiar
Editar
python selfbot.py
The bot will await commands like !purge, !ronyban, or !avatar.

Important Notes
Discord's Terms of Service: Self-bots violate Discord’s Terms of Service, which could result in the suspension or banning of your account. Use with caution.
Token Safety: Keep your token private. Never share it publicly.
