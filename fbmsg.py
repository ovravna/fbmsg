# !/usr/bin/env python
# -*- coding: utf-8 -*-
import re

count_map = {}

for index in range(679):

	with open('D:/Downloads/facebook-ravnaaa/messages/{}.html'.format(index), 'r', encoding="utf8") as file:
		html = file.read()

	srch = re.search('Participants: ([^,><]+?)(?=[<\n])', html)

	if srch:

		count_map[srch.group(1)] = len(re.findall('class="message"', html))

print('length of count_map:',len(count_map), end='\n\n')

mx = sorted(count_map, key=lambda k: count_map[k], reverse=True)

for k in mx:
	if count_map[k] < 100:
		break
	print(k, count_map[k])
