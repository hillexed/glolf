
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

```g!glolf
<person1>
<person2>```
Start a game between <person1> and <person2>

`g!glolfer <name>`
View glolfer stats for a player! You can type in any name!

```g!tourney 1v1
<names on new lines>```
Start a 1v1 tourney! Each new line after tourney 1v1 will be treated as a player name. You need a power-of-two number of entrants to make a tourney.

`g!tourney 1v1v1`
Start a 1v1v1 tourney, where each match will have 3 entrants competing and only one advancing to the next round!
''', ["all"],)

basics = HelpTopic("glolf basics","ℹ️", '''

Glolf is a turn-based simulated absurdist emoji two-dimensional multiplayer battle royale parody of golf. The prequel to blaseball nobody asked for, glolf is set in the alternate universe where Glolf won the Great Blaseball-Glolf Conflict and Polkadot Patterson is a five-moon driver. Hit the most balls :white_circle: into holes :golf: in the fewest strokes to win!

To get started with glolf, start a game with `g!glolf`, or check out your favorite character's stlats with `g!glolfer <name>`! For a list of commands, try `g!help commands`, or react below to continue browsing these help pages. To see everything I can teach you, try `g!help all`!
''', ["commands","basics2", "all"])

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

Above the scorecard is the course: a 2D emoji grid. Players can move anywhere on the course to reach the closest ball. A glolfer's position on the course will be marked by their signature emoji (the emoji next to their name on the scorecard). Here, Jasper Groove :woman_kneeling: is near the top middle, while Freddie Missouri :see_no_evil: is in the bottom left, close to the ball 🟠.

Each turn, a glolfer can perform one action, such as moving towards a ball or hitting a ball they're standing on. The ball is always in play, even if it's out of bounds, off the screen, or in the middle of the ocean. When a glolfer hits a ball, a Hit Arrow will appear over their head :arrow_right: to tell you what direction the ball went.

Notable events, such as a glolfer scoring a ball, getting a hit, or challenging someone to a duel, will appear in a "notable events" box above the course. ''', ["basics","duels","cracks"])

cracks=HelpTopic("The Fabric Of Spacetime",'💥','''
During the first Internet Open, a player named Simulacrum hit a 40-tile-long chip. Dubbed the Grand Unchip, this event weakened spacetime. Sometimes players with bad enough Grip will accidentally crack spacetime. Anything on the same tile as a rift will fall in. Don't worry! They usually make it back, falling out of another crack elsewhere onto the course.
''', ["basics2"])

wiki=HelpTopic("Glolf Wiki",'🇼','''
Glolf has a wiki at https://glolfwiki.sibr.dev . Anyone is free to edit!
''', [])

duels=HelpTopic("duels",'⚔️','''
**Duels**

If two glolfers are on the same tile, they might challenge one another to a Duel! The :crossed_swords: emoji represents a duel in progress on the glolf course.

Each glolfer uses different dueling techniques, and might be more or less effective against other duelers. A glolfer's Self-Awareness stlat measures how good they are at dueling. Watch for their Signature Move!

When a glolfer wins a duel, they'll launch the other glolfer into the air! They'll land in the farthest hole so that the winner of the duel can hit their hard-won ball.
''', [])

gods=HelpTopic("gods","💰",'''The IGA, the Internet Glolf Association, appears to be run by mysterious beings. So far there have been sightings of an interesting Manager :moneybag:, an Intern occasionally called the Sliced One :octopus:, and the mysterious and so-far unreachable being known only as Support :loop:. Every so often they run the Internet Open, a huge community glolf tournament with Prizes and Consequences. They show up from time to time in 
https://discord.gg/Qjvr2wMbsu in the #glolf-announcements channel to chat, announce, or threaten.''', [])



##### help helptopics

helptopics = {
"basics":basics,
"basics2":basics2,
"commands":commands,
"duels":duels,
"gods":gods,
"cracks":cracks,
"wiki":wiki,
}
helptopics["all"] = AllHelpTopicsTopic("All","*️⃣","",helptopics.keys())


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
        reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=check)
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