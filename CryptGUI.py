from cryptography.fernet import Fernet
from tkinter import *
from tkinter.ttk import *
import os

root = Tk()
root.title("CryptIN")
root.geometry('253x320')



# Encrypt a file.
def EnCry():
    wert = L1.get(L1.curselection())
    wert = wert + ".cry"
    
    file = open(wert, 'rb')
    key = file.read()
    file.close()

    cipher = Fernet(key)

    print("Encrypt")
    openF = NameF.get().replace('\\','/')
    NameF.delete(0, END)

    targetF = open(openF, 'rb')
    cryText = targetF.read()
    targetF.close()

    encrypted_text = cipher.encrypt(cryText)

    targetF = open(openF, 'wb')
    targetF.write(encrypted_text)
    targetF.close()
    pass


# Decrypt a file. 
def DeCry():
    wert = L1.get(L1.curselection())
    wert = wert + ".cry"
    
    file = open(wert, 'rb')
    key = file.read()
    file.close()

    cipher = Fernet(key)

    print("Decrypt")
    openF = NameF.get().replace('\\','/')
    NameF.delete(0, END)

    targetF = open(openF, 'rb')
    cryText = targetF.read()
    targetF.close()

    decrypted_text = cipher.decrypt(cryText)

    targetF = open(openF, 'wb')
    targetF.write(decrypted_text)
    targetF.close()
    pass


# File ending: .cry
def finde():
    cwd = os.path.dirname(os.path.realpath(__file__))
    
    fileDir = cwd
    fileExt = r".cry"
    files = [_ for _ in os.listdir(fileDir) if _.endswith(fileExt)]
    
    for l in files:
        l = l.replace('.cry', "")
        L1.insert('end', l)
        # print(l)

def cloSe():
    root.destroy()
    
def NewKey():
    KeyN = Toplevel(root)
    KeyN.title("New Key")
    KeyN.geometry('175x70')
    
    def GENkey():
        file = NameK.get().replace('\\','/')
        file = file + ".cry"
        key = Fernet.generate_key()

       	# print(key)
#
        file = open(file, 'wb')
        file.write(key) # key type bytes
        file.close()
        
        L1.delete(0, END)
        finde()
        
        NameK.delete(0, END)
        pass
    
    def dell():
        file = NameK.get().replace('\\','/')
        file = file + ".cry"
        
        if os.path.exists(file):
            os.remove(file)
            
            L1.delete(0, END)
            finde()
            
            NameK.delete(0, END)
        else:
            NameK.delete(0, END)
            pass
    
    
    Label(KeyN, text= "Name:").grid(row= 1,column= 1)
    NameK = Entry(KeyN, width= 15)
    NameK.grid(row= 1,column= 2)
    
    
    Button(KeyN, text= "Generate", command= GENkey).grid(row= 2,column= 2)
    Button(KeyN, text= "Deleted", command= dell).grid(row= 2,column= 1)
    

Button(root, text= "Exit...", command= cloSe).grid(row= 1,column= 1)
Button(root, text= "Encrypt", command= EnCry).grid(row= 1,column= 2)
Button(root, text= "Decrypt", command= DeCry).grid(row= 1,column= 3)

Label(root, text= "").grid(row= 2,column= 1)
Label(root, text= "Keys:").grid(row= 3,column= 1)
L1 = Listbox(root, selectmode='browse', width=16, height=10)
L1.grid(row= 3,column= 2)

Label(root, text= "").grid(row= 4,column= 2)

Label(root, text= "FileName:").grid(row= 5,column= 1)
NameF = Entry(root, width= 15)
NameF.grid(row= 5,column= 2)

Label(root, text= "").grid(row= 6,column= 1)
Button(root, text= "New/Del Key", command= NewKey).grid(row= 7,column= 2)

finde()

root.mainloop()