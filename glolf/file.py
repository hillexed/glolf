import discord
from os.path import splitext

async def parse_file_command(message, command_body):
    if len(message.attachments) == 0:
        return await message.channel.send("Oops, you forgot to attach a text file containing your command")
    elif len(message.attachments) != 1:
        return await message.channel.send("Too many attachments!")
    
    attachment = message.attachments[0]

    filename, fileExtension = splitext(attachment.filename)

    if fileExtension != ".txt":
        return await message.channel.send("I can only read .txt files")
    
    encoded_text = await attachment.read()
    text = encoded_text.decode()

    message.content = text
    message.attachments = []
    return text


