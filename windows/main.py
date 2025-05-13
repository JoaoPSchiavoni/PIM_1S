
from utilities import colors, users
colors.colors()

while True:
    name = users.get_user_info()
    #precisa criar uma funcao para pegar a idade do usuario
    users.welcome(name)
    users.user_consentiment(name)
    
    print()
    
    