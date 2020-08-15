tasksList = []

print("Let's add all the tasks you need to do before your trip:")
print("After done with all task enter an X to exit")

def tasks():
    exit1=''
    while exit1 != 'X':
        task = input('Enter Task >>> ')
        task = task.capitalize()
        if task == 'X' or task == 'x':
            exit1 = task
        elif task != 'X' or 'x':
            tasksList.append(task)
    return(tasksList)

def reviewTasks():
    review = input('Want to review your taks... Enter Y for yes, N for No >>> ')
    review = review.capitalize()

    if review == 'Y':
        for t in range(len(tasksList)):
            print('Task',t+1,': ',tasksList[t]) 


def addNewTasK():
    exit2 = True
    while exit2:
        addTask = input('Need to add a new task... Enter Y for yes, N for No >>> ')
        addTask = addTask.capitalize()

        if addTask == 'N':
            exit2 = False
        elif addTask == 'Y':
            position = int(input('In which position you will enter the new task (Enter a number from 1 to {} >>> '.format(len(tasksList)+1)))
            newTask = input('Enter new Task >>>  ')
            tasksList.insert(position-1,newTask)
    return(tasksList)


def completedTasks():
    exit3 = True

    while exit3:
        taskCompleted = input('Have completed any task... Enter Y for yes, N for No >>> ')
        taskCompleted = taskCompleted.capitalize()

        if taskCompleted == 'N':
            exit3 = False
        elif taskCompleted == 'Y':
            position = int(input('Which task has been completed (Enter a number from 1 to {} >>> '.format(len(tasksList))))
            tasksList.remove(tasksList[position-1])



tasks()
reviewTasks()
addNewTasK()
reviewTasks()
completedTasks()
reviewTasks()

print('let\'s keep save your party\'s passport information:')
passportInfo = {}
partyNum = int(input('How many members in your  party >>> '))
for n in range(partyNum):
    passportName = input('Enter name in passport >>> ')
    passportNum = input('Enter number in passport >>> ')
    passportInfo[passportName]=passportNum

print('Displaying passport information')
print('Party Members',partyNum)
for name in passportInfo:
    print('Passport Name:',name,'Passport number:',passportInfo[name])

countriesVisited = set()
numCountries = int(input('How many countries have you visited >>> '))
for c in range(numCountries):
    country = input('Add country {}: '.format(c+1))
    country = country.capitalize()
    countriesVisited.add(country)

#print(countriesVisited)

friendsCountry = set()
numCountriesF = int(input('How many countries have your friend visited >>> '))
for c in range(numCountriesF):
    countryF = input('Add country {}: '.format(c+1))
    countryF = countryF.capitalize()
    friendsCountry.add(countryF)

#print(friendsCountry)

MissingCountries = friendsCountry.difference(countriesVisited)

print('The countries you have not visited, that your friend have visited are:')
for country in MissingCountries:
    print(country,end=' ')







