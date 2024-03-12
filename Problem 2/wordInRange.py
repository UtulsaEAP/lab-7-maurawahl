'''
Name: Maura Wahl
Time: Thursdays at 2pm
'''
def wordInRange():
    #Type your code here
    filename = input()
    word1 = input()
    word2 = input()
    file_object = open(filename)
    another_file_thing = file_object.readlines()
    for x in another_file_thing:
        x = x.strip()
        if word1<=x<=word2:
            print(x + " - in range")
        else:
            print(x + " - not in range")


    return
if __name__ == '__main__':
    wordInRange()