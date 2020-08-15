import string

Princess = 'Belle,Ariel,Rapunzel,Moana,Tiana,Cinderella,Aurora,Ana,Elsa,Jasmine,Merida,Mulan'

Sidekicks = ['Meeko','Woody','Mushu','Olaf','Sven','Gus','Baloo','Tinkerbell','Sebastian','Heihei','Timon','Dory',
             'Lumière','Timon','Pumbaa','Rafiki','Pascal','Baymax','Woody','Mike Wazowski','Kristoff','Stitch',
             'Abu','Pascal','Zazu','Pua','Pumbaa','Heihei','Cogsworth','Olaf','Sven','Louis','Ray','Thumper','Rafiki']

#To covert princess string to a list
Princess = Princess.split(',')

# To remove the duplicate elements in the Sidekicks list
disneySidekicks = []
for sidekick in Sidekicks:
    if sidekick not in disneySidekicks:
        disneySidekicks.append(sidekick)

#Using string methods to declare the letter of the alphabet
letters = string.ascii_uppercase

#To create a disctionary using the letter string and the Disney Sidekicks list
disneySidekicksDict = {}
disneySidekicksDict = dict(zip(letters,disneySidekicks))


#Another way to create a dictionary with the Letter String and the Sidekicks List
'''
for l in letters:
    for sidekick in disneySidekicks:
        disneySidekicksDict[l] = sidekick
        disneySidekicks.remove(sidekick)
        break

print(disneySidekicksDict)
'''



months={'Jan': '', 'Feb': '', 'Mar': '', 'Apr': '', 'May': '', 'Jun': '', 'Jul': '',
        'Aug': '', 'Sep': '', 'Oct': '', 'Nov': '', 'Dec': ''}

#To assign the each princess to a Month
months = dict(zip(months, Princess))


#Starts the game!!!
print('Hiiiii I am Python and I learned a new game...')
print('Let\'s find which disney princess you would be and who would be your sidekick!!!')
play = input('do you want to play? (Yes or No)')
play = play.upper()
print(play)

if play == "YES":
    while play == "YES":
        name = input('What is your name? >> ')
        month = int(input('In what month is your birth-day? Use numbers from 1 to 12, exe: Jan = 1 >>> '))
        nameLetter = name[0]
        count = 1
        for mon in months.keys():
            if count == month:
                value = months.get(mon)
                break
            count+=1
        print('You would be princess {} and your faithfull sidekick would be {}'
              .format(value,disneySidekicksDict.get(nameLetter)))
        print('')
        play = input('Want to play again? >>> ')
    else:
        print("It is been a pleasure playing with you!!!")
        print("See you...")
    