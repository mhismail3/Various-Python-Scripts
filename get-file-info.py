import os, sys, stat, time

fileName = input("> ")
try:
    fileStats = os.stat(fileName)
except OSError:
    print ("\nNameError : No such file or directory\n")


fileInfo = {
    'fname': fileName,
    'fsize': fileStats.st_size,
    'f_lm' : time.strftime("%d/%m/%Y %I:%M:%S %p", time.localtime(fileStats.st_mtime)),
    'f_la' : time.strftime("%d/%m/%Y %I:%M:%S %p", time.localtime(fileStats.st_atime)),
    'f_ct' : time.strftime("%d/%m/%Y %I:%M:%S %p", time.localtime(fileStats.st_ctime))
}

print (("\nfile name = {fname}, file size = {fsize} bytes, last modified = {f_lm}, " +
       "last accessed = {f_la}, creation time = {f_ct}\n").format(**fileInfo))

if stat.S_ISDIR(fileStats.st_mode):
    print ("This a directory")
else:
    print ("This is not a directory\n")
    print ("A closer look at the os.stat({}) tuple:".format(fileName))
    print (fileStats)
    print ("\nThe above tuple has the following sequence:")
    print ("""st_mode (protection bits), st_ino (inode number),
    st_dev (device), st_nlink (number of hard links),
    st_uid (user ID of owner), st_gid (group ID of owner),
    st_size (file size, bytes), st_atime (last access time, seconds since epoch),
    st_mtime (last modification time), st_ctime (time of creation, Windows)"""
)
