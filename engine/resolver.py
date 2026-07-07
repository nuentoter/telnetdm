def resolve_item(text, items):

    text = text.lower()

    text = (
        text.replace("the ", "")
            .replace("a ", "")
            .replace("an ", "")
    )

    for item in items:

        if item.matches(text):
            return item

    return None
