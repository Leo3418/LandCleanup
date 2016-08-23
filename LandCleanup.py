#   Copyright (C) 2016 Leo3418 (https://github.com/Leo3418)

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see (http://www.gnu.org/licenses/). 

print 'Copyright (C) 2016 Leo3418'
print 'This is free software licensed under GNU GPLv3 with the absence of any warranty'
print ''

fhand = open('cleanup.txt')
fout = open('hasland.txt', 'w')
names = []
for line in fhand:
    name = line[2:-5]
    if not name in names:
        names.append(str(name))
fhand.close()
fhand = open('Land.yml')
for line in fhand:
    if 'owner:' in line:
        line = line.lower()
        line = line[9:-1]
        for name in names:
            if name == line or name == line[1:-1]:
                fout.write(name)
                fout.write('\n')
                names.remove(name)        
fout.close()
fhand.close()
print 'Done! Please check out "hasland.txt".'
