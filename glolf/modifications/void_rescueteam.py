import data.players


class ReadyToHelp(PlayerModification):
    # ready to help players in the interdimensional void
    # also can spread the word and recruit others
    displayEmoji = "⛑️"
    isDead = False
    description = "This glolfer joined the Rescue Team!"
    join_types = ("reluctantly","eagerly","hestitantly","resolutely","obediently","eagerly","eagerly")

    def on_glolfer_update(self, glolfer, current_glolfer_action):
        if random.random() < 0.1:
            current_glolfer_action["action"] = "attracting"
            ball = get current ball
            move ball closer to self.player.position
                self.game.send_message(f"{self.player.get_display_name()} Attracts a ball towards them!")


    def on_duel(self, glolfer, other_duelist):

        other_duelist = get other duelist
        if self.displayEmoji not in other_duelist.modifications:
            #data.players.add_permanent_modification_to_player(other_duelist.name,self.displayEmoji)
            adjective = random.chance(join_types)
            self.game.send_message(f"{glolfer.name} told {other_duelist.name} about Dog Dad's plight!\n{other_duelist.name} {adjective} joined the Rescue Team!", print_in_summary=True)
