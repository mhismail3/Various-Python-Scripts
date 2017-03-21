import os, sys

try:
    directory = sys.argv[1]
except IndexError:
    sys.exit("Must provide an argument.")

dir_size = 0
fsizedicr = {'Bytes': 1,
             'Kb': 1.0 / 1024,
             'Mb': 1.0 / 1024**2,
             'Gb': 1.0 / 1024**3}

for path, dirs, files in os.walk(directory):
    for file in files:
        dir_size += os.path.getsize(os.path.join(path, file))

fsizeList = [str(round(fsizedicr[key] * dir_size, 4)) + " " + key for key in fsizedicr]

if dir_size == 0: print ("File Empty")
else:
    for units in sorted(fsizeList)[::-1]:
        print ("Folder Size: " + units)
