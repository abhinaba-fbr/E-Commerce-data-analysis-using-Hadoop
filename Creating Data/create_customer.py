import random

# Get a random date for DOB in sql format
def getDate():
    year=random.randint(1950, 2010)
    month=random.randint(1, 12)
    if(month<10):
        month='0'+str(month)
    else:
        month=str(month)
    date=random.randint(1, 28)
    if(date<10):
        date='0'+str(date)
    else:
        date=str(date)
    return str(year)+"-"+month+"-"+date

# Get a random Contact number
def getContact():
    contact=random.randint(9000000000, 9999999999)
    return contact

# Get a random state
def getState(states, no_of_states):
    idx=random.randint(0, no_of_states-1)
    return states[idx]

# Get a random city of the given state
def getCity(state, cities):
    idx=random.randint(0, len(cities[state])-1)
    return cities[state][idx]


# Fetching names
fnames=open("names.txt", "r")
lines=fnames.readlines()
names=[]
for line in lines:
    names.append(line.split()[0])

fnames.close()

# Fetching states
fstates=open("states.txt", "r")
states=fstates.readlines()
states=list(map(lambda state: state.strip(), states))
no_of_states=len(states)

fstates.close()

# Fetching cities
cities={}

for state in states:
    state_name=state.lower()
    state_list=state_name.split()
    state_name='_'.join(state_list)
    fs=open(state_name+".txt", "r")
    places=fs.readlines()
    places=list(map(lambda place: place.strip(), places))
    cities[state]=places
    fs.close()

# Create the insert table SQL file
fsql=open("SQLFiles/Insert_Customer.sql", "w")

fsql.write("use ABShopping\n")
fsql.write("\n")
fsql.write("INSERT INTO Customers values\n")
for name in names:
    dob=getDate()
    contact=getContact()
    state=getState(states, no_of_states)
    city=getCity(state, cities)
    fsql.write("('"+name+"','"+str(dob)+"','"+str(contact)+"','"+state+"','"+city+"'),\n")

fsql.close()
