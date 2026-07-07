def resolve_npc(text, npcs):

    text = text.lower()


    text = (
        text.replace("the ", "")
            .replace("old ", "")
    )


    for npc in npcs:

        if text in npc.name.lower():

            return npc


        if text in npc.id.lower():

            return npc


        words = npc.name.lower().split()

        for word in words:

            if word == text:

                return npc


    return None
