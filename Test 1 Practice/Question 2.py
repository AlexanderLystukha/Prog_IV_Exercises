
def swap(pet_dict: dict) -> dict:

    name_specie_dict: dict = {}

    for specie, list_of_pets in pet_dict.items():

        if not specie:
            raise Exception("bro is an empty string")

        if not list_of_pets:
            raise Exception("bro is empty")

        for pet in list_of_pets:
            name_specie_dict[pet] = specie

    return name_specie_dict

try:
    print(swap({ "RAT": ["Lydian", "Elvira"], "GUINEA_PIG": ["Egon"], "TARANTULA": ["Freddie", "Katrina"] }))

except Exception as e:
    print("An exception occured: ", e)