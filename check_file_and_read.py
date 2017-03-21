import sys, os


def main():
    if len(sys.argv) < 2:
        print('[-] Usage: python check_file.py <filename1> [filename2] ... [filenameN]')
        exit(0)
    
    for filename in sys.argv[1:]:
        if not os.path.isfile(filename):
            print ('[-] ' + filename + ' does not exist.')
            continue

        if not os.access(filename, os.R_OK):
            print ('[-] ' + filename + ' access denied')
            continue
        
        print ('[+] Reading from : ' + filename)
        with open(filename, 'r') as f: print(f.read())


if __name__ == '__main__':
    main()
