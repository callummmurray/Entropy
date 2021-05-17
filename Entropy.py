
import randomdotorg
import random
import urllib
import urllib2
import threading       
_LOCK = threading.Lock() 

r = randomdotorg.RandomDotOrg('calmur8@gmail.com')
r.get_quota()

print r.get_quota()

c = ['c','c','g','c','e','g','bf','c','d','e','fs','g','af','bf','c']
cs = ['cs','cs','af','cs','f','a','b','cs','ef','f','g','af','a','b','c','cs']
d = ['d','d','a','d','fs','a','c','d','e','fs','af','a','bf','c','cs','d']
ef = ['ef','ef,','bf','ef','g','bf','cs','ef','f','g','a','bf','b','cs','d','ef']
e = ['ef','ef','bf','ef','g','bf','cs','ef','f','g','a','bf','b','cs','d','ef']
f = ['f','f','c','f','a','c','ef','f','g','a','b','c','cs','ef','e','f']
fs = ['fs','fs','cs','fs','bf','cs','e','fs','af','bf','c','cs','d','e','f','fs']
g = ['g','g','d','g','b','d','f','g','a','b','cs','d','ef','f','fs','g']
af = ['af','af','ef','af','c','ef','fs','af','bf','c','d','ef','e','fs','g','af']
a = ['a','a','e','a','cs','e','g','a','b','cs','ef','e','f','g','af','a']
bf = ['bf','bf','f','bf','d','f','af','bf','c','d','e','f','fs','af','a','bf']
b = ['b','b','fs','b','ef','f','a','b','c','ef','f','fs','g','a','bf','b']

notelist = c,cs,d,ef,e,f,fs,g,af,a,bf,b

def common_harmonics (a,b):
	a_series = set(a)
	b_series = set(b)

	if (a_series & b_series):
		print(a_series & b_series)
	else: 
		print('no common harmonics')	

piece_duration = 0
event_number = 1
orientation = ['(forwards)','(backwards)']
timbre = ['-reverb-','-bitcrusher-','-distortion-']

#section 1 

print '\nSECTION 1\n'

l = 8
u = 10

while piece_duration <= 225:
	print 'e ',event_number
	event_number += 1
	print r.choice(timbre)
	a = r.choice(notelist)
	b = r.choice(notelist)
	common_harmonics(a,b)
	length = r.randint(l,u)
	print 'l ',length
	print r.choice(orientation)
	piece_duration += length
	print 'piece duration ',piece_duration 
	print '\n'

#section 2 

print 'SECTION 2\n'

l = 6
u = 10

while piece_duration <= 450:
	print 'e ',event_number
	event_number += 1
	print r.choice(timbre)
	a = r.choice(notelist)
	b = r.choice(notelist)
	common_harmonics(a,b)
	length = r.randint(l,u)
	print 'l ',length,'to scale ',float(length)/2  #prints actual length, then scaled length
	print r.choice(orientation)
	piece_duration += length
	print 'piece duration ',piece_duration 
	print '\n'

#section 3

print 'SECTION 3\n'

l = 4
u = 10

while piece_duration <= 675:
	print 'e ',event_number
	event_number += 1
	print r.choice(timbre)
	a = r.choice(notelist)
	b = r.choice(notelist)
	common_harmonics(a,b)
	length = r.randint(l,u)
	print 'l ',length,'to scale ',float(length)/4 #prints actual length, then scaled length
	print r.choice(orientation)
	piece_duration += length
	print 'piece duration ',piece_duration 
	print '\n'

#section 4 

print 'SECTION 4\n'

l = 2
u = 10

while piece_duration <= 900:
	print 'e ',event_number
	event_number += 1
	print r.choice(timbre)
	a = r.choice(notelist)
	b = r.choice(notelist)
	common_harmonics(a,b)
	length = r.randint(l,u)
	print 'l ',length,'to scale ',float(length)/8 #prints actual length, then scaled length
	print r.choice(orientation)
	piece_duration += length
	print 'piece duration ',piece_duration 
	print '\n'

print '\nEND'