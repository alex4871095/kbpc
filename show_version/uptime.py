import re

def obtain_uptime( data_string ):
        uptime = re.search(r"uptime is (.+)\n", data_string)
        if uptime:
                up = "uptime is " + uptime.group(1)
                return up
        else:
                return None

def main():
        with open("../show_version.txt") as show_ver_file:
                show_ver = show_ver_file.read()
        print obtain_uptime(show_ver)

if __name__ == '__main__':
        main()

