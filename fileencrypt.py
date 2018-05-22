#!/usr/bin/python3

import sys
import encryptdecrypt as ENC

#define the input. The input file is as the first commandline argument, the second 
#argument is defined as ouput file, third is key 
ARG_infile=1
ARG_outfile=2
ARG_key=3
ARG_length=4

def covertfile(infile,outfile,key):
    try:
        enc_key=int(key)  #key used in encrytion must be a integer
    except:
        print ("Error: the key %s must be an integer" % (key))
    else:
        try:
            with open(infile) as file_in: 
#with open() gives better syntax and exceptions handling, it automatically clean up 
                infile_content=file_in.readlines()
        except:
            print ("Unable to open %s" % (infile))
        try:
            with open(outfile,'w') as file_out:
                for line in infile_content:
                    out_line = ENC.encryptText(line,enc_key)
                    file_out.writelines(out_line)
        except:
            print ("unable to open %s" % (outfile))
        print ("conversion complete : %s" % (outfile))
    finally:
        print ("Finish")

#test 
if len(sys.argv) == ARG_length: #make sure it's given all the argument required
    print ("command: %s" % (sys.argv))
    covertfile(sys.argv[ARG_infile], sys.argv[ARG_outfile], sys.argv[ARG_key])
else:
    print ("Please enter fileencrypt.py infile outfile key in order")
#END
    
                 

