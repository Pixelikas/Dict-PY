# Cria um dicionário e suas propriedades
dog = {
    
    'Name': 'Boo',
    'Breed': 'Pitbull',
    'Age': 6
    
}

# Mostra na tela o valor contido na propriedade 'Name'
print(dog['Name'])

# Atribui novo valor para a propriedade 'Age'
dog['Age'] = 8

# Cria uma nova propriedade 'Size' com o valor 'G'
dog['Size'] = 'G'

# Deleta a propriedade 'Breed'
del dog['Breed']

# Mostra na tela as propriedade e valores do dicionário 
print(dog)

# Mostra na tela somente as propriedades do dicionário 
print(dog.keys())

# Mostra na tela somente os valores das propriedades do dicionário 
print(dog.values())