#!/usr/bin/python3
# vim:set ts=4

import os

if not os.path.exists('build'):
	os.mkdir('build')

with open('build/index.html', 'w') as fp:
	fp.write('<html>')
	fp.write('<head><title>A blank page</title></head>')
	fp.write('<body></body>')
	fp.write('</html>')
