
import asyncio
import logging
import discord
logger = logging.getLogger(__name__)

from typing import NamedTuple, Optional

helptopics = {}


class HelpTopic(NamedTuple):
    name: str
    emoji: str
    description: str
    links: Optional[list] = []

    def format_links(self):
        if len(self.links) == 0:
            return ''
        string = "** See also:**\n"
        for linkname in self.links:
            if linkname in helptopics:
                string += f"{helptopics[linkname].emoji} {helptopics[linkname].name.title()}\n"
        return string

    def format_for_discord(self):
        return f'''
**{self.emoji + ' ' if self.emoji is not None else ''}{self.name.title()}**
{self.description.strip()}
{self.format_links()}
        '''.strip()

class AllHelpTopicsTopic(HelpTopic):
    def format_for_discord(self):
        string = "**All Help Topics** \nheres everything i know how to help you with:\n"
        for topic_name in helptopics:
            string += f"{helptopics[topic_name].emoji} `g!help {topic_name}`\n"
        return string


# actual help topics

commands = HelpTopic("all bot commands","❓", '''
Access this list with `g!help commands`!

`g!glolf`
Start a random game! You can also provide player names on new lines below the command:

```g!glolf <options>
<person1>
<person2>```
Start a game between <person1> and <person2>. Options is a list of options separated by a space. They can include:
`g!glolf clubs`: Pit glolf club against glolf club in a tag-team club game! Put one (pre-made) club name per line. Case sensitive.
`g!glolf bo3`: best of 3. No matter the competitor count, first to two wins, wins.
`g!glolf bo5`: Best of 5. First to 3 wins wins.

`g!glolfer <name>`
View glolfer stats for a player! You can type in any name!

```g!tourney 1v1
<names on new lines>```
Start a 1v1 tourney! Each new line after tourney 1v1 will be treated as a player name. You need a power-of-two number of entrants to make a tourney. You can also add "30m" or "1h" after the "1v1" to increase the delay between games of the tourney.

`g!tourney 1v1v1`
Start a 1v1v1 tourney. 3 entrants per game, but only one advances.

`g!tourney 1v1 clubs`: Pit glolf club against glolf club in a tag-team tournament where the best club wins! Put one club name per line. Case sensitive. Each round is a best of 5.

`g!viewclub <clubname>`
See information about a glolf club someone has created, such as the players in the club, their loft, and their best stlats!

```g!createclub
g!deleteclub
g!addtoclub
g!removefromclub``` Make and manage clubs. See `g!help clubcommands` for more info.

`g!inventory`: Check your inventory! Each user has a different inventory, which starts with some goodies for adding flavor to players. 

`g!signup`
Become a fan of one of the glolf clubs competing in the Internet Open!

''', ["clubcommands", "invite","all"],)

basics = HelpTopic("glolf basics","ℹ️", '''

Glolf is a turn-based simulated absurdist emoji two-dimensional multiplayer battle royale parody of golf. The prequel to blaseball nobody asked for, glolf is set in the alternate universe where Glolf won the Great Blaseball-Glolf Conflict and Polkadot Patterson is a five-moon driver. Hit the most balls :white_circle: into holes :golf: in the fewest strokes to win!

To get started with glolf, start a game with `g!glolf`, or check out your favorite character's stlats with `g!glolfer <name>`! For a list of commands, try `g!help commands`, or react below to continue browsing these help pages. To see everything I can teach you, try `g!help all`!

Glolf is an one-person passion project! If you want to show support I set up a ko-fi at <https://ko-fi.com/hillexed>  !
''', ["basics2","commands", "all", "invite"])

clubcommands = HelpTopic("club-related commands","🤝", '''

```g!createclub <clubname>
<club emoji> "<club motto>"
<person1>
<person2>
...
```
Create a new glolf club! They can compete in tag-team club games against other clubs.

`g!deleteclub <clubname>`: Delete a club you created.

```g!addtoclub <clubname>
<playername>
```
Add a player to a club you created.

```
g!removefromclub <clubname>
<playername>
```
Remove a player from a club you created.

''', ["commands", "all",])


basics2 = HelpTopic("glolf basics, continued","🟩", '''
Glolf games take plase on a glolf course, represented by a grid of emojis. During a game, glolfers move around a course to try to find balls 🟠 and hit them into the holes ⛳. Here's an example glolf game:

🟩🟩:woman_kneeling:🟩🟩
🟩🟩🟩🟩🟩
🟩⛳🟩🟩🟩
🟠🟩🟩🟩🟦
:see_no_evil:🟩🟩🟦🟦
**Scorecard:**
Jasper Groove :woman_kneeling: 5 holes, 13 strokes :eyes: 
Freddie Missouri :see_no_evil: 4 holes, 8 strokes 

The most important part of a glolf game is the scorecard, at the bottom. There you can see each glolfer's name, their score, and their signature emoji (and modifications, if any, in parentheses). The player(s) in the lead will have an :eyes: emoji next to their scorecard.

Above the scorecard is the course, a 2D grid of emojis. A glolfer's position on the course will be marked by their signature emoji (the emoji next to their name on the scorecard) - so in the above example,  Jasper Groove :woman_kneeling: is near the top middle, while Freddie Missouri :see_no_evil: is in the bottom left, close to the ball 🟠 . Players can move anywhere on the course to reach the ball, and even outside of bounds.

Each turn, a glolfer can perform one action, such as moving towards a ball or hitting a ball they're standing on. The ball is always in play, even if it's out of bounds, off the screen, or in the middle of the ocean. When a glolfer hits a ball, a Hit Arrow will appear over their head :arrow_right: to tell you what direction the ball went.

Notable events, such as a glolfer scoring a ball, getting a hit, or challenging someone to a duel, will appear in a "notable events" box above the course. ''', ["basics","scoring","duels","cracks", "commands", "all"])

cracks=HelpTopic("The Fabric Of Spacetime",'💥','''
During the first Internet Open, a player named Simulacrum hit a 40-tile-long chip. Dubbed the Grand Unchip, this event weakened spacetime. Sometimes players with bad enough Grip will accidentally crack spacetime. Anything on the same tile as a rift will fall in. Don't worry! They usually make it back, falling out of another crack elsewhere onto the course.
''', ["basics2"])

wiki=HelpTopic("Glolf Wiki",'🇼','''
Glolf has a wiki at https://glolfwiki.sibr.dev . Anyone is free to edit!
''', ['all'])

invite = HelpTopic("Bot Invite Link",'📎','''
Invite Glolf to another server using this link: https://discord.com/api/oauth2/authorize?client_id=836012465732059146&permissions=26688&scope=bot
''',['all'])

duels=HelpTopic("duels",'⚔️','''
If two glolfers are on the same tile, they might challenge one another to a Duel! The :crossed_swords: emoji represents a duel in progress on the glolf course.

Each glolfer uses different dueling techniques, and might be more or less effective against other duelers. A glolfer's Self-Awareness and Stance stlats determine how good they are at dueling. Watch for their Signature Move!

When a glolfer wins a duel, they'll launch the other glolfer into the air! They'll land in the farthest hole, allowing the winner of the duel the chance to score. Of course, that's not be the only way a duel can end...
''', ["basics2"])

scorenames=HelpTopic("scorenames",'📛','''
There are different names for scores depending on how many strokes a ball recieves before reaching a hole. Each course has a "par" - a number that measures how many strokes a Competent Player should be able to score the ball using. A "hole in one" is hitting a ball into a hole in one stroke. Here are some other common score names:

4 below par: "Condor"
3 below par: "Albatross"
2 Below par: "Eagle"
1.5 below par: "||------||"
1 below par: "Birdie"
0.5 below par: "||----||"
0 below par: "Par". yup
0.5 above par: ||------||
1 above par: "Bogey"
1.5 above par: ||--------||
2 above par: "Double Bogey"
1.5 above par: ||---------||
3 above par: "Triple Bogey"
3.14 above par: ||--------||
10 above par: "Disappointment"

Making an Eagle will summon the Eagle, and making an Albatross will summon the Albatross.

''', ["basics2"])

scoring=HelpTopic("scoring",'🎊','''
Glolf scoring is similar to golf scoring. In glolf, the player who has hit the most balls into holes wins. (This is technically true in golf too, but glolfers don't have time to wait for their opponents to finish the course). If two glolfers score the same number of balls, the player with the least strokes wins (like golf).

Taking Posession of other players' balls is perfectly legal.

After a player scores in a club game, they must hand off the club to a teammate. Their teammate will drive onto the field in a glolf cart 🛺 to tag in! No guarantees they won't ram anybody, though...
''', ["basics2","scorenames"])

#clubs=HelpTopic("Clubs",'<need emoji>','''
#Players sometimes form clubs. Hitting a ball with a club makes it fly farther!
#''', ['all'])

gods=HelpTopic("gods","💰",'''The IGA, the Internet Glolf Association, appears to be run by mysterious beings. So far there have been confirmed sightings of a being known as the Manager :moneybag:, an Intern occasionally called the Sliced One :octopus:, and the mysterious and so-far unreachable Support :loop:. Every so often they run the Internet Open, a huge community glolf tournament with Prizes and Consequences. They show up from time to time in https://discord.gg/Qjvr2wMbsu in the #glolf-announcements channel to chat, announce, or threaten.''', ['all'])

# more stuff: eagles 
# albatrosses


##### help helptopics

helptopics = {
"basics":basics,
"basics2":basics2,
"scoring":scoring,
"scoring":scorenames,
"commands":commands,
"duels":duels,
"gods":gods,
"cracks":cracks,
"wiki":wiki,
"invite":invite,
"clubcommands":clubcommands
}
helptopics["all"] = AllHelpTopicsTopic("All Help Topics","*️⃣","",helptopics.keys())


async def show_topic(triggering_message, sent_help_message, topic: HelpTopic, client):
    # uses helptopics dict defined above
    sentmessage = await sent_help_message.edit(content=topic.format_for_discord())

    try:
        linked_topics = {helptopics[linked_topic_name].emoji: helptopics[linked_topic_name] for linked_topic_name in topic.links} #can raise ValueError if linked_topic_name not in helptopics
    except KeyError as e:
        missing_keys = [linked_topic_name for linked_topic_name in topic.links if linked_topic_name not in helptopics]
        logging.error(f"Help topic {topic.name}: Unable to find linked topics {missing_keys}")
        # fail gracefully
        linked_topics = {helptopics[linked_topic_name].emoji: helptopics[linked_topic_name] for linked_topic_name in topic.links if linked_topic_name in helptopics}
        
    for emoji in linked_topics:
        try:    
            await sent_help_message.add_reaction(emoji)
        # except NoSuchEmojiError:
        except discord.errors.HTTPException as e:
            logger.error(f"topic {linked_topics[emoji].name} has a broken emoji {emoji} which can't be used as a reaction!")
            raise e

    def check(reaction, user):
        return user == triggering_message.author and str(reaction.emoji) in linked_topics

    try:
        reaction, user = await client.wait_for('reaction_add', timeout=120.0, check=check)
        if str(reaction.emoji) in linked_topics:
             # remove all reactions?
            try:    
                await sent_help_message.clear_reactions()
            except discord.errors.Forbidden:
                pass
            await show_topic(triggering_message, sent_help_message, linked_topics[str(reaction.emoji)], client)
    except asyncio.TimeoutError:
        try:    
            await sent_help_message.clear_reactions()
        except discord.errors.Forbidden:
            pass
    return


async def parse_help_command(message, command_body, client, debug=False):
    topic_name = command_body.strip().lower()
    if len(topic_name) == 0:
        topic_name = "basics"
    if topic_name in helptopics:
        sentmessage = await message.channel.send('ok umm one sec')
        return await show_topic(message, sentmessage, helptopics[topic_name], client)
    else:
        await message.channel.send("sorry umm dont know how to help you with that. try `g!help all` to see everything i can teach you about")
