class Wolf():
    def __init__(self):
        self.alive = True
        self.name = 'Wolf'
        self.reactions = {
            'given': 'Wolf has been given something and cries from hapiness.',
            'meet': 'Wolf makes a wish to eat a child. Fairy good mother gets mad and kills wolf.'
        }

    def dead(self):
        self.alive = False
        print('Wolf has died')

    def introduction(self):
        print("I am the big ol' scary Wolf!")