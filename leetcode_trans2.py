#!/usr/bin/env python2

input_text = raw_input("Enter some text: ")

leetreplace = {
	"a": "4",
	"b": "8",
	"e": "3",
	"l": "1",
	"o": "0",
	"s": "5",
	"t": "7"
}

def leettrans(a, b):
	for x,y in b.iteritems():
		a = a.replace(x,y)
	return a

print leettrans(input_text,leetreplace)
