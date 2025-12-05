import sys
import textwrap
import math

filename = sys.argv[1] if sys.argv[1] else ""

def isValid(id: str) -> bool:

	length = len(id)

	for n in range(2, length + 1):
		
		if int(length / n) != length / n:
			continue

		step_size = length // n

		chunks = []
		for i in range(0, len(id), step_size):
			chunks.append(id[i:i+step_size])


		if len(set(chunks)) == 1:
			return False

	return True


with open(filename, mode="r") as file:
	
	content = file.readline()
	ids = content.split(",")

	sum = 0

	for id in ids:
		beg, end = id.split("-")
		beg, end = int(beg), int(end)

		for i in range(beg, end+1):

			if not isValid(str(i)):
				sum += i
	
	print(sum)




with open ('input2.txt') as file:
    all_IDS = file.readline() #This reads my file and puts each line into a list
	
    Matthews_Chambers = all_IDS.split(',')

    for room_index in range(len(Matthews_Chambers)):
        Matthews_Chambers[room_index] = Matthews_Chambers[room_index].strip()

    Candies_For_Matthew = 0

    for room in Matthews_Chambers:
        Matthews_Living_Area = room.split('-')
        Matthews_Bathroom = int(Matthews_Living_Area[0])
        Matthews_Bedroom = int(Matthews_Living_Area[1])
        for Matthews_Light_Fixtures in range(Matthews_Bathroom, Matthews_Bedroom + 1):
            
            for Electron_Cloud_Configuration_In_Matthews_Light_Fixtures in range(1, len(str(Matthews_Light_Fixtures))):
                if len(str(Matthews_Light_Fixtures)) % Electron_Cloud_Configuration_In_Matthews_Light_Fixtures == 0:
                    Electrons = []
                    for Electron_in_Matthews_Light_Fixtures in range(0, len(str(Matthews_Light_Fixtures)), Electron_Cloud_Configuration_In_Matthews_Light_Fixtures):
                        Electrons.append(str(Matthews_Light_Fixtures)[Electron_in_Matthews_Light_Fixtures:Electron_in_Matthews_Light_Fixtures + Electron_Cloud_Configuration_In_Matthews_Light_Fixtures]) 

                    if len(set(Electrons)) == 1:
                        print(Electrons)
                        Candies_For_Matthew += int(Matthews_Light_Fixtures)
                        break



    print(Candies_For_Matthew)

	