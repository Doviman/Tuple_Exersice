
textbooks = [("textbook ID", "Textbook Name", "Course", " # of Books", "Price per Book", "Publisher ID"),
             ("TEXT-0001", "Basic Anatomy and Physiology", "BIO-100", 400, 94.00, "PUB-1003"),
             ("TEXT-0002", "Chemestry for Biology Students", "BIO-101-102", 400, 105.30, "PUB-1002"),
             ("TEXT-0003", "Anatomy and Physiology", "BIO-141-142", 330, 159.75, "PUB-1003")]
d = 0
tbks = []
while d < len(textbooks):
    tbks.append(textbooks[d][1])
    tbks.append(textbooks[d][4])
    d += 1
    print tbks
    tbks = []

print textbooks[1][1], textbooks[1][4]
print textbooks[2][1], textbooks [2][4]
print textbooks[2][1], textbooks[2][4]
print textbooks[3][1], textbooks[3][4]


publisher = [("Publisher ID", "Publisher Name", "Address", "City", "State", "Zip", "Phone Number"),
             ("PUB-1001", "Science Books Galore", "525 Allen St", "Trenton", "NJ", "08620", "609-555-2554"),
             ("PUB-1002", "Books for Chemestry Students Ltd", "142 N Spring St", "Los Angel", "CA", "90012", "213-555-8382"),
             ("PUB-1003", "Carliz Publishers Corp", "24 King Ave", "Columbus", "OH", "43201", "614-555-3322")]


e = 0
pblshr = []
while e < len(publisher):
    pblshr.append(publisher[e][1])
    pblshr.append(publisher[e][6])
    e += 1
    print pblshr
    pblshr = []

print publisher[1][1], publisher[1][6]
print publisher[2][1], publisher[2][6]
print publisher[3][1], publisher[3][6]
