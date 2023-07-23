import os
import shutil
import random
print("=========================================")
print("            Welcome to NovaDOS           ")
print("=========================================")
print("  Type 'help' to see the list of commands ")
print("=========================================")
def separator(name):
    os.system("cls")
    print("+--------------- " + name + " ---------------+")

def edit():
    file = input("Which file do you want to edit? ")
    with open(file, 'a') as f:
        filetext = input("Enter the text to add to the file: ")
        f.write(filetext + "\n")

def fopen():
    separator("Opening File")
    file = input("Open: ")
    print("")
    with open(file, 'r') as f:
        for line in f:
            print(line)
            print("")
    editredirect()

def editredirect():
    separator("Editing")
    print("You can edit this file with the 'edit' command.")
    dcmdLvl2()

def cr():
    directoryName = input("Name of directory: ")
    os.mkdir(directoryName)

def rmdir():
    directoryName = input("Name of directory to remove: ")
    try:
        os.rmdir(directoryName)
    except OSError as e:
        print(f"Error: {e}")

def mv():
    source = input("Enter the source file/directory: ")
    destination = input("Enter the destination directory: ")
    shutil.move(source, destination)

def cp():
    source = input("Enter the source file/directory: ")
    destination = input("Enter the destination directory: ")
    shutil.copy(source, destination)

def cat():
    file = input("Enter the file to display: ")
    with open(file, 'r') as f:
        content = f.read()
        print(content)

def help():
    print("Available commands:")
    print("edit - Edit a file and add text to it")
    print("mkdir - Create a new directory")
    print("rmdir - Remove an empty directory")
    print("mv - Move a file or directory")
    print("cp - Copy a file or directory")
    print("cat - Display the contents of a file")
    print("number - Generate a random number between 1 and 100")
    print("help - Show available commands")

def cmdLvl2():
    separator("NovaDOS")
    print("Use the 'leave' command to shut down the system. Use the 'type' command to start a text editor. You can also type 'clear' to clear the screen. Type 'help -a' for more options.")
    tcmdLvl2 = input("~$: ")
    if tcmdLvl2 == "leave":
        quit()
    elif tcmdLvl2 == "type":
        typer()
    elif tcmdLvl2 == "clear":
        os.system('cls')
    elif tcmdLvl2 == "":
        dcmdLvl2()
    elif tcmdLvl2 == "help -a":
        help()
        dcmdLvl2()
    elif tcmdLvl2 == "cr":
        cr()
    elif tcmdLvl2 == "cd":
        cd()
    elif tcmdLvl2 == "list":
        os.system('dir')
    elif tcmdLvl2 == "show":
        print(os.getcwd())
    elif tcmdLvl2 == "rem":
        rem()
    elif tcmdLvl2 == "open":
        fopen()
    elif tcmdLvl2 == "edit":
        edit()
    elif tcmdLvl2 == "cat":
        cat()
    elif tcmdLvl2 == "mv":
        mv()
    elif tcmdLvl2 == "cp":
        cp()
    elif tcmdLvl2 == "number":
        generate_number()
        dcmdLvl2()
    elif tcmdLvl2 == "help":
        help()
    elif tcmdLvl2 == "user":
        user()
    else:
        print("Command not found.")
    dcmdLvl2()

def dcmdLvl2():
    separator("NovaDOS")
    tcmdLvl2 = input("~$: ")
    if tcmdLvl2 == "leave":
        quit()
    elif tcmdLvl2 == "type":
        typer()
    elif tcmdLvl2 == "clear":
        os.system('cls')
    elif tcmdLvl2 == "":
        dcmdLvl2()
    elif tcmdLvl2 == "help":
        help()
    elif tcmdLvl2 == "cr":
        cr()
    elif tcmdLvl2 == "cd":
        cd()
    elif tcmdLvl2 == "list":
        os.system('dir')
    elif tcmdLvl2 == "show":
        print(os.getcwd())
    elif tcmdLvl2 == "rem":
        rem()
    elif tcmdLvl2 == "open":
        fopen()
    elif tcmdLvl2 == "edit":
        edit()
    elif tcmdLvl2 == "cat":
        cat()
    elif tcmdLvl2 == "mv":
        mv()
    elif tcmdLvl2 == "cp":
        cp()
    elif tcmdLvl2 == "number":
        generate_number()
        dcmdLvl2()
    elif tcmdLvl2 == "help -a":
        help()
        dcmdLvl2()
    elif tcmdLvl2 == "user":
        user()
    else:
        print("Command not found.")
    dcmdLvl2()

def typer():
    separator("Typer")
    print("Start typing to begin.")
    typerCMD = input("  ")
    saveAs = input("Save file as: ")
    if saveAs == "":
        dcmdLvl2()
    with open(saveAs, 'w') as f:
        f.write(typerCMD)
    print("You can access this file with the 'open' command.")
    dcmdLvl2()

def generate_number():
    random_number = random.randint(1, 100)
    print("Generated number:", random_number)

def CMDLine():
    separator("NovaDOS")
    print("Hello, and welcome to NovaDOS. Type 'help' to get started.")
    cmd = input("~$: ")
    if cmd == "leave":
        quit()
    elif cmd == "type":
        typer()
    elif cmd == "clear":
        os.system('cls')
    elif cmd == "":
        dcmdLvl2()
    elif cmd == "help":
        help()
    elif cmd == "cr":
        cr()
    elif cmd == "cd":
        cd()
    elif cmd == "list":
        os.system('dir')
    elif cmd == "show":
        print(os.getcwd())
    elif cmd == "rem":
        rem()
    elif cmd == "open":
        fopen()
    elif cmd == "edit":
        edit()
    elif cmd == "cat":
        cat()
    elif cmd == "mv":
        mv()
    elif cmd == "cp":
        cp()
    elif cmd == "number":
        generate_number()
    elif cmd == "user":
        user()
    else:
        print("Command not found.")
    dcmdLvl2()

def redirect():
    signIn()

def mUserRedirect():
    makeUser()

def PwordSignIn():
    rPword = input("Password: ")
    with open('passwords.txt', 'r') as f:
        for line in f:
            if rPword == line.strip():
                CMDLine()
                return
    print("Incorrect password.")
    signIn()

def signIn():
    separator("Sign In")
    rUname = input("Username: ")
    with open('usernames.txt', 'r') as f:
        for line in f:
            if rUname == line.strip():
                PwordSignIn()
                return
    print("Username not found.")
    mUserRedirect()

def makeUser():
    separator("New User")
    nUname = input("New username: ")
    nPword = input("Create a password for the user: ")

    with open('usernames.txt', 'w') as f:
        f.write(nUname + "\n")
    with open('passwords.txt', 'w') as f:
        f.write(nPword + "\n")
    signIn()

def start():
    print("Create a new user? Warning: This will delete any other users. (Y/N): ")
    nUser = input(" ")
    if nUser.lower() == "n":
        signIn()
    elif nUser.lower() == "y":
        makeUser()
    elif nUser == "Sarel":
        print("Sarel is a really great Dev. He knows how to use Python perfectly and he likes Synthwave music.")
        start()
    elif nUser == "Sfaltrax":
        print("Sfaltrax is a YouTuber and dev, passionate about video games and programming languages. He is from the Studio Dev Team.")
        start()
    else:
        start()

os.system("cls")
start()
