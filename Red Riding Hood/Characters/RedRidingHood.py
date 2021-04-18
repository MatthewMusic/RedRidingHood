class RedRidingHood():
    def __init__(self):
        self.alive = True
        self.name = 'RedRidingHood'
        self.reactions = {
            'alone_grandmother': 'Red Riding Hood and her Grandmother eats pie.',
            'alone_hunter': 'Red Riding Hood is alone with the Hunter, and screams.',
            'alone_wolf': 'Red Riding Hood is alone with the Wolf, and gives him flowers.',
            'become_wolf': 'Red Riding Hood got impatient and turned into a Wolf too!'
        }

    def dead(self):
        self.alive = False
        print('Red Riding Hood has died')

    def introduction(self):
        print("I am the adorable Red Riding Hood!")

