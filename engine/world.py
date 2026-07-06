WORLD = {
    "start_room": {
        "name": "Ruined Outpost",
        "description": (
            "Stone walls crumble under moss and time. "
            "A cold wind moves through broken watchtowers."
        ),
        "exits": {
            "north": "forest_edge"
        },
        "items": ["rusted key"],
        "hidden": {
            "search": "You notice faint scratch marks on the stone floor.",
            "perception": "You spot disturbed dirt near the eastern wall."
        }
    },

    "forest_edge": {
        "name": "Forest Edge",
        "description": (
            "Dark pine trees press close together. "
            "The forest feels alive and watching."
        ),
        "exits": {
            "south": "start_room"
        },
        "items": [],
        "hidden": {
            "perception": "Something large recently moved through the underbrush."
        }
    }
}
