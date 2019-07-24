#!/usr/bin/env python3
import re

# Creating the list of files to read
tex_files = [
        'doc.tex',
        'intro.tex',
        'texput.log',
        'usr_01.tex',
        'usr_02.tex',
        'usr_03.tex',
        'usr_04.tex',
        'usr_05.tex',
        'usr_06.tex',
        'usr_07.tex',
        'usr_08.tex',
        'usr_09.tex',
        'usr_10.tex',
        'usr_11.tex',
        'usr_12.tex',
        'usr_20.tex',
        'usr_21.tex',
        'usr_22.tex',
        'usr_23.tex',
        'usr_24.tex',
        'usr_25.tex',
        'usr_26.tex',
        'usr_27.tex',
        'usr_28.tex',
        'usr_29.tex',
        'usr_30.tex',
        'usr_31.tex',
        'usr_32.tex',
        'usr_40.tex',
        'usr_41.tex',
        'usr_42.tex',
        'usr_43.tex',
        'usr_44.tex',
        'usr_45.tex',
        'usr_90.tex'
        ]

# Regex creation
# The notation used in these manuals is explained here: \hyperref[notation]{|\texttt{notation}|}.
# Group 1 = Before label
# Group 2 = Name of the label
# Group 3 = Text for the label
# Group = Post label
regex = re.compile(r"^(.*)\\hyperref\[(\S*)\]\{(.*)\}(.*)$")

# Main loop
for filename in tex_files:
    file_read = open(filename, 'r')
    file_write = open("manual_pagenumber/"+filename, 'w')
    for line in file_read:
        result = regex.search(line)
        if result != None:
            new_line = result.group(1)
            new_line += result.group(3)
            new_line += " on page \\pageref{"
            new_line += result.group(2)
            new_line += "}"
            new_line += result.group(4)
            file_write.write(new_line)
            file_write.write("\n")

            # print("Previous line:")
            # print(line)
            # print("New line:")
            # print(new_line)
        else:
            file_write.write(line)
            pass
    file_read.close()
    file_write.close()
