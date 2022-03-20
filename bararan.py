import cmath

dictionary = ["hello", "melo", "food", "foonchoza", "Abo", "hellicopter", "hellooooo", 'barev', 'kartsumem', 'hajox',
              'Arman', 'varaguyr']

search = input("searching: ")
ed = int(input("input your edit_distance: "))
output_quantity = int(input("input your output_quantity: "))

counter = 0

# 1st method
"""
if search in dictionary:
    print(search)
else:
    print("did you mean:")

    for word in dictionary:
        if search.tolower() in word.tolower() and abs(len(search)-len(word)) <= ed:
            counter += 1

            if counter < output_quantity:
                print(word)
            else:
                break
"""

# 2nd method

lowercased_dict = []

for x in dictionary:
    lowercased_dict.append(x.lower())

for i in range(ed + 1):
    for j in range(ed + 1):

        t = False
        new = search[i:len(search) - j]

        if new.lower() in lowercased_dict:
            counter += 1
            t = True

        if counter <= output_quantity:
            if 0 < counter and t is True:
                if i != 0 or j != 0:
                    print("Did you mean: ", new)
                    continue
                else:
                    print("Found: ", new)
                    continue
        else:
            break
for word in dictionary:

    for i in range(ed + 1):
        for j in range(ed + 1):

            t = False
            new = word[i:len(word) - j]

            if word[i:len(word) - j].lower() == search:
                counter += 1
                t = True

            if counter <= output_quantity:
                if 0 < counter and t is True:
                    if i != 0 or j != 0:
                        print("Did you mean: ",word)
                        continue
                    else:
                        print("Found: ", word)
                        continue
            else:
                break
if counter == 0:
    print("there is no matching one.")
