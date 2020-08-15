swiches = int(input("How many Switches will you add to the inventory "))
print('Please add the information in order as requested')
print('If the information is not available enter N/A')

SWdb = [ ]
for sw in range(swiches):
    switchInfo = [ ]
    print('Switch {} information:'.format(sw+1))
    hn = input('Hostname >>> ') #0
    switchInfo.append(hn)
    sbs = input('Shared Buffer Space (MB) >>> ') #1
    switchInfo.append(sbs)
    bfm = input('Boot-flash memory (GB) >>> ') #2
    switchInfo.append(bfm)
    sm = input('System memory (BG) >>> ') #3
    switchInfo.append(sm)
    ru = input('Rack unit (RU) >>> ') #4
    switchInfo.append(ru)
    switchInfo = tuple(switchInfo)
    SWdb.append(switchInfo)
    

#print(SWdb)
#print(len(SWdb),'Cantidad de SWs')

N34180YCcounter = 0
N34180YClist = []
N3464Ccounter  =  0
N3464Clist  =  []
N3432DScounter = 0
N3432DSlist = []
N3408Scounter = 0
N3408Slist = []
NoNexusCounter = 0
NoNexusList = []

for sw in range(len(SWdb)):
    if SWdb[sw][1] == '20' and SWdb[sw][4] == '1':
        N34180YClist.append(SWdb[sw][0])
        N34180YCcounter += 1
    elif SWdb[sw][1] == '22' and SWdb[sw][4] == '2':
        N3464Ccounter +=1
        N3464Clist.append(SWdb[sw][0])
    elif SWdb[sw][1] == '70' and SWdb[sw][4] == '1':
        N3432DScounter +=1
        N3432DSlist.append(SWdb[sw][0])
    elif SWdb[sw][1] == '70' and SWdb[sw][4] == '4':
        N3408Scounter +=1
        N3408Slist.append(SWdb[sw][0])
    else:
        NoNexusList.append(SWdb[sw][0])
        NoNexusCounter +=1

print('The following {} devices are Nexus 34180YC'.format(N34180YCcounter))
print(N34180YClist)
print('The following {} devices are Nexus 3464C'.format(N3464Ccounter))
print(N3464Clist)
print('The following {} devices are Nexus 3432D-S'.format(N3432DScounter))
print(N3432DSlist)
print('The following {} devices are Nexus 3408-S'.format(N3408Scounter))
print(N3408Slist)
print('The following {} devices are not Nexus'.format(NoNexusCounter))
print(NoNexusList)