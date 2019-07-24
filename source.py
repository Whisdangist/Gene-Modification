#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import re
import os

for file in os.listdir("input"):
    sentences = []
    with open("input/%s" % file) as doc:
        for line in doc.readlines():
            sentences.extend(re.split(r'\.(\s|$)', line.strip()))
            # sentences.extend(line.strip().split('.'))

    # patten = re.compile(r'Embryo|Clon(e|ing)', re.I)
    patten = re.compile(r'gen(etic|om(e|ic)|e[^a-z]*).*[^a-z](edit|modif)', re.I)
    with open("output/%s" % file, "w") as doc:
        for sentence in sentences:
            if patten.search(sentence):
                doc.write(sentence)
                doc.write('\n')
                print sentence.strip()

