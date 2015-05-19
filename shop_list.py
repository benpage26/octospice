#! /usr/bin/env python
import re
import sys

f = open(sys.argv[1],'U')
lines = f.readlines()
x = ''.join(lines)

ingredients = re.findall(r"\[([^[]+)\]", x)

for s in [k for k in lines if k.startswith('Serves:')]:
 print s.strip()

for x in ingredients:
  print ' -',x

#todo from each ingredient take $\d+[^\w] as a 'measure' the rest as an ingredient and scale up the measure as requested
#Todo: Group ingredients based on the #step they were taken from in the prose
#Todo: Consider how to represent an 'intro' text and maybe a photo?