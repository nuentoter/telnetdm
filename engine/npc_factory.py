from engine.npc import NPC
from engine.quest import Quest


def create_quest(data):

    if isinstance(data, Quest):
        return data

    return Quest(
        name=data.get("name", "Unknown Quest"),
        description=data.get("description", ""),
        objective=data.get("objective", ""),
        target=data.get("target", ""),
        amount=data.get("amount", 1),
        reward=data.get("reward", {})
    )


def create_npc(data, database=None):

    if isinstance(data, NPC):
        return data

    quests = [
        create_quest(q)
        for q in data.get("quests", [])
    ]

    return NPC(
        npc_id=data.get("id", "unknown"),
        name=data.get("name", "Unknown"),
        personality=data.get("personality", "neutral"),
        dialogue=data.get("dialogue", []),
        quests=quests,
        database=database
    )


def create_npcs(data, database=None):

    return [
        create_npc(npc, database)
        for npc in data or []
    ]
