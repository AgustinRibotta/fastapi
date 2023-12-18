""" Typos de datos """
def get_full_name(first_name, last_name):
    full_name = first_name.title() + ' ' + last_name.title()
    return full_name

print(get_full_name('Agustin', 'Ribotta'))

# Para auto compeltadose debe especificar el tipo de dato
def get_name(name: str, last_name: str) -> str:
    full_name = name.title() + ' ' + last_name.title()
    return full_name

print(get_full_name('Agustin', 'Ribotta'))
print(get_full_name('Agustin', 'Ribotta'))

def gat_name_with_age(name: str, age: int):
    name_with_age = name + 'is this old: ' + str(age)
    return name_with_age

print(gat_name_with_age('Agustin',12))


""" Type List """

def procees_items (items: list[str]) -> str:
    for e in items:
        print(e.title())


""" Type set and tuple """

def procees_item( items_t: list[ int, int, int], items_s: set[bytes]):
    return items_t, items_s


""" Type dict """

def procees_item_dic(price: dict[str, float]):
    for items_name, item_precie in price.items():
        print(items_name, item_precie)

""" Type Union """
# La variable admite varios tipos de datos

def procees_item_union(items: str | int ):
    print(items)