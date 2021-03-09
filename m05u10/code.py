with open('utskrift.txt', 'w') as fw:
#Öppnar utskrift text fil och sätter det som fw.

  fw.write('''1 2 3
4 5 6
7 8 9
''') 
#Skriver in de nummer och i de ordning in i dokumentet

  fw.write('\nHär var det rutigt!') 
  #Hopper ner ett steg och skirver in stringen

with open('utskrift.txt', 'r') as fr: 
#Öppnar txt filen utskrift som fr.

  print(fr.read())
  #Printar innehållet av txt filen utskrift