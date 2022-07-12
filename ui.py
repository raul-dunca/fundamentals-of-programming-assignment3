"""
  User interface module
"""
from copy import deepcopy
from functions import undo,top_special,min_command,avg_command,sort, calculate_avrg, get_p1, get_p2, get_p3, add_contestant, create_contestant, add_contestant_at_poz, init_contestans, split_command, replace_grade_command, remove_contestant_command
def top_command(contestants_list,param):
    """
    this function first checks if we are in the case of the command "top a" or "top a Pb" and then calls the specific
    functions in order to give the requested output
    """
    if (len(param) > 2):
        nr, prob = param.split(maxsplit=1)
        show_top(top_special(contestants_list,nr,prob),nr)
    else:
        pozi = param
        if (int(pozi) > 0 and int(pozi) <=len(contestants_list)):
             show_top(sort(contestants_list),param)
        else:
            raise ValueError
def show_top(contestants_list,param):
    """
    here we show the first param contestants
    """
    index=1
    for i in range (0,int(param)):
        print("C" + str(index) + ": " + str(get_p1(contestants_list[i])) + ", " + str(get_p2(contestants_list[i])) + ", " + str(
            get_p3(contestants_list[i])))
        index += 1

def list_contestant_command(contestants_list,param):
    """
    if we have no parameters we just print the list if we have just one and its "sorted" we print the list sorted
    if we have more parameters then we have 3 cases: < nr , > nr , = nr
    :param contestants_list: the list of contestants
    :param param: the parameters after the keyword "list"
    """
    if param==None:
        show_contestants(contestants_list)
    elif(param=='sorted'):
        l=sort(contestants_list)
        show_contestants(l)
    else:
        op,nr=param.split()
        avrg_list= calculate_avrg(contestants_list)
        if op=='<':
           show_contestants_special1(contestants_list,avrg_list,nr)
        elif op=='=':
            show_contestants_special2(contestants_list, avrg_list, nr)
        elif op=='>':
            show_contestants_special3(contestants_list, avrg_list, nr)

        else:
             raise ValueError
def show_contestants_special1(contestants_list,avrg_list,nr):
    """
    We just print the contestants with the average grade < than a given number
    """
    k=int(0)
    index = 1
    for i in range(0, len(avrg_list)):
        if (avrg_list[i] < int(nr)):
            k = k + 1
    if k == 0:
        print("There is not any contestant with this property!")
    else:
        for i in range(0, len(avrg_list)):
            if (avrg_list[i] < int(nr)):
                print("C" + str(index) + ": " + str(get_p1(contestants_list[i])) + ", " + str(
                    get_p2(contestants_list[i])) + ", " + str(
                    get_p3(contestants_list[i])))
                index += 1
def show_contestants_special2(contestants_list,avrg_list,nr):
    """
    We just print the contestants with the average grade = to a given number
    """
    k=int(0)
    index = 1
    for i in range(0, len(avrg_list)):
        if (avrg_list[i] == int(nr)):
            k = k + 1
    if k == 0:
        print("There is not any contestant with this property!")
    else:
        for i in range(0, len(avrg_list)):
            if (avrg_list[i] == int(nr)):
                print("C" + str(index) + ": " + str(get_p1(contestants_list[i])) + ", " + str(
                    get_p2(contestants_list[i])) + ", " + str(
                    get_p3(contestants_list[i])))
                index += 1
def show_contestants_special3(contestants_list,avrg_list,nr):
    """
    We just print the contestants with the average grade > than a given number
    """
    k=int(0)
    index = 1
    for i in range(0, len(avrg_list)):
        if (avrg_list[i] > int(nr)):
            k = k + 1
    if k == 0:
        print("There is not any contestant with this property!")
    else:
        for i in range(0, len(avrg_list)):
            if (avrg_list[i] > int(nr)):
                print("C" + str(index) + ": " + str(get_p1(contestants_list[i])) + ", " + str(
                    get_p2(contestants_list[i])) + ", " + str(
                    get_p3(contestants_list[i])))
                index += 1
def show_contestants(contestants_list):
    #just a print function
    index = 1
    for contestant in contestants_list:
        print("C" + str(index) + ": "+ str(get_p1(contestant))+", "+str(get_p2(contestant))+", "+str(get_p3(contestant)))
        index += 1
def add_contestant_command(contestants_list, param):
        """
        we split the parameters in the 3 grades and if the values are good we add contestant
        :param contestants_list: the list of contestants
        :param param: the parameters after the keyword "add"
        """
        p1, p2, p3 = param.split()
        try:
            add_contestant(contestants_list, create_contestant(int(p1), int(p2), int(p3)))
        except ValueError as ve:
            print("Contestant could not be added: " + p1, p2, p3)

def insert_contestant_command(contestants_list, param):
    """
    we split the parameters in the 3 grades, the word "at" and the position and if the values are good we add contestant at the certain position
    :param contestants_list: contestants_list: the list of contestants
    :param param: the parameters after the keyword "insert
    :return:
    """
    p1, p2, p3, word, poz = param.split()
    try:
        add_contestant_at_poz(contestants_list, create_contestant(int(p1), int(p2), int(p3)),poz)
    except ValueError as ve:
        print("Contestant could not be added: " + p1, p2, p3)
def start ():
    stack=[]
    contestants_list=init_contestans()
    stack.append(contestants_list[:])
    while True:
        command = input("command> ")
        command_word, command_params = split_command(command)
        try:
            if command_word == 'add':
                add_contestant_command(contestants_list,command_params)
                stack.append(deepcopy(contestants_list))
            elif command_word=='list':
                list_contestant_command(contestants_list,command_params)
            elif command_word=='insert':
                insert_contestant_command(contestants_list,command_params)
                stack.append(deepcopy(contestants_list))
            elif command_word=='remove':
                remove_contestant_command(contestants_list,command_params)
                stack.append(deepcopy(contestants_list))
            elif command_word=='replace':
                replace_grade_command(contestants_list,command_params)
                stack.append(deepcopy(contestants_list))
            elif command_word=="avg":
                print(avg_command(contestants_list,command_params))
            elif command_word=="min":
                print(min_command(contestants_list,command_params))
            elif command_word=="top":
                top_command(contestants_list,command_params)
            elif command_word=="undo":
                contestants_list=undo(stack).copy()
            elif command_word == 'exit':
                return
            else:
                print("Bad command!")
        except ValueError as ve:
            print("You entered some invalid value! Try again")
        except IndexError as ie:
            print("Invalid index")