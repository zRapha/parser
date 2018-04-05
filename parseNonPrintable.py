#================================================================================#
# A simple parser to find a flag in a ZIP bomb containing non-printable chars    #
# Parsing time around 2.5M lines per Minute - 167M: ~1 Std (Kali VM - i7/4GB)    #
#================================================================================#

from datetime import datetime
import re

def parseNonPrintable():
	try: 
		startTime = datetime.now()
		lines = 167000000 # Manually adding for efficiency reasons
		with open('file', 'r') as inp, open('flag.txt', 'a') as outp:
	    		for line in inp:	
				clean_line = re.sub(r'\xa0','',line).decode('utf-8','ignore').strip()
				outp.write(clean_line)
				lines -= 1  			
				print 'Remaining lines:', lines
		outp.close(); inp.close()
		print 'Time needed to process:', datetime.now() - startTime		
		outputfile = open('flag.txt', 'r') 
    print 'The potential flag is:', outputfile.read()
	except IOError:
		print 'Error with the file, call mom'

if __name__ == "__main__":
    parseNonPrintable() 
