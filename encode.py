#! /usr/bin/env python

import sys
import ntpath
# TODO - Check Error No Such File Or Directory
print "..:: Subtitles Encoder ::.."
print "By George Sofianos<georgesofianosgr@gmail.com>"
print "Encode Subtitles From Windows-1253(Greek) To UTF-8\n"

if(len(sys.argv) > 1):
        print "Please Wait, Encoding\n"
        # Remove ' and " from path if exist
        path = sys.argv[1].replace("'","")
        path = path.replace('"',"")
        newPath = ntpath.split(path)[0] + "/Enc-" + ntpath.basename(path)
        fr = open(path,"rb")
        fw = open(newPath,"w")
        byte = fr.read(1)
        while byte != "":
                decByte = byte.decode("windows-1253")
                encByte = decByte.encode("utf8")
                fw.write(encByte)
                byte = fr.read(1)
        
        print "Encode Complete"  
        print "Encoded File: " + ntpath.basename(newPath)      
        fr.close()
        fw.close()
else:
        print "Usage: subsEncode PATH_TO_FILE"
    
