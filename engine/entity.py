from uuid import uuid4


class Entity:

    def __init__(
        self,
        entity_id=None,
        name=""
    ):

        self.uid = str(uuid4())

        self.id = entity_id or self.uid

        self.name = name

        self.components = {}

        self.tags = set()



    def add_component(
        self,
        component
    ):

        self.components[
            component.__class__.__name__
        ] = component

        component.entity = self



    def get(
        self,
        component_type
    ):

        return self.components.get(
            component_type
        )



    def has(
        self,
        component_type
    ):

        return component_type in self.components



    def add_tag(
        self,
        tag
    ):

        self.tags.add(
            tag.lower()
        )



    def has_tag(
        self,
        tag
    ):

        return tag.lower() in self.tags



    def __repr__(self):

        return (
            f"<Entity {self.id}>"
        )
