class Person:
    def __init__(self, name):
        self.name = name
        self.mother = None
        self.children = []

class FamilyTree:
    def __init__(self):
        self.people = {}

    def add_person(self, name, mother_name=None):
        person = Person(name)
        self.people[name] = person

        if mother_name and mother_name in self.people:
            self.people[mother_name].children.append(person)
            person.mother = self.people[mother_name]

    def get_relationship(self, name, relationship):
        person = self.people.get(name)
        if not person:
            return []

        if relationship == 'mother':
            return [person.mother.name] if person.mother else []
        elif relationship == 'children':
            return [child.name for child in person.children]
        else:
            return []