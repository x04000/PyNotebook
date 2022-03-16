from bdb import Breakpoint
import os

info = "\x1b[38;2;0;255;116m[\x1b[0;36m!\x1b[38;2;0;255;116m] "
warning = "\x1b[38;2;255;100;0m[\x1b[0;36m!\x1b[38;2;255;100;0m] "
error = "\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] "

def logo():
    print("""\x1b[38;2;255;0;189mWelcome to \x1b[38;2;255;0;0mUltraKnife \x1b[38;2;255;0;189m| \x1b[38;2;0;255;251mPyNotebook \x1b[38;2;0;255;116mv.1.0 \x1b[38;2;255;0;189m| \x1b[38;2;35;0;255mby x04000
    \x1b[38;2;0;255;251m
    __                      ____                            ___
    \ ````''''----....____.'\   ````''''--------------------| |________________________________
    :.                                                      | |                           :    |
    '::.                                                    | |        \x1b[38;2;255;0;0mUltraKnife\x1b[38;2;0;255;251m         :    |
        '::..                                               | |        ----------         :    |
        `'-::...____________________________________________| |\_______      _____        :    |
            ```'''------------------------------------------| |        \____/     \_______:____|
                                                           /  |
                                                           |  |
                                                           |__|
    """)
def checkdir():
    try:
        f=open("Notebook/UltraKnife", "w")
        f.close()
    except:
        print(error+"Dir Notebook doesn't exists")
        print(info+"Creating dir Notebook...")
        os.system("mkdir Notebook")
        f=open("Notebook/UltraKnife", "w")
        f.close()

try:       
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    logo()
    checkdir()
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    logo()
    while(True):
        uki = str(input("\x1b[0;36mUltraKnife ❯ \x1b[38;2;0;255;251m"))
        if uki == "exit":
            print(info+"Have a nice day :)")
            break
        elif uki == "help":
            print("""[Help]
delete  - Delete a note
exit    - Exit the script
search  - Search a note
write   - Write a new note
            """)
        elif uki == "search":
            try:
                os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                logo()
                while(True):
                    uki = str(input("\x1b[0;36mSearch ❯ \x1b[38;2;0;255;251m"))
                    if uki == "exit":
                        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                        logo()
                        break
                    else:
                        checkdir()
                        try:
                            sn1 = 0
                            sn2 = 0
                            sn = str(sn1)+"-"+str(sn2)
                            while(True):
                                with open("Notebook/"+sn,"r") as archive:
                                    for line in archive:
                                        if str(line) == uki:
                                            print("["+str(line)+"]")
                                            sn2 = 1
                                            sn = str(sn1)+"-"+str(sn2)
                                            with open("Notebook/"+sn,"r") as archive:
                                                for line in archive:
                                                    print(str(line))
                                            break
                                        else:
                                            sn1 = sn1+1
                                            sn = str(sn1)+"-"+str(sn2)

                        except KeyboardInterrupt:
                            print("\n"+error+"Keyboard Interrupt")
                        except ValueError:
                            print("\n"+error+"Variable Error")
                        except:
                            print("")

            except KeyboardInterrupt:
                print("\n"+error+"KeyboardInterrupt")
            except ValueError:
                print("\n"+error+"Variable Error")
            except:
                print("\n"+error+"A unknow error ocurred")

        elif uki == "write":
            try:
                checkdir()
                os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                logo()
                uki = str(input("\x1b[0;36mWrite Title ❯ \x1b[38;2;0;255;251m"))
                if uki == "exit":
                        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                        logo()
                        break
                name0 = 0
                name1 = 0
                name = "Notebook/"+str(name0)+"-"+str(name1)
                while(True):
                    try:
                        f=open(name, "r")
                        f.close()
                        name0 = name0 + 1
                        name = "Notebook/"+str(name0)+"-"+str(name1)
                    except:
                        name = "Notebook/"+str(name0)+"-"+str(name1)
                        f=open(name, "w")
                        f.write(uki)
                        f.close()
                        name1 = 1
                        name = "Notebook/"+str(name0)+"-"+str(name1)
                        f=open(name, "w")
                        f.close()
                        break
                os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                logo()
                print("[Info] If you want to stop writing the note type '.:stop:.'\n")
                line1 = 0
                while(True):
                    uki = str(input("\x1b[0;36mWrite Note ❯ \x1b[38;2;0;255;251m"))
                    if uki == ".:stop:.":
                        break
                    else:
                        if line1 == 0:
                            f=open(name, "a")
                            f.write(uki)
                            f.close()
                            line1 = 1
                        else:
                            f=open(name, "a")
                            f.write("\n"+uki)
                            f.close()
                print(info+"Note created ;)")

            except KeyboardInterrupt:
                print("\n"+error+"KeyboardInterrupt")
            except ValueError:
                print("\n"+error+"Value Error")
            except:
                print("\n"+error+"A unknow error ocurred")
        
        elif uki == "delete":
            try:
                os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                logo()
                print("[Info] If your note doesn't has been deleted try to write a new note and try again\n")
                while(True):
                    uki = str(input("\x1b[0;36mDelete by title ❯ \x1b[38;2;0;255;251m"))
                    if uki == "exit":
                        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                        logo()
                        break
                    else:
                        checkdir()
                        try:
                            ff = 0
                            sn1 = 0
                            sn2 = 0
                            sn = str(sn1)+"-"+str(sn2)
                            while(True):
                                if ff == 1:
                                    break
                                with open("Notebook/"+sn, "r") as archive:
                                    for line in archive:
                                        if str(line) == uki:
                                            ff = 1
                                            print(info+"Deleting: ["+str(line)+"]")
                                            break
                                        else:
                                            sn1 = sn1+1
                                            sn = str(sn1)+"-"+str(sn2)

                        except KeyboardInterrupt:
                            print("\n"+error+"Keyboard Interrupt")
                        except ValueError:
                            print("\n"+error+"Variable Error")
                        except:
                            print("")

                        try:
                            if ff == 1:
                                os.remove("Notebook/"+sn)
                                sn2 = 1
                                sn = str(sn1)+"-"+str(sn2)
                                os.remove("Notebook/"+sn)
                                print(info+"Note deleted ;)")

                        except KeyboardInterrupt:
                            print("\n"+error+"Keyboard Interrupt")
                        except ValueError:
                            print("\n"+error+"Variable Error")
                        except:
                            print("")

            except KeyboardInterrupt:
                print("\n"+error+"KeyboardInterrupt")
            except ValueError:
                print("\n"+error+"Variable Error")
            except:
                print("\n"+error+"A unknow error ocurred")

except KeyboardInterrupt:
    print("\n"+error+"KeyboardInterrupt")
except ValueError:
    print("\n"+error+"Value Error")
except:
    print("\n"+error+"A unknow error ocurred")