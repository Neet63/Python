#fileobj.write(contentToWrite)  -> write to file

f = open('writefile.txt','w+')
f.write('Hello\nHow Are You???\n')
# content = input("Enter the content You want to write :")
# f.write(content)
f.close()


#Writing File in Binary Mode
f = open('binary_write.bin','wb')
content = b'Hello World!!!'
f.write(content)
f.close()

#Write to an existing file
f = open('foo.txt', 'a')
text = 'Hello World!!!'
f.write(text)
f.close()


# Writing to a File in Reading and Writing Modes
#in w or a mode cant change previous content
# so to do that we use w+ with write and read mode

#.seek() -> rewind the stream to any desired byte position
# fileObject.seek(offset[, whence])

# offset − This is the position of the read/write pointer within the file.
# whence − This is optional and defaults to 0 which means absolute file positioning, other values are 1 which means seek relative to the current position and 2 means seek relative to the file's end.
# 0 -> absolute file positioning
# 1 -> seek relative to the current position
# 2 -> eek relative to the file's end


fo=open("foo.txt","w+")
fo.write("This is a rat race")
fo.seek(10,0)  #->  Moves the file pointer/cursor to the 10th byte in the file to read.
data=fo.read(3)  # read 3 bytes
fo.seek(10,0)  #->  Moves the file pointer/cursor to the 10th byte in the file to write.
fo.write('cat')
fo.close()
