import re

def obtain_model( data_string ):
        model = re.search(r"Cisco (.+?) (.+?) processor", data_string)
        if model:
                mod = model.group(1)
                return mod
        else:
                return None

def main():
        with open("../show_version.txt") as show_ver_file:
                show_ver = show_ver_file.read()
        print obtain_model(show_ver)

if __name__ == '__main__':
        main()

