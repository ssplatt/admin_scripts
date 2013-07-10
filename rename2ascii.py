#!/usr/bin/python
import os, sys, getopt
def main(argv):
    inputdir = ''
    try:
        opts, args = getopt.getopt(argv, "")
    except getopt.GetoptError:
        print 'usage: rename2ascii.py <inputdir>'
        sys.exit(2)
    for arg in args:
		if os.path.isdir(arg):
			inputdir = arg
		else:
			print 'usage: rename2ascii.py <inputdir>'
			sys.exit()
            
    for file in os.listdir(inputdir):
		print "checking: ", file.encode('utf8')
		new_file = ''
		for i in file:
			if ord(i) < 128:
				new_file = new_file + i
			else:
				new_file = new_file + '_'
		if (file != new_file) and (os.path.isfile(file) or os.path.isdir(file)) :
			print u"Renaming", file.encode('utf8'),u" to ", new_file.encode('utf8')
			os.rename(file, new_file)
		else:
			print "skipping: ", file.encode('utf8')

if __name__ == "__main__":
   main(sys.argv[1:])