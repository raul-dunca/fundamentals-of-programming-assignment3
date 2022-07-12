"""
  Program functionalities module
"""

def split_command(command):
    """
    We just split de command name and the parameters of the given command
    :param command: a string including the command and parameters together
    :return: the name of the command and the parameters separately
    """
    aux = command.split(" ", maxsplit=1)
    command_word = aux[0]
    command_param = aux[1] if len(aux) == 2 else None
    return command_word, command_param

def test_split_command():
    assert split_command('add 3 8 10') == ('add', '3 8 10')
    assert split_command('insert 10 10 9 at 5') == ('insert', '10 10 9 at 5')
    assert split_command('remove 1') == ('remove','1')
    assert split_command('remove 1 to 3') == ('remove', '1 to 3')
    assert split_command('replace 4 P2 with 5') == ('replace', '4 P2 with 5')
    assert split_command('list') == ('list', None)
    assert split_command('list sorted') == ('list', 'sorted')
    assert split_command('list < 4') == ('list', '< 4')
    assert split_command('exit') == ('exit', None)

test_split_command()

def add_contestant(contestants_list,contestant):
   contestants_list.append(contestant)

def add_contestant_at_poz(contestants_list,contestant,poz):
    """
    this function just adds a constant at a given position
    :param contestants_list: the list of contestants
    :param contestant:the contestant
    :param poz: position where the contestant should be
    """
    if ( int(poz)<0 or int(poz)>=len(contestants_list)):
        raise IndexError
    else:
        contestants_list[int(poz)]=contestant

def test_add_contestant_at_poz():
    l = [[1, 2, 3], [6, 6, 6], [7, 5, 3], [7, 8, 9]]
    poz=1
    c=[10,10,10]
    add_contestant_at_poz(l,c,poz)
    assert l[poz]==c

test_add_contestant_at_poz()

def get_p1(contestant):
    return contestant[0]
def get_p2(contestant):
    return contestant[1]
def get_p3(contestant):
    return contestant[2]

def create_contestant(p1,p2,p3):
    if(p1<0 or p1>10):
        raise ValueError
    elif(p2<0 or p2>10):
        raise ValueError
    elif(p3<0 or p3>10):
        raise ValueError
    else:
        return [p1,p2,p3]

def test_create_contestant():
    assert create_contestant(3,4,5)== [3,4,5]

test_create_contestant()

def calculate_avrg(contestant_list):
    """
    we just calculate the average grade of each contestant an same it in a list
    :param contestant_list: the list of contestants
    :return: the average grades list
    """
    avrg_list=[]
    for i in range (0,len(contestant_list)):
        avrg_list.append((get_p1(contestant_list[i])+get_p2(contestant_list[i])+get_p3(contestant_list[i]))/3.0)
    return avrg_list

def test_calculate_avrg():
    assert  calculate_avrg([[5,5,5],[10,10,10],[3,2,10],[6,8,7],[1,2,4]])==[5.0,10.0,5.0,7.0,2.3333333333333333]

test_calculate_avrg()

def remove_contestant_command(contestants_list,param):
    """
     first we save in a list all the words separated by space and we have 3 cases
     first if we only have 1 word we have the command "remove a" then if we have 2
     the command "remove < a" and if we have 3 words we have the command "remove a to b"
    :param contestants_list:the list of contestants
    :param param: the parameters after command "remove"
    """
    aux= param.split()
    if(len(aux)==1):
        if (int(aux[0]) >= 0 and int(aux[0]) < len(contestants_list)):
            contestants_list[int(aux[0])] = [0, 0, 0]
        else:
            raise IndexError
    elif len(aux)==2:
            remove_op(contestants_list,aux[0],aux[1])
    elif(len(aux)==3):
            remove_contestant(contestants_list,aux[0],aux[1]+" "+aux[2])
    else:
             raise ValueError

def test_remove_contestant_command():
    l = [[1, 2, 3], [6, 6, 6], [7, 5, 3], [7, 8, 9]]
    p = '1'
    remove_contestant_command(l, p)
    assert l == [[1, 2, 3], [0, 0, 0], [7, 5, 3], [7, 8, 9]]

test_remove_contestant_command()

def remove_op(contestants_list,op,nr):
    """
    first in l we get the average list and then we check if the operation is < or > and then we just go on
    the average list and if we find items < or > then nr we remove it from the contestants list
    """
    l=calculate_avrg(contestants_list)
    if(op=="<"):
        for i in range(0,len(l)):
            if(l[i]<int(nr)):
                contestants_list[i] = [0, 0, 0]
    elif op==">":
        for i in range(0,len(l)):
            if(l[i]>int(nr)):
                contestants_list[i] = [0, 0, 0]
    else:
        raise ValueError
def test_remove_op():
    l=[[4,5,3],[9,9,9],[8,7,10]]
    op="<"
    nr="9"
    remove_op(l,op,nr)
    assert l==[[0,0,0],[9,9,9],[0,0,0]]
    l = [[4, 5, 3], [9, 9, 9], [8, 7, 10]]
    op = ">"
    nr = "8"
    remove_op(l,op,nr)
    assert l==[[4, 5, 3], [0, 0, 0], [0, 0, 0]]

test_remove_op()

def remove_contestant(contestants_list,poz1,rest):
    """
    we just remove 2 or more contestants from position a to position b
    :param contestants_list: the list of contestants
    :param poz1: the starting position that need to be removed
    :param rest: the rest of the parameters for ex: to 4
    """
    word, poz2 =rest.split()
    if (int(poz1) >= len(contestants_list) or int(poz1) < 0):
        raise IndexError
    elif (int(poz2)>=len(contestants_list) or int(poz2)<0 or poz1>poz2):
        raise IndexError
    else:
        for i in range(int(int(poz1)),int(int(poz2)+1)):
            contestants_list[i]=[0,0,0]

def test_remove_contestant():
    l=[[1, 2, 3], [6, 6, 6], [7, 5, 3],[7,8,9]]
    poz1='1'
    rest='to 2'
    remove_contestant(l,poz1,rest)
    assert l==[[1, 2, 3], [0, 0, 0], [0, 0, 0],[7,8,9]]

test_remove_contestant()

def replace_grade_command(contestants_list,param):
    """
    we first separate the parameters then we verify if each one has a correct value and then we replace the
    grade from the given problem at a given contestant with a given new grade
    :param contestants_list: the list of contestants
    :param param: the parameters after the keyword "replace"
    :return:
    """
    poz, prob ,word, grade=param.split()
    if (int(poz)<0 or int(poz)>=len(contestants_list)):
        raise ValueError
    elif int(grade)>10 or int(grade) <0:
        raise ValueError
    else:
        if(prob=='P1'):
            contestants_list[int(poz)]=[int(grade),get_p2(contestants_list[int(poz)]),get_p3(contestants_list[int(poz)])]
        elif prob=='P2':
            contestants_list[int(poz)] = [get_p1(contestants_list[int(poz)]), int(grade), get_p3(contestants_list[int(poz)])]
        elif prob=='P3':
            contestants_list[int(poz)] = [get_p1(contestants_list[int(poz)]), get_p2(contestants_list[int(poz)]), int(grade)]
        else:
            raise ValueError

def test_replace_grade_command():
    l = [[1, 2, 3], [6, 6, 6], [7, 5, 3]]
    p = "1 P2 with 5"
    replace_grade_command(l,p)
    assert l[1][1]==5
    p = "0 P1 with 10"
    replace_grade_command(l, p)
    assert l[0][0] == 10
    p = "2 P3 with 7"
    replace_grade_command(l, p)
    assert l[2][2] == 7

test_replace_grade_command()


def sort(contestants_list):
    """
    we just make a copy of our list and sort it by average grades
    :param contestants_list: the list of contestants
    :return: a copy of the list sorted
    """
    new_list=contestants_list.copy()
    avrg = calculate_avrg(new_list)
    for i in range(0,len(new_list)):
        for j in range(0,len(new_list)):
            if(avrg[i]>avrg[j]):
                new_list[i],new_list[j]=new_list[j],new_list[i]
                avrg[i],avrg[j]=avrg[j],avrg[i]
    return new_list

def test_sort():
    assert sort([[10,10,10],[5,6,4],[7,9,5]])==[[10,10,10],[7,9,5],[5,6,4]]

test_sort()

def init_contestans():
    return [create_contestant(7,5,3),create_contestant(10,8,6),create_contestant(10,4,1),create_contestant(7,5,3),create_contestant(9,8,7),create_contestant(10,7,9),create_contestant(1,1,1),create_contestant(2,8,9),create_contestant(7,4,8),create_contestant(10,10,10)]

def getpozitions(contestants_list, param):
    """
     this function is used for the command min and avg to get the positions that we need
    :param contestants_list: the list of contestants
    :param param: the parameters after the keywords "min" and "avg"
    :return: the first and last position that need be verified on the abg list
    """
    poz, word , poz2=param.split()
    if(int(poz)>=int(poz2)):
        raise ValueError
    elif int(poz)> len(contestants_list) or int(poz) <0 or int(poz2) < 0 or int(poz2)>len(contestants_list):
        raise ValueError
    else:
        return [poz,poz2]
def test_getpoztions():
    assert getpozitions([[1,2,3],[4,2,1],[9,7,6]],"0 to 1")==["0","1"]

test_getpoztions()

def min_command(contestants_list,param):
    """
    first we calculate the average of our list and then we get our positions that we need to go through and get the min
    the we go on the average list from p[0] to p[1] and calculate the min then return it
    """
    l=calculate_avrg(contestants_list)
    p = getpozitions(contestants_list, param)
    min=float(11)
    for i in range(int(p[0]), int(p[1]) + 1):
        if min>l[i]:
            min=l[i]
    return min
def test_min_command():
    assert min_command([[1,2,3],[4,2,5],[1,1,1]],"0 to 1")==2.0

test_min_command()

def avg_command(contestants_list,param):
    """
    first we calculate the average of our list and then we get our positions that we need to go through and sum
    up the averages the we return the sum divided by the number of elements
    """
    avgr=calculate_avrg(contestants_list)
    p=getpozitions(contestants_list,param)
    s=float(0)
    for i in range (int(p[0]),int(p[1])+1):
        s=s+avgr[i]
    return s/float(int(p[1])-int(p[0])+1)
def test_avg_command():
    assert avg_command([[1,2,3],[7,8,9],[5,3,7],[10,10,10]],"1 to 3")==7.6666666666666666666666

test_avg_command()

def sort_p1(contestants_list):
    """
    we just sorted the contestants by the first problem
    """
    new_list = contestants_list.copy()
    for i in range(0, len(new_list)):
        for j in range(0, len(new_list)):
            if (new_list[i][0]>new_list[j][0]):
                new_list[i], new_list[j] = new_list[j], new_list[i]
    return new_list
def sort_p2(contestants_list):
    """
    we just sorted the contestants by the second problem
    """
    new_list = contestants_list.copy()
    for i in range(0, len(new_list)):
        for j in range(0, len(new_list)):
            if (new_list[i][1] > new_list[j][1]):
                new_list[i], new_list[j] = new_list[j], new_list[i]
    return new_list
def sort_p3(contestants_list):
    """
    we just sorted the contestants by the third problem
    """
    new_list = contestants_list.copy()
    for i in range(0, len(new_list)):
        for j in range(0, len(new_list)):
            if (new_list[i][2] > new_list[j][2]):
                new_list[i], new_list[j] = new_list[j], new_list[i]
    return new_list

def top_special(contestants_list,nr,prob):
    """
    this function checks by which problem should the contestants be sorted
    """
    if(int(nr)<=0 or int(nr)>len(contestants_list)):
        raise IndexError
    if(prob=="P1"):
        return sort_p1(contestants_list)
    elif(prob=="P2"):
        return sort_p2(contestants_list)
    elif(prob=="P3"):
        return sort_p3(contestants_list)
    else:
        raise ValueError

def test_top_special():
    l = [[1, 2, 3], [6, 6, 6], [7, 5, 3],[9,9,9]]
    nr="2"
    prob="P1"
    p=top_special(l,nr,prob)
    assert p==[[9,9,9], [7, 5, 3] , [6, 6, 6],[1, 2, 3]]
    prob="P2"
    p=top_special(l,nr,prob)
    assert p == [[9, 9, 9], [6, 6, 6],  [7, 5, 3], [1, 2, 3]]
    prob="P1"
    p==top_special(l,nr,prob)
    assert p==[[9, 9, 9], [6, 6, 6], [7, 5, 3],[1, 2, 3]]
test_top_special()

def undo(stack):
    """
    we first check if the stack has a length bigger then 1 bcs if it does not have that means
    that we cant do any more undo's  then we just eliminate the top item of the stack and return the next one
    bcs that the list before the last operation was made
    """
    if(len(stack)>1):
        stack.pop()
        return stack[-1]
    else:
        raise IndexError
def test_undo():

    assert undo([[[1,2,3],[9,9,9],[5,5,5]],[[1,2,3],[9,9,9],[0,0,0]]])==[[1,2,3],[9,9,9],[5,5,5]]
test_undo()