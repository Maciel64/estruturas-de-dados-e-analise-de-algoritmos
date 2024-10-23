
class SiblingsException(Exception) :
    def __init__(self) -> None:
        super().__init__("Relacionamento entre irmãos ⚠️⚠️⚠️")

class VeryVeryWrongRelationShipException(Exception) :
    def __init__(self) -> None:
        super().__init__("Relacionamento erradíssimo ⚠️⚠️⚠️")

class Person :
    def __init__(self, name: str, mother = None, father = None) -> None:
        self.name = name
        self.mother = mother
        self.father = father
        self.sons = []

        if mother and father :
            mother.add_son(self)
            father.add_son(self)

    def add_son(self, son) :
        self.sons.append(son)

    def ancestors (self) :
        if self.mother :
            print(f"Minha mãe é {self.mother.name}")

        if self.father :
            print(f"Meu pai é {self.father.name}")

        if not self.mother and not self.father :
            return
    
        self.ancestors()


class Male (Person) :
    def __init__(self, name: str, mother: Person = None, father: Person = None, wife = None) -> None:
        super().__init__(name, mother, father)
        if wife: self.set_wife(wife)

    def set_wife(self, wife) :
        if self.mother :
            if self.mother == wife :
                raise VeryVeryWrongRelationShipException()

            if wife.mother and self.mother == wife.mother :
                raise SiblingsException()
            
        if self.father and wife.father :
            if self.father == wife.father :
                raise SiblingsException()

        self.wife = wife
        self.wife.husband = self


class Female (Person) :
    def __init__(self, name: str, mother: Person = None, father: Person = None, husband = None) -> None:
        super().__init__(name, mother, father)
        if husband: self.set_husband(husband)

    def set_husband(self, husband) :
        if self.mother and husband.mother :
            if self.mother == husband.mother :
                raise SiblingsException()
            
        if self.father :
            if self.father == husband.father :
                raise VeryVeryWrongRelationShipException()

            if husband.father and self.father == husband.father :
                raise SiblingsException()

        self.husband = husband
        self.husband.wife = self

def genealogic_tree(person: Person) :
    print(f"Meu nome é {person.name}")

    if person.mother :
        print(f"Minha mãe é {person.mother.name}")

    if person.father :
        print(f"Meu pai é {person.father.name}")

    if len(person.sons) > 0 :
        print(f"Tenho {len(person.sons)} filhos, sendo eles ")
        for son in person.sons :
            print(son.name)
    
    if not person.mother and not person.father :
        return
    
    print()
    genealogic_tree(person.mother)
    genealogic_tree(person.father)


def main() :
    try :
        person1 = Male("João")
        person2 = Female("Maria")

        person3 = Male("Henrique", person2, person1)
        person4 = Female("Sofia", person2, person1, person3)
        
        genealogic_tree(person4)

    except Exception as e :
        print(e)
main()