import random

# Get a random state
def getState(states, no_of_states):
    idx=random.randint(0, no_of_states-1)
    return states[idx]

# Get a random city of the given state
def getCity(state, cities):
    idx=random.randint(0, len(cities[state])-1)
    return cities[state][idx]

# Fetching vendors
fvendors=open("vendors.txt", "r")
lines=fvendors.readlines()
vendors=list(map(lambda vendor: vendor.strip(), lines))

fvendors.close()

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
fsql=open("SQLFiles/Insert_Vendor.sql", "w")

fsql.write("use ABShopping\n")
fsql.write("\n")
fsql.write("INSERT INTO Vendors values\n")
for vendor in vendors:
    state=getState(states, no_of_states)
    city=getCity(state, cities)
    fsql.write("('"+vendor+"','"+state+"','"+city+"'),\n")

fsql.close()