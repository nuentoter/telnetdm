from engine.action_handler import action
from engine.quest_events import process_event


@action("attack")
def do_attack(session, action, world):

    if session.combat is None:
        return "There is nothing to attack."

    output = []
    result = session.combat.player_attack()

    if result["hit"]:
        if result["critical"]:
            output.append("Critical hit!")
        output.append(f"You hit the {session.combat.enemy.name} for {result['damage']} damage.")
    else:
        output.append("You miss.")

    if session.combat.finished():
        enemy = session.combat.enemy

        if enemy.hp <= 0:
            xp = enemy.xp_reward
            enemy_name = enemy.name

            session.player.gain_xp(xp)

            output.append(f"You defeated the {enemy_name}!")
            output.append(f"You gain {xp} XP.")

            completed = process_event(
                session.player,
                "defeat",
                enemy_name
            )

            for quest in completed:
                output.append(f"Quest complete: {quest.name}")

                reward = quest.reward

                if reward.get("xp"):
                    session.player.gain_xp(reward["xp"])

                if reward.get("gold"):
                    session.player.gold += reward["gold"]

                output.append(
                    f"Reward: {reward.get('xp',0)} XP, {reward.get('gold',0)} gold"
                )

            if getattr(enemy, "loot", None):
                for loot in enemy.loot:
                    item = getattr(loot, "item", None)
                    if item:
                        session.player.add_item(item)
                        output.append(f"You found: {item.name}")

            session.combat = None
            return "\r\n".join(output)

    enemy_result = session.combat.enemy_attack()

    if enemy_result["hit"]:
        output.append(f"The {session.combat.enemy.name} hits you for {enemy_result['damage']} damage.")
    else:
        output.append(f"The {session.combat.enemy.name} misses.")

    output.append(f"HP: {session.player.hp}/{session.player.max_hp}")

    return "\r\n".join(output)


@action("enemy")
def do_enemy(session, action, world):

    if session.combat is None:
        return "There is no enemy."

    return session.combat.enemy.describe()


@action("flee")
def do_flee(session, action, world):

    if session.combat is None:
        return "You are not fighting."

    session.combat = None
    return "You flee from combat."