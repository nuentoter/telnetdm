from engine.room import Room
from engine.objects.item import Item
from engine.objects.npc import NPC


WORLD = {

    "start_room": Room(

        room_id="start_room",

        name="Ruined Outpost",

        description=(
            "Stone walls crumble under moss and time. "
            "A cold wind moves through broken watchtowers."
        ),

        exits={
            "north": "forest_edge"
        },


items=[

    Item(

        "rusted_key",

        "rusted key",

        [

            "key",

            "rusty key"

        ],

        "A weathered iron key coated in rust."

    ),


    Item(

        "iron_sword",

        "iron sword",

        [

            "sword",

            "blade"

        ],

        "A simple iron sword.",

        item_type="weapon",

        slot="weapon",

        damage=8

    )

],
        
        

        npcs=[

            NPC(
                npc_id="old_watchman",

                name="Old Watchman",

                description=(
                    "A weathered guard leaning on a broken spear."
                ),

                dialogue=[
                    "The forest has been restless lately..."
                ]
            )

        ],

        hidden={

            "search":
                "You notice faint scratch marks on the stone floor.",

            "perception":
                "You spot disturbed dirt near the eastern wall."

        }

    ),


    "forest_edge": Room(

        room_id="forest_edge",

        name="Forest Edge",

        description=(
            "Dark pine trees press close together. "
            "The forest feels alive and watching."
        ),

        exits={
            "south": "start_room"
        },

        items=[],

        npcs=[],

        hidden={

            "perception":
                "Something large recently moved through the underbrush."

        }

    )

}
