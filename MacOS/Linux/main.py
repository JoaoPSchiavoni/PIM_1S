
from utilities import colors, users
colors.colors()
from time import sleep

while True:
    name = users.get_user_info()
    users.welcome(name)
    users.user_consentiment(name)
    
    print()
    
    