import urllib2, re, operator # the lib that handles the url stuff


#data = urllib2.urlopen(f)

import sys, os

#"Usage message" if input < 2
if len(sys.argv) < 2:
	sys.exit("Usage: %s filename" % sys.argv[0])

# Formatted Syntax for input: "python module4*.py battingStats1940.txt"
filename = sys.argv[1]

# If you haven't specified a file-path to reach filename (or it isn't stored locally with battingAvg.py) print "Error message" 
if not os.path.exists(filename):
	sys.exit("Error: File '%s' not found" % sys.argv[1])

# Open the file for reading
f = open(filename)

magicLine = re.compile("(?P<name>[A-Z]\w*\s[A-Z]\w*)\s\w*\s(?P<bats>\d)\s\w*\s\w*\s(?P<hits>\d)\s\w*\s\w*\s(?P<runs>\d)\s\w*")

batsDictionary = {}
hitsDictionary = {}
runsDictionary = {}
battingAverages = {}

for line in f:
        if re.search('(runs)', line):
                name = re.match(magicLine, line).group('name')
                if name in batsDictionary:
                        batsDictionary[name] += float(re.match(magicLine, line).group('bats'))
                        hitsDictionary[name] += float(re.match(magicLine, line).group('hits'))
                        runsDictionary[name] += float(re.match(magicLine, line).group('runs'))
                else:
                        batsDictionary[name] = float(re.match(magicLine, line).group('bats'))
                        hitsDictionary[name] = float(re.match(magicLine, line).group('hits'))
                        runsDictionary[name] = float(re.match(magicLine, line).group('runs'))

for name in batsDictionary:
        battingAverages[name] = round(float(hitsDictionary[name]/batsDictionary[name]), 3)  

sorted_averages = sorted(battingAverages.items(), key=operator.itemgetter(1))        
for i in reversed(sorted_averages):
        if len(str(i[1])) <= 4:
                print str(i[0]) + ": " + str(i[1]) + "0"
        else: print str(i[0]) + ": " + str(i[1])


f.close()