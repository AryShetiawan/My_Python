#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jon
#
# Created:     09/02/2013
# Copyright:   (c) Jon 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

ini = '''
; set the colorscheme and userlevel
[colorscheme]
background=red
foreground=blue
title=green

[userlevel]
login=2
title=1
'''

def apply_value(name, config):
    print("""\nSetting: %s\nConfiguration: %s"""%(name,config))

#Chunking Python code to process .INI file

sects = ini.split('[',)
for sect in sects[1:]:
   # do something with sect, like get its name
   # (the stuff up to ']') and read its assignments
    name, assignments = sect.split(']')
    assignments = [assign for assign in assignments.split('\n') if assign != '']
    apply_value(name, assignments)

#Counting Python code to process .INI file

for line in ini:
    if line != '':
        if line[0] == '[':
            current_section = line[1:-2]
        elif line[0] in '"";\n' :
            continue     # ignore comments
        else:
            apply_value(current_section, line)