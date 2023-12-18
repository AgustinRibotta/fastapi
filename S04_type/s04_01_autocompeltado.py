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