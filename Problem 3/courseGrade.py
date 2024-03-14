'''
Name: Maura Wahl
Time:Thursdays at 2pm
'''
def courseGrade(): #when spacing them out, do /t to format it

    # TODO: Declare any necessary variables here. 
    user_input = input()
    filename = ("./Problem 3/" + str(user_input) + ".")
      
    # TODO: Read a file name from the user and read the tsv file here. 
    file_object = open(filename)
    read_file = file_object.readlines()
    print(read_file)
   
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    return

if __name__ == "__main__":
    courseGrade()
    
    