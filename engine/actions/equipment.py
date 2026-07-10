from engine.action_handler import action
from engine.resolver import resolve_item



@action("equip")
def do_equip(

    session,

    action,

    world

):

    item = resolve_item(

        action.target,

        session.player.inventory

    )


    if not item:

        return "You do not have that item."


    if not getattr(

        item,

        "slot",

        None

    ):

        return "You cannot equip that."


    session.player.equip(

        item

    )


    return (

        f"You equip the {item.name}."

    )



@action("unequip")
def do_unequip(

    session,

    action,

    world

):

    for slot, item in session.player.equipment.items():

        if item is None:

            continue


        if item.matches(

            action.target

        ):

            session.player.unequip(

                slot

            )


            return (

                f"You remove the {item.name}."

            )


    return "You are not wearing that."



@action("equipment")
def do_equipment(

    session,

    action,

    world

):

    weapon = session.player.equipment.get(

        "weapon"

    )

    armor = session.player.equipment.get(

        "armor"

    )


    return "\r\n".join(

        [

            "Equipment:",

            f"Weapon: {weapon.name if weapon else 'None'}",

            f"Armor: {armor.name if armor else 'None'}"

        ]

    )
