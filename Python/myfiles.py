bufferobj = open('farahaha.txt')

readfile = bufferobj.read()
bufferobj.close()

readfile = readfile.upper()
#breakpoint()
bufferobj = open('farahaha.txt','w')

bufferobj.write(readfile)
bufferobj.close()
