#iJ

def line():
    print("_______________________________________________________________________________\n")
        

line()
paternal = input("[3] " + "Paternal ♂ genotype" + " (default 'Aa') = ").strip()
maternal = input("[4] " + "Maternal ♀ genotype" + " (default 'Aa') = ").strip()
line()
frame = input("[5] " + "Frame type" + " (1-4, default '1'): ").strip()
line()


#Genotypes
if paternal == "":
    paternal = "Aa"
if maternal == "":
    maternal = "Aa"

#Frame
if frame == "":
    frame = "1"



p1, p2 = paternal[:len(paternal)//2], paternal[len(paternal)//2:]
m1, m2 = maternal[:len(maternal)//2], maternal[len(maternal)//2:]




m3, m4 = m1, m1
m5, m6 = m2, m2
p3, p4 = p1, p1
p5, p6 = p2, p2





if m1.isupper() == False:
    if p1.isupper() == True:
        m3, p3 = p3, m3
    if p2.isupper() == True:
        m4, p5 = p5, m4
if m2.isupper() == False:
    if p1.isupper() == True:
        m5, p4 = p4, m5
    if p2.isupper() == True:
        m6, p6 = p6, m6        





f1 = m3 + p3
f2 = m4 + p5
f3 = m5 + p4
f4 = m6 + p6





if frame == "1":
    print("""
 _____ _____ _____
|     |     |     |
| ♀/♂ |  """ + p1 + """  |  """ + p2 + """  |
|_____|_____|_____|
|     |     |     |
|  """ + m1 + """  |  """ + f1 + """ |  """ + f2 + """ |
|_____|_____|_____|
|     |     |     |
|  """ + m2 + """  |  """ + f3 + """ |  """ + f4 + """ |
|_____|_____|_____|
""")
if frame == "2":
    print("""

      |     |     
  ♀/♂ |  """ + p1 + """  |  """ + p2 + """
 _____|_____|_____
      |     |     
   """ + m1 + """  |  """ + f1 + """ |  """ + f2 + """
 _____|_____|_____
      |     |
   """ + m2 + """  |  """ + f3 + """ |  """ + f4 + """
      |     |     
""")
if frame == "3":
    print("""

      |     |     |
  ♀/♂ |  """ + p1 + """  |  """ + p2 + """  |
 _____|_____|_____|
      |     |     |
   """ + m1 + """  |  """ + f1 + """ |  """ + f2 + """ |
 _____|_____|_____|
      |     |     |
   """ + m2 + """  |  """ + f3 + """ |  """ + f4 + """ |
 _____|_____|_____|
""")
if frame == "4":
    print("""
 _____ _____ _____
      |     |     |
  ♀/♂ |  """ + p1 + """  |  """ + p2 + """  |
 _____|_____|_____|
      |     |     |
   """ + m1 + """  |  """ + f1 + """ |  """ + f2 + """ |
 _____|_____|_____|
      |     |     |
   """ + m2 + """  |  """ + f3 + """ |  """ + f4 + """ |
 _____|_____|_____|
""")



input()