class Registry:

    def __init__(self):

        self.entities = {}



    def register(
        self,
        entity
    ):

        self.entities[
            entity.id
        ] = entity



    def unregister(
        self,
        entity_id
    ):

        self.entities.pop(
            entity_id,
            None
        )



    def get(
        self,
        entity_id
    ):

        return self.entities.get(
            entity_id
        )



    def all(self):

        return list(
            self.entities.values()
        )



    def find_by_name(
        self,
        text
    ):

        text = text.lower()

        for entity in self.entities.values():

            if entity.name.lower() == text:

                return entity

        return None



    def find_by_tag(
        self,
        tag
    ):

        tag = tag.lower()

        return [

            entity

            for entity in self.entities.values()

            if entity.has_tag(tag)

        ]
