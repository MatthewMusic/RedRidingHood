from Characters.Wolf import Wolf
from Characters.Hunter import Hunter
from Characters.RedRidingHood import RedRidingHood
from Characters.Grandmother import Grandmother
from Characters.FairyGodMother import FairyGodMother
import random

wolf = Wolf()
hunter = Hunter()
red_riding_hood = RedRidingHood()
grandmother = Grandmother()
fairy_god_mother = FairyGodMother()

characters = [wolf, hunter, red_riding_hood, grandmother, fairy_god_mother]
story_list = []

def grandmotherPieCheck():
    index = 0
    character = None
    character2 = None
    while index < len(story_list) - 1:
        if story_list[index].name == 'RedRidingHood':
            character = story_list[index]
        elif story_list[index].name == 'Hunter':
            character2 = story_list[index]
        index += 1

    if character is None and character2 is not None:
        return True
    else:
        return False


def findTwoCharactersInStory(name1, name2):
    index = 0
    character = None
    character2 = None
    while index < len(story_list) - 1:
        if story_list[index].name == name1:
            character = story_list[index]
        elif story_list[index].name == name2:
            character2 = story_list[index]
        index += 1

    if character is None and character2 is None:
        return False
    else:
        return True


def appearCharacter(name):
    index = 0
    character = None
    while index < len(characters) - 1:
        if characters[index].name == name:
            character = characters[index]
            characters.pop(index)
            addCharacterToStory(character)
            break
        else:
            index += 1

    return character


def appearStory(name):
    index = 0
    character = None
    while index < len(story_list) - 1:
        if story_list[index].name == name:
            character = story_list[index]
            break
        else:
            index += 1

    return character


def getSpecificCharacterForTest(index):
    character = characters[index]
    character.introduction()
    characters.pop(index)
    return character


def getCharacter():
    index = random.randint(0, len(characters) - 1)
    character = characters[index]
    character.introduction()
    characters.pop(index)
    return character


def addCharacterToStory(character):
    story_list.append(character)


def killCharacter(name):
    index = 0
    while index < len(story_list) - 1:
        if story_list[index].name == name:
            character = story_list[index]
            character.dead()
            story_list.pop(index)
            break
        else:
            index += 1

def redRidingHoodStory(character, characterTwo):
    # print('redRidingHoodStory')
    if characterTwo.name == 'Grandmother':
        print(character.reactions['alone_grandmother'])
        #name = 'FairyGodMother'
        #new_character = appearCharacter(name) or appearStory(name)
        #new_character.reactions['pie']
    elif characterTwo.name == 'Hunter':
        print(character.reactions['alone_hunter'])
        return 'alone_hunter'
    elif characterTwo.name == 'Wolf':
        print(character.reactions['alone_wolf'])


def grandmotherStory(character, characterTwo):
    if findTwoCharactersInStory('Hunter', 'RedRidingHood'):
        print(character.reactions['hunter_is_there'])
    elif grandmotherPieCheck():
        print(character.reactions['red_riding_hood_is_not_there'])
    elif findTwoCharactersInStory('Grandmother', 'Wolf'):
        print(character.reactions['alone_with_wolf'])
        killCharacter('Wolf')
    elif findTwoCharactersInStory('Grandmother', 'FairyGodMother'):
        character.reactions['fairy_god_mother_is_present']
        print(character.reactions['alone'])


def wolfStory(character, characterTwo):
    if findTwoCharactersInStory('Wolf', 'FairyGodMother'):
        print(character.reactions['meet'])
        killCharacter('Wolf')


def hunterStory(character, characterTwo):
    if findTwoCharactersInStory('Hunter', 'Wolf'):
        killCharacter('Wolf')


def fairyGodMotherStory(character, characterTwo):
    print(character.reactions['appear'])
    finished = True
    return finished


story_methods = {
    'RedRidingHood': redRidingHoodStory,
    'Grandmother': grandmotherStory,
    'Wolf': wolfStory,
    'Hunter': hunterStory,
    'FairyGodMother': fairyGodMotherStory,
}

if __name__ == "__main__":
    answer = input('This is the story about Red Riding Hood. Continue? (y/n)').lower().strip()

    if answer == 'y':
        reactions = 0
        iteration = 0
        while len(characters) > 0:
            if len(story_list) == 0:
                character = getSpecificCharacterForTest(2)
                # character = getCharacter()
                addCharacterToStory(character)

                # character = getSpecificCharacterForTest(1)
                character = getCharacter()
                addCharacterToStory(character)
            else:
                characterOne = story_list[len(story_list) - 2]
                characterTwo = story_list[len(story_list) - 1]
                action = story_methods[characterOne.name](characterOne, characterTwo)
                iteration += 1
                if action == 'alone_hunter':
                    name = 'Grandmother'
                    character = appearCharacter(name) or appearStory(name)
                    # print(character)
                    print('Grandmother hears Red Riding Hood scream and appears out of the blue!')
                # break
                elif action is True:
                    print('END OF STORY! GO HOME! :D')
                    break

                print("Story continues..")
                character = getCharacter()
                addCharacterToStory(character)

                if len(characters) == 0:
                    print('END OF STORY! GO HOME! :D')
                    break

    else:
        print("Well...I don't like you either BLAH! :3")
