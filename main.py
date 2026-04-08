from family import FamilyTree

def main():
    print("Running main.py...")
    family_tree = FamilyTree()

    family_tree.add_person('King Arthur')
    family_tree.add_person('Queen Margaret')
    family_tree.add_person('Child1', 'Queen Margaret')

    print("Queen Margaret's children:")
    children = family_tree.get_relationship('Queen Margaret', 'children')
    print(children)  # ['Child1']

if __name__ == '__main__':
    main()