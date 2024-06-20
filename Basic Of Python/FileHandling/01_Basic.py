name = input("Enter anuything: ")
#is equivalent to
import sys
name = sys.stdin.readline()

print (name)
#is equivalent to
import sys
sys.stdout.write(name)


#Create File Object
# file object = open(file_name [, access_mode][, buffering])


#Accessmode
# r: Read-only, pointer at the beginning (default mode).
# rb: Read-only in binary, pointer at the beginning (default mode).
# r+: Read and write, pointer at the beginning.
# rb+: Read and write in binary, pointer at the beginning.
# w: Write-only, truncates file or creates new.
# wb: Write-only in binary, truncates file or creates new.
# w+: Write and read, truncates file or creates new.
# wb+: Write and read in binary, truncates file or creates new.
# a: Append-only, pointer at the end, creates new if not exists.
# ab: Append-only in binary, pointer at the end, creates new if not exists.
# a+: Append and read, pointer at the end, creates new if not exists.
# ab+: Append and read in binary, pointer at the end, creates new if not exists.
# x: Exclusive creation, fails if file exists.
# b: Binary mode.
# t: Text mode (default).
# +: Updating (read and write).

# Open a file
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not: ", fo.closed)
print ("Opening mode: ", fo.mode)
fo.close()