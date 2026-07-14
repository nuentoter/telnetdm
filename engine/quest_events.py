def process_event(player, event, target):

    completed = []

    for quest in player.quests:

        if hasattr(quest, "advance"):
            before = quest.completed
            quest.advance(target)

            if quest.completed and not before:
                completed.append(quest)

    return completed
