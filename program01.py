# -*- coding: utf-8 -*-
from pngmatrix import load_png8

def ex(file_png, file_txt, file_out):
    image = load_png8(file_png)
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
