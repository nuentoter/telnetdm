self.inventory = []

self.equipment = {

    "head": None,

    "chest": None,

    "legs": None,

    "feet": None,

    "hands": None,

    "weapon": None,

    "offhand": None,

    "ring_left": None,

    "ring_right": None,

    "neck": None

}


def equip(
    self,
    item
):

    slot = item.slot

    self.equipment[slot] = item


def unequip(
    self,
    slot
):

    item = self.equipment[slot]

    self.equipment[slot] = None

    return item

