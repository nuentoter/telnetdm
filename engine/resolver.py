def resolve_item(target, available_items):

    target = target.lower()

    for item in available_items:

        item_words = item.lower().split()

        matches = 0

        for word in item_words:
            if word in target:
                matches += 1

        if matches > 0:
            return item

    return None
