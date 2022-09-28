import re

def main():
    with open("log.txt", 'r+', encoding='utf8') as f:
        for line in f:
            print(line)

            m = re.search(r'(PORT|Port|port)(: | |:")(\d{1,5})', line)

            if m:
                print("Port: {} found!".format(m[3]))
            
                
if __name__ == "__main__":
    main()


