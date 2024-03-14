'''
Name: Maura Wahl
Time: Thursdays at 2pm
'''
def fileNameChange():
    #type your code here
    filename = input()
    with open(filename, "r") as file_object:
        another_file_thing = file_object.readlines()
    for x in another_file_thing:
        x = x.strip()
        y = x.replace("photo.jpg","info.txt")
        print(y)
    

        
    return

if __name__ == '__main__':
    fileNameChange()