def normalize_words(text):
    """
    Makes comparisons less strict.
    """

    replacements = {
        "rusty": "rusted",
        "old": "",
        "ancient": "",
        "thing": "",
        "object": ""
    }

    words = text.lower().split()

    cleaned = []

    for word in words:
        if word in replacements:
            replacement = replacements[word]

            if replacement:
                cleaned.append(replacement)

        else:
            cleaned.append(word)

    return cleaned



def resolve_item(target, available_items):

    target_words = normalize_words(target)


    for item in available_items:

        item_words = normalize_words(item)


        matches = 0


        for word in target_words:

            if word in item_words:
                matches += 1


        if matches >= len(target_words):
            return item


    return None
