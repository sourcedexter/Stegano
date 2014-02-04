# version 7.0
# author : Akshay Pai

import re
import string
import base64 
import random
from colorama import init
from termcolor import colored
from loremipsum import get_paragraphs,get_sentences

bin1 = []
flag = 0

def bedazzle_green(c):
    c = c.upper()
    c = '\033[1m'+ colored(c, 'green') + '\033[0m'
    return c

def bedazzle_blue(c):
    c = c.upper()
    c = '\033[1m'+ colored(c , 'blue') + '\033[0m'
    return c

def bedazzle_black(c):
    c = '\033[1m'+ colored(c , 'grey') + '\033[0m'
    return c
 
def gen_para():
    return str((get_paragraphs(1)[0])).lower() 

def gen_sent():
    return str((get_sentences(1)[0])).lower() 

def get_other1(): 
    sent1 = ['wapiti zero karuntuk zesta un goloto korem xerata.'
             ,'zerita kument xerolo mokatilo rewastra.','tukutoro yeswara zetolomento likumhaja frtsxtarxa.']
    choi = random.randint(1,3)
    return str((sent1[choi-1])).lower()

def get_other2(j): 
    punct = string.punctuation
    num = '0123456789'
    if j.isdigit():
        return num
    elif j in string.punctuation:
        return punct

def encrypt_data(data): 
    data1 = str(data)
    data2 = base64.b64encode(data1)
    data3 = base64.b64encode(data2)
    return data3

def decrypt_data(data):
    data1 = base64.b64decode(data)
    data2 = base64.b64decode(data1)
    data3 = eval(data2)
    return data3
    

def file_to_list(file_name):
    f = open(file_name)
    buffers = []
    for lines in f:
        buffers.append(lines)
    return buffers

def file_to_str(fname):
    with open (fname, "r") as myfile:
        data=myfile.read().replace('\n', ' ')
        data = (data.strip())
    return data.lower() 

def word_count(var):
    wrdcount = 0
    for i in var.split():
        eawrdlen = len(i) / len(i)
        wrdcount = wrdcount + eawrdlen
    return wrdcount

def make_file(got_data): 
    f = open('secretdata.txt','w')
    f.writelines(got_data)
    f.close()

def put_key(key):  
    f = open('secretdata.txt', 'a')
    f.writelines("\nkey\n")
    f.writelines(key)
    f.close()
def check_file(fi_name):  # function added
    lis1 = file_to_list(fi_name)
    len01 = len(lis1)
    if lis1[len01 - 2] == 'key\n':
        return lis1[len01 - 1]
    else:
        return 'false'

def handle_file(val):    #function added 
    if val == 'false':
        print("key not present in the file")
        print("press 1. enter key manually   ctrl+c to abort")
        choice = raw_input()
        while(choice != '1'):
            print("\n\nWrong input. Enter 1 or ctrl+c to exit.\n")
            choice = raw_input()
        print("enter the key")
        key_val = raw_input()
        data = decrypt_data(key_Val)
        return data
    else:
        data = decrypt_data(val)
        return data
        
    
def disp_message(val01, file_name):
    f = open(file_name,'r')
    data = f.readlines()
    f.close()
    str01 = str(data[0])
    str02 = ''
    for each in val01:
        #print each
        for single in each:
            #print single
            str02 = str02 + str01[single]
        str02 = str02 + ' '
    print("the hidden message in the data is:")
    print(str02)
    
    print("\n\npress 1. to see hidden data visualisation or  ctrl+c to terminate")
    cho = raw_input()
    if cho == '1':
        print(show_data(str01,1,val01))

def get_data():
    while(True):
        print ("select: \n1) to enter as text \n2) to accept datafrom file ")
        choice = raw_input()
        if choice == '1':
            print ("enter the text")
            text1 = raw_input()
            return text1.lower()
        elif choice == '2':
            print ("enter the name of the text file:")
            text1 = raw_input()
            data = file_to_str(text1)
            return data
        else:
            print ("not a valid choice. press ctrl+c to end or reenter a valid choice")

def hide_data(val_one): 
    data = val_one
    g_master = ''
    #print data
    data2 = []
    str1 = []
    temp = []
    g = ''
    data2 = data.split(' ')
    other = ['k','w','x','z'] 
    #print data2
    for i in range(len(data2)):
        d2 = data2[i]
        for j in d2:
            if j in other: 
                g = get_other1()
            elif j.isdigit() or j in string.punctuation:
              g = get_other2(j)
            else:
                while j not in g:
                    g = gen_sent()
            ind1 = g.find(j)
            ind1 = ind1 + len(g_master)
            g_master = g_master + g
            temp.append(ind1)
        bin1.append(temp)
        temp = []
        g= ''
    return  g_master

def show_data(gg_master,fl=flag,key1=bin1):
    if fl == 1:
        bin2 = key1
    else:
        bin2 = bin1
    str_fi = ""
    gmaster = gg_master 
    #print(gmaster)
    first = 0
    last = 0
    for h in range(len(bin2)):
        d1 = bin2[h]
        last = d1[-1]
        if h%2 == 0:
            for f in range(first,last+1):
                if f in d1:
                    ch = bedazzle_green(gmaster[f])
                    str_fi = str_fi + ch
                else :
                    ch = bedazzle_black(gmaster[f])
                    str_fi = str_fi + ch
        else:
            for f in range(first,last+1):
                if f in d1:
                    ch = bedazzle_blue(gmaster[f])
                    str_fi = str_fi + ch
                else :
                    ch = bedazzle_black(gmaster[f])
                    str_fi = str_fi + ch
        first = last
    for f in range(last,len(gmaster)):
        ch = bedazzle_black(gmaster[f])
        str_fi = str_fi + ch
    #print (str_fi)    
    return str_fi              

def main():
    print("1.create a hidden data  2. view an existing hidden data") #added
    choice3 = raw_input()  #added
    while(choice3 !='1' and choice3 !='2'):   #while loop added
        print("\n\nWrong input. Enter 1 or 2 or ctrl+c to exit.\n")
        choice3 = raw_input()
    if choice3 == '2':   # if loop added
        print("enter file name:")
        file_name = raw_input()
        val01 = check_file(file_name)
        val02 = handle_file(val01)
        disp_message(val02,file_name)
    else:
        info1 = get_data()
        info2 = hide_data(info1)
        make_file(info2)
        key = encrypt_data(bin1)
        print ("the key:\n\n " + key)
        print ("\n\n")
        print("The data is hidden within the generated text.")
        print("The text is stored in the file \"secretdata.txt\"")
        print("Do you want to store the key to decrypt the the message inthe file?")
        print("Enter 'y' for yes and 'n' for no")
        choice = raw_input()
        while(choice != 'y' and choice != 'n'):
            print("\n\nWrong input. Enter y or n or ctrl+c to exit.\n")
            choice = raw_input()
        if choice == 'y':
            put_key(key)
            print ("\nDone.\n\n")
        else:
            pass
        while(True):
            print("\n\n1.show the text  2.show visualisation  or ctrl+c to exit\n\n")
            choice2 = raw_input()
            while(choice2 !='1' and choice2 !='2'):
                print("\n\nWrong input. Enter 1 or 2 or ctrl+c to exit.\n")
                choice2 = raw_input()
            if choice2 == '1':
                print(info2)
            else:
                print(show_data(info2))

main()
            
        








