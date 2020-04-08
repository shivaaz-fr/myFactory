import re
series = 'Miss Fisher:Phrany Fisher;GOT:Daenerys Targaryen;X-Files:Dana Scully;Miss Ficher:Jack Robinson;Miss Fisher:Dorothy Williams;GOT:Jon Snow;GOT:Tyrion Lannister;X-Files:Fox Mulder'
pattern  = r':([A-Za-z ]+)[;|$]'
match = re.findall(r'GOT' + pattern, series)
print (match)
