# Vacuum Cleaner Problem

rooms = {'A': 'Dirty', 'B': 'Dirty'}
location = 'A'

while True:
    if rooms[location] == 'Dirty':
        print("Cleaning Room", location)
        rooms[location] = 'Clean'
    elif location == 'A':
        location = 'B'
    else:
        break

print("\nFinal Status:")
print(rooms)
