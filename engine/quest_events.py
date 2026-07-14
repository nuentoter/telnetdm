def process_event(player, event, target):

    completed = []

    for quest in list(player.quests):

        if hasattr(quest, "advance"):

            before = quest.completed
            quest.advance(target)

            if quest.completed and not before:
                completed.append(quest)

                if hasattr(player, "complete_quest"):
                    player.complete_quest(quest)

    return completed
