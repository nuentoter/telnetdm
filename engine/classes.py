CLASSES = {


    "fighter": {

        "hp": 12,

        "description":
            "A trained warrior skilled with weapons."

    },


    "rogue": {

        "hp": 10,

        "description":
            "A quick and clever adventurer."

    },


    "mage": {

        "hp": 8,

        "description":
            "A scholar of mysterious forces."

    },


    "ranger": {

        "hp": 10,

        "description":
            "A wilderness explorer."

    }

}



def get_class(
    name
):

    return CLASSES.get(
        name.lower()
    )
