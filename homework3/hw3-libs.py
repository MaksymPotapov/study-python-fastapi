# *Деякi вiдповiдi взятi з неба
# 1
player_info = {
    'name': 'Messi',
    'age': 35,
    'sport': 'football',
    'team': 'Barcelona'
}
print(f'#1\t{player_info}\n--------------------')

# 2
book_lib = {
    'Harry Potter': 'J.K. Rowling',
    'Lord of the rings': 'J.R.R. Tolkien',
    'Hobbit': 'J.R.R. Tolkien'
}
print(f'#2\tInitial list: {book_lib}')
book_lib.update({'The Da Vinci Code': 'Dan Brown'})
print(f'  \tResulting lib: {book_lib}\n--------------------')

# 3
countries_lib = {
    'Ukraine': 'Kyiv',
    'Britain': 'London',
    'Spain': 'Madrid',
    'France': 'Paris',
    'Germany': 'Berlin',
    'US': 'Washington D.C.',
    'Mexico': 'Ciudad de Mexico'
}
print(f'#3\tCapitals:')
print(f'  \tIts capital is: {countries_lib.get(input('  \tType the country whose capital you want to know\n  ->'), 'Sorry, country not in our base')}')
print('--------------------')