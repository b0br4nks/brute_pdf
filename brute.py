import pikepdf

from tqdm import tqdm

key = [x.strip() for x in open("keylist.txt")]

name_file = input("\033[1;36;40m[?]Enter the name of the file: ")

for z in tqdm(key, "\033[1;33;40m[?]Brute-force in progress..."):
    try:
        with pikepdf.open(name_file+".pdf", password=z) as pdf:
            print("\n\n\n\033[1;35;40m[!]Cracked key:", z+ "\n\n")
            close = input("\033[1;36;40m[?]Save the cracked file? (y/n): ")
            if close == "y":
                pdf.save(name_file+"-cracked.pdf")
                print("\033[1;35;40m[!]File saved as: "+name_file+"-cracked.pdf\n\n")
                break
            else:
                print("\033[1;35;40m[!]File not saved\n\n")
                exit()
    except pikepdf._qpdf.PasswordError as e:
        continue