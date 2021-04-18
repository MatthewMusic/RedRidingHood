class Hunter():
    def __init__(self):
        self.alive = True
        self.name = 'Hunter'
        self.reactions = {
            'wolf': 'The Hunter found the wolf and kills it!',
            'grandmother': 'A delightful smell of pie is in the air. The Hunter appears out of nowhere to follow the pie aroma'
        }

    def dead(self):
        self.alive = False
        print('Hunter has died')

    def introduction(self):
        print("They call me Hunter!")