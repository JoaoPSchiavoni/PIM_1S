
from utilities import colors, users
colors.colors()

while True:
    name = users.get_user_info()
    users.welcome(name)
    users.user_consentiment(name)
    
    print()
    
    