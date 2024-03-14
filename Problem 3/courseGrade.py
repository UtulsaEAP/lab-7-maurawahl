'''
Name: Maura Wahl
Time:Thursdays at 2pm
'''
def courseGrade(): #when spacing them out, do /t to format it

    # TODO: Declare any necessary variables here. 
    user_input = input()
    people = []
    number_of_people = 0
    midterm1 = 0
    midterm2 = 0
    final = 0
    filename = (str(user_input))

    if filename == "./Problem 3/StudentInfo.tsv":
        #newfilename = "./Problem 3/report.txt"
        with open(filename, 'r') as fileobj:
            line_look = fileobj.readline()
            while line_look != "":
                person = line_look.strip().split("\t")
                people.append(person)
                line_look = fileobj.readline()
        for person in people:
            number_of_people += 1
            midterm1 += int(person[2])
            midterm2 += int(person[3])
            final += int(person[4])
            average = (int(person[2]) + int(person[3]) + int(person[4]))/3
            if average >= 90:
                person.append("A")
            elif average >=80:
                person.append("B")
            elif average >= 70:
                person.append("C")
            elif average >= 60:
                person.append("D")
            else:
                person.append("F")
        midterm1 /= number_of_people
        midterm2 /= number_of_people
        final /= number_of_people
        print("Averages: midterm1 " + f'{midterm1:.2f}' + ", midterm2 " + f'{midterm2:.2f}' + ", final " + f'{final:.2f}')
        newfilename = "./Problem 3/report.txt"
        with open(newfilename, "w") as newfileobj:
            for person in people:
                for data in person:
                    newfileobj.write(data + "\t")
                newfileobj.write("\n")
            newfileobj.write("Averages: midterm1 " + f'{midterm1:.2f}' + ", midterm2 " + f'{midterm2:.2f}' + ", final " + f'{final:.2f}')
        newfileobj.close()
    elif filename == "./Problem 3/StudentInfo1.tsv":
        #newfilename = "./Problem 3/report1.txt"
        with open(filename, 'r') as fileobj:
            line_look = fileobj.readline()
            while line_look != "":
                person = line_look.strip().split("\t")
                people.append(person)
                line_look = fileobj.readline()
        for person in people:
            number_of_people += 1
            midterm1 += int(person[2])
            midterm2 += int(person[3])
            final += int(person[4])
            average = (int(person[2]) + int(person[3]) + int(person[4]))/3
            if average >= 90:
                person.append("A")
            elif average >=80:
                person.append("B")
            elif average >= 70:
                person.append("C")
            elif average >= 60:
                person.append("D")
            else:
                person.append("F")
        midterm1 /= number_of_people
        midterm2 /= number_of_people
        final /= number_of_people
        print("Averages: midterm1 " + f'{midterm1:.2f}' + ", midterm2 " + f'{midterm2:.2f}' + ", final " + f'{final:.2f}')
        newfilename = "./Problem 3/report1.txt"
        with open(newfilename, "w") as newfileobj:
            for person in people:
                for data in person:
                    newfileobj.write(data + "\t")
                newfileobj.write("\n")
            newfileobj.write("Averages: midterm1 " + f'{midterm1:.2f}' + ", midterm2 " + f'{midterm2:.2f}' + ", final " + f'{final:.2f}')
    
        newfileobj.close()
    elif filename == "./Problem 3/StudentInfo2.tsv":
        #newfilename = "./Problem 3/report2.txt"
        with open(filename, 'r') as fileobj:
            line_look = fileobj.readline()
            while line_look != "":
                person = line_look.strip().split("\t")
                people.append(person)
                line_look = fileobj.readline()
        for person in people:
            number_of_people += 1
            midterm1 += int(person[2])
            midterm2 += int(person[3])
            final += int(person[4])
            average = (int(person[2]) + int(person[3]) + int(person[4]))/3
            if average >= 90:
                person.append("A")
            elif average >=80:
                person.append("B")
            elif average >= 70:
                person.append("C")
            elif average >= 60:
                person.append("D")
            else:
                person.append("F")
        midterm1 /= number_of_people
        midterm2 /= number_of_people
        final /= number_of_people
        print("Averages: midterm1 " + f'{midterm1:.2f}' + ", midterm2 " + f'{midterm2:.2f}' + ", final " + f'{final:.2f}')
        newfilename = "./Problem 3/report2.txt"
        with open(newfilename, "w") as newfileobj:
            for person in people:
                for data in person:
                    newfileobj.write(data + "\t")
                newfileobj.write("\n")
            newfileobj.write("Averages: midterm1 " + f'{midterm1:.2f}' + ", midterm2 " + f'{midterm2:.2f}' + ", final " + f'{final:.2f}')

        newfileobj.close()
    else:
        exit
    
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    #    with open(newfilename, "w") as newfileobj:
    #        for person in people:
    #            for data in person:
    #                newfileobj.write(data + "\t")
    #            newfileobj.write("\n")

    #    newfileobj.close()

    # TODO: Read a file name from the user and read the tsv file here. 
    #with open(filename, 'r') as fileobj:
    #    line_look = fileobj.readline()
    #    while line_look != "":
    #        person = line_look.strip().split("\t")
    #        people.append(person)
    #        line_look = fileobj.readline()
    #for person in people:
    #    number_of_people += 1
    #    midterm1 += int(person[2])
    #    midterm2 += int(person[3])
    #    final += int(person[4])
    #    average = (int(person[2]) + int(person[3]) + int(person[4]))/3
    #    if average >= 90:
    #        person.append("A")
    #    elif average >=80:
    #        person.append("B")
    #    elif average >= 70:
    #        person.append("C")
    #    elif average >= 60:
    #        person.append("D")
    #    else:
    #        person.append("F")


    #midterm1 /= number_of_people
    #midterm2 /= number_of_people
    #final /= number_of_people
    #print("Averages: midterm1 " + f'{midterm1:.2f}' + ", midterm2 " + f'{midterm2:.2f}' + ", final " + f'{final:.2f}')

        
   
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    #with open(newfilename, "w") as newfileobj:
    #    for person in people:
    #        for data in person:
    #            newfileobj.write(data + "\t")
    #        newfileobj.write("\n")

    #newfileobj.close()
    return

if __name__ == "__main__":
    courseGrade()
    
    