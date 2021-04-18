class FairyGodMother():
    def __init__(self):
        self.alive = True
        self.name = 'FairyGodMother'
        self.game_ended = False
        self.reactions = {
            'appear': 'Fairy God Mother is bored and the story has now ended!',
            'pie': 'Fairy God Mother has appeared to give you her blessing.'
        }

    def dead(self):
        self.alive = False
        print('Fairy God Mother has died')

    def introduction(self):
        print("I am the sexy Fairy God Mother!")

