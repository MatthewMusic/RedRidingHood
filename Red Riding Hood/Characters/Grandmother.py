class Grandmother():
    def __init__(self):
        self.alive = True
        self.name = 'Grandmother'
        self.reactions = {
            'appear': 'Grandmother heard Red Riding Good scream and appears!',
            'hunter_is_there': 'To protect Red Riding Hood from stranger danger, Grandmother kills the Hunter by tickling him to death...',
            'red_riding_hood_is_not_there': 'Grandmother likes to share her pie, and hands the Hunter a slice',
            'alone_with_wolf': 'Grandmother and the wolf are alone, and she decides to kill it!',
            'fairy_god_mother_is_present': 'Grandmother misses adorable Red Riding Hood so much and wishes for her to appear. Fairy God Mother hears her wishes and makes it come true!',
            'alone': 'Grandmother is alone and decides to bake some pie',
        }

    def dead(self):
        self.alive = False
        print('Grandmother has died')

    def introduction(self):
        print("I am just an old Grandmother!")