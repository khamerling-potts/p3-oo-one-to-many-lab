class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.add_pet(self)

    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type in self.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise Exception("must be a valid pet type")

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if isinstance(owner, Owner) or not owner:
            self._owner = owner
        else:
            raise Exception("must be an Owner type")

    @classmethod
    def add_pet(cls, pet):
        cls.all.append(pet)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner.name == self.name]

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("must be Pet type")

    def get_sorted_pets(self):
        return sorted(Pet.all, key=lambda pet: pet.name)
