import requests # add via pip
import random
from random import randrange
import threading # add via pip
import string
import time
from os import system, name
from colorama import Fore, Back, Style # add via pip

logo = """  _   _ _ _             _                _       
 | \ | (_) |           | |              | |      
 |  \| |_| |_ _ __ ___ | |__  _ __ _   _| |_ ___ 
 | . ` | | __| '__/ _ \| '_ \| '__| | | | __/ _ \\
 | |\  | | |_| | | (_) | |_) | |  | |_| | ||  __/
 |_| \_|_|\__|_|  \___/|_.__/|_|   \__,_|\__\___|
 \t\t\t\tdeveloped by mayce 2021""";
url = "https://discordapp.com/api/v6/entitlements/gift-codes/NITROCODE?with_application=false&with_subscription_plan=true";

def clearScreen(): # clear console according to os
    if name == 'nt':
        _ = system('cls');
    else:
        _ = system('clear');

def mesh(): # generate code mesh
    cipher = "OGIHjFkDa9AosyQzLrfSmp3tT0Kc1N4iWwdRhubnPe27JqxlEUBYvZ8g5CM6XV";
    cipher_upkeep = ''.join(random.sample(cipher, len(cipher)));
    code_from_cipher = ''.join(random.choices(
            cipher_upkeep,
            k = 16
        ));
    return code_from_cipher;       

def method(id, thread_name, selection): # run api checks on mesh
    if selection == 1:
        _t = True;
        while(_t):
            headers = {"User-Agent": mesh(),
                        "Device-Memory": mesh(),
                        "Content-DPR": mesh(),
                        "DPR": mesh(),
                        "Viewport-Width": randrange(1920),
                        }
            rt = mesh();
            url_with_token = url.replace("NITROCODE", rt);
            code_request = requests.get(url_with_token, headers);
            if "limited" in code_request.json()['message']:
                _t = False;
                print("[" + thread_name + "]" + Fore.RED + " > RATE LIMITED : " + Style.RESET_ALL + "[" + Fore.YELLOW + rt + Style.RESET_ALL + "]");
                input("Press restart the app or Ctrl+C...");
                exit
            elif "unknown" in code_request.json()['message']:
                print("[" + thread_name + "]" + Fore.ORANGE + " > Nitro Code Invalid : " + Style.RESET_ALL + "[" + Fore.YELLOW + rt + Style.RESET_ALL + "]");
            else:
                _t = False;
                print("[" + thread_name + "]" + Fore.GREEN + " > Possible Nitro Code Found: " + rt + Style.RESET_ALL);
                
                input("Press restart the app or Ctrl+C....");
                exit
                
    elif selection == 2:
        _t = True;
        limit = int(input(Fore.BLUE + "How many valid codes to gather: " + Fore.CYAN));
        print(Style.RESET_ALL + "\n");
        while(_t):
            gathered = [];
            rt = mesh();
            url_with_token = url.replace("NITROCODE", rt);
            code_request = requests.get(url_with_token);
            if code_request.status_code == 200:
                gathered.append(rt);
                print(Fore.BLUE + "[" + thread_name + "]" + Fore.GREEN + " > Nitro Code Found: " + rt + Style.RESET_ALL);
            else:
                print(Fore.BLUE + "[" + thread_name + "]" + Fore.RED + " > Nitro Code Invalid : " + Style.RESET_ALL + "[" + Fore.YELLOW + rt + Style.RESET_ALL + "]");

            if len(gathered) >= limit:
                print(Fore.BLUE + "[" + thread_name + "]" + Fore.GREEN + " >>> Finished" + Style.RESET_ALL + "\n");
                input("Press any key to exit...");
                main();
    elif selection == 3:
        exit
    else:
        main();
    

def main(): # main handle
    clearScreen();
    
    print(Fore.BLUE + logo + Style.RESET_ALL + "\n\n");

    print(Fore.CYAN + "Please select one of the following options:" + Style.RESET_ALL);
    print("\n\n");
    print(Fore.BLUE + "\t[1] Run until 1 code is found\n");
    print("\t[2] Run until X codes are found\n");
    print("\t[3] Run indefinitely (log valid codes in file)" + Style.RESET_ALL + "\n");
    
    selection = int(input("\nSelection > " + Fore.CYAN));
    print(Style.RESET_ALL);
    
    # threading
    global threadStack;
    threadStack = [];
    for x in range(50):
        tempthread = threading.Thread(target = method, args=(x, Style.RESET_ALL + "Thread " + Fore.GREEN + "#" + Fore.BLUE + str(x) + Style.RESET_ALL, selection));
        tempthread.start();
        threadStack.append(tempthread);

main();

