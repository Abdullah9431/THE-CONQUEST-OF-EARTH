# -*- coding: utf-8 -*-
'''
The Caponians, an alien strain coming from an unspecified planet in
the galaxy, have been planning for quite a while the invasion of the
planet Earth. To do this, they have created and installed in various
points of the planet "mind bending machines". This machinery reduces
the intelligence of humans through the telephone network [1].

Once the phase of reducing human intelligence is over, the next
step towards the conquest of the Earth will be the landing on our
planet, which will happen as soon as the Caponians will find some
areas where they can land with their spaceships.

A spaceship (seen from above) can be represented as a rectangle of
dimensions W (width) and H (height). When considering the necessary
space for landing, a spaceship will open hatches on the 4 sides of
the rectangle. These gates are one per side.

The areas protrude by the same amount D, in order to allow to open on
each side a landing hatch. Each hatch is therefore as wide as the side
of the spaceship on which it is located and long as D, whatever side
it is on.

The Caponians would like to land with their spaceships in some of our
cities by looking at the city map. A city can be represented as a black
rectangular image, in which every building is represented as a colored
rectangle (each building has a color that uniquely identifies it).

In order to define the final details of the landing plan, the Caponians
need an algorithm which, given a map of a city and a
list of spaceships, confirms or not if
each spaceship has enough space to land in that city.
To land, a spaceship has to open its 4 hatches. Spaceships do not land
in the city at the same time, so they must be evaluated separately
from each other.

(1) So, given a black image (city) filled with solid colored
rectangles (buildings), where each building has its own unique color,
it is necessary:

- determine position, size and color of each rectangle
- save in a text file one rectangle per line
- in the file, each rectangle is represented with a sequence of 7 values:
     x, y, w, h, r, g, b
  separated by commas, in order of decreasing y-coordinate (the row
  nunber). In case of equal y, in order of increasing x (row-pixel number).

(2) Next, we are given a text file containing N triple of
integers. Each triple is separated internally and from the other
triples by a variable number of spaces, tabs or carriage returns. Each
triple represents width W, height H and minimum distance D (see below)
of a spaceship that you would like to land in a city at step (1):

- So we have to return a list of N Boolean values: the i-th value in
the list is True if there is enough space in the image to
insert the i-th spaceship.

- a rectangle can be inserted in the image if there exists at least
one position in the image where there is enough space (i.e., an area
consisting entirely of black pixels) to hold the i-th spaceship.
A spaceship can land if contains the rectangle itself, plus the 4
"extensions" of the rectangle, i.e. the 4 hatches of the spaceship.

For example, if a spaceship has 2 pixels of width and 3 of height and
D = 2, we will have to look for an area in the image to contain the
following figure:

                              **
                              **
                            **++**
                            **++**
                            **++**
                              **
                              **

where the + symbols are the pixels of the 2x3 rectangle/spaceship and the *
are the pixels of the 4 extensions/hatches.

Example:
Given the following image represented with one character for each
pixel, where "." is a black pixel and characters other than "." are
colored pixels (*=red, +=green):

**....
**....
......
......
....++
....++

The file with the found rectangles  must contain the lines:
4,4,2,2,0,255,0
0,0,2,2,255,0,0

and given the following spaceships:

(3, 3, 0)
(2, 2, 4)
(1, 1, 3)
(4, 2, 1)
(2, 4, 1)

the returned list will be: [True, False, False, False, False].
In fact only the first spaceship can land for example in the zone marked by
'X' (it has no doors, in fact D = 0)

**.XXX
**.XXX
...XXX
......
....++
....++

while the others don't enter in the map because, even if they have a point
in which they can land, they cannot open all the hatches.


[1] https://en.wikipedia.org/wiki/Zak_McKracken_and_the_Alien_Mindbenders)
'''

from pngmatrix import load_png8
'from line 122 to 175 perfectly working (tested)'
def ex(file_png, file_txt, file_out):
    image = load_png8(file_png)
    #print(image)#[[(255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 255, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 255, 0)]]#load_png8(file_png)
    x =-1
    y =-1
    rectlist = []
    final = []
    for y,row in enumerate(image):
        for x,pixel in enumerate(row):
            if pixel != (0 ,0 ,0):
                if pixel not in rectlist:
                    rectlist.append(pixel)
                    final.append([x,y,1,1,pixel[0],pixel[1],pixel[2]])
                if pixel in rectlist:
                    for i in range(len(final)):
                        if list(final[i][4:]) == list(pixel):
                            final[i][2]= x - final[i][0] +1
                            final[i][3]= y - final[i][1] +1
    def sorter(c):
        return (c[1],-c[0])
    final = sorted(final,key = sorter,reverse = True)
    with open(file_out,'w') as f:
        for d in final:
            d=str(d)
            d = d.replace('[','')
            d = d.replace(']','')
            d = d.replace(' ','')
            f.writelines(d+'\n')
    with open(file_txt) as f:
        num = f.read()
        num = num.split()
    result = []
    for a, b, c in zip(num[::3],num[1::3],num[2::3]):
        '''a=width,b=height,c=length of hatch'''
        a = int(a)
        b= int(b)
        c=int(c)
        ck1 = b + c*2
        flag = True
        def checker1(ck1,p,q):
            '''checker1 is supposed to check the portion indicated by third bracket
                         [**]
                         [**]
                       **[++]**
                       **[++]**
                       **[++]**
                         [**]
                         [**]
                
        '+' is the body of spaceship and '*' is its hatch'''
            
            try:
                for x in range(p,p+a):
                    for y in range(q,q+ck1):
                        if image[y][x] != (0,0,0):
                            return None
                return True
            except:
                return None
        def checker2(p,q,b,c):
            '''checker2 is supposed to check the portion indicated by third bracket
                           **
                           **
                       [**]++**
                       [**]++**
                       [**]++**
                          **
                          **'''
            mx1 = p-c
            my1 = q+c 
            if mx1 <0 or my1<0:
                return None
            for mx in range(mx1,mx1+c):
                for my in range(my1,my1+b):
                    if image[my][mx] != (0,0,0):
                        return None
            return True
        def checker3(p,q,b,c):
            '''checker1 is supposed to check the portion indicated by third bracket
                       **
                       **
                     **++[**]
                     **++[**]
                     **++[**]
                       **
                       **'''
            mx2 = p+a
            my2 = q+b
            try:
                for mox in range(mx2,mx2+c):
                    for moy in range(my2,my2+b):
                        if image[moy][mox] != (0,0,0):
                            return None
                return True
            except:
                return None
        def main(ck1,b,c):
            if checker1(ck1,p,q):
                if c == 0:
                    return True
                if checker2(p,q,b,c):
                    if checker3(p,q,b,c):
                        return True
        for p in range(len(image[0])):
           for q in range(len(image)):
               if main(ck1,b,c) is True:
                   flag = False
                   break
           if not flag:
               break
        if flag:
            result.append(False)
        else:
            result.append(True)
    return result
    
    
    
    
    
    
    
    
#     def checker1(ck1,p,q):
#         try:
#             for x in range(p,p+a):
#                 for y in range(q,q+ck1):
#                     if image[y][x] != (0,0,0):
#                         return False
#             return True
#         except:
#             return False
#     def checker2(p,q,b,c):
#         mx1 = p-c
#         my1 = q+c 
#         if mx1 <0 or my1<0:
#             return False
#         for mx in range(mx1,mx1+c):
#             for my in range(my1,my1+b):
#                 if image[my][mx] != (0,0,0):
#                     print(mx,my)
#                     return False
#         return True
#         if c ==0:
#             print(p,q)
#             #result.append(True)
#             return True
#     def checker3(p,q,b,c):
#         mx2 = p+a
#         my2 = q+b
#         try:
#             for mox in range(mx2,mx2+c):
#                 for moy in range(my2,my2+b):
#                     if image[moy][mox] != (0,0,0):
#                         print(mox,moy,mx2,my2)
#                         return False
#             return True
#         except:
#             return False
#     def main(ck1,b,c):
#         if checker1(ck1,p,q):
#             print(1)
#             if c == 0:
#                 return True
#             if checker2(p,q,b,c):
#                 if checker3(p,q,b,c):
#                     result.append(True)
#                 else:
#                     result.append(False)
#             else:
#                 result.append(False)
#         else:
#             result.append(False)
#     for p in range(len(image[0])):
#        for q in range(len(image)):
#            result.append(main(ck1,b,c))
#     return result
    
#         #check for heights with hatches if they fit in image 
#         #then check for width without hatches
#         #then in the line of width check if hatches can be placed
# ex('images/example.png','/home/araz/Desktop/HW6rec/HW6-rec/rectangles/example.txt','test_out')                
                       
                 
    

# # if __name__ == "__main__":
# #     pass
