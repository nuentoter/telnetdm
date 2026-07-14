from engine.world_database import WorldDatabase


def seed_world(db=None):

    if db is None:
        db = WorldDatabase()


    if db.room_exists("forest_edge"):

        return


    db.add_room(

        "forest_edge",

        {

            "id": "forest_edge",

            "name": "Forest Edge",

            "description":
                "Dark pine trees press close together. The forest feels alive and watching.",

            "exits": {

                "south": "ruined_outpost"

            },

            "items": [],

            "npcs": []

        }

    )


    db.add_room(

        "ruined_outpost",

        {

            "id": "ruined_outpost",

            "name": "Ruined Outpost",

            "description":
                "Stone walls crumble under moss and time. A cold wind moves through broken watchtowers.",

            "exits": {

                "north": "forest_edge"

            },

            "items": [],

            "npcs": []

        }

    )
