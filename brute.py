import pikepdf

from tqdm import tqdm

mag = "\033[0;35;40m"
cya = "\033[0;36;40m"
yel = "\033[0;33;40m"
whi = "\033[1;37;40m"

print(f"""{mag}
██████  ██████  ██    ██ ████████ ███████         ██████  ██████  ███████ 
██   ██ ██   ██ ██    ██    ██    ██              ██   ██ ██   ██ ██      
██████  ██████  ██    ██    ██    █████           ██████  ██   ██ █████   
██   ██ ██   ██ ██    ██    ██    ██              ██      ██   ██ ██      
██████  ██   ██  ██████     ██    ███████ ███████ ██      ██████  ██      
""")

key = [x.strip() for x in open("keylist.txt")]

name_file = input(f"{cya}[?]Enter the name of the file: ")

for z in tqdm(key, f"{yel}[?]Brute-force in progress..."):
    try:
        with pikepdf.open(name_file+".pdf", password=z) as pdf:
            print(f"\n\n\n{mag}[!]Cracked key:", f"{whi}{z}\n\n")
            close = input(f"{cya}[?]Save the cracked file? (y/n): ")
            if close == "y":
                pdf.save(name_file+"-cracked.pdf")
                print(f"{mag}[!]File saved as: "+name_file+"-cracked.pdf\n\n")
                break
            else:
                print(f"{mag}[!]File not saved\n\n")
                exit()
    except pikepdf._qpdf.PasswordError as e:
        continue
