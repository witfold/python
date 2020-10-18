dict = {
    'name': '',
    'surname': '',
    'year of birthday': 0,
    'city': '',
    'email': '',
    'phone': ''
}


def type_user_info(name, surname, year_of_birthday, city, email, phone):
    print(f' Name - {name} '
          f' Surname - {surname} '
          f' Year of birthday - {year_of_birthday} '
          f' City - {city} '
          f' Email - {email} '
          f' Phone - {phone}')


for key in dict.keys():
    value = input(f'Type {key} value: ')
    if key == 'year of birthday':
        value = int(value)
    dict[key] = value

type_user_info(
    name=dict.get('name'),
    surname=dict.get('surname'),
    year_of_birthday=dict.get('year of birthday'),
    city=dict.get('city'),
    email=dict.get('email'),
    phone=dict.get('phone')
)
