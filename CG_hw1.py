#!/usr/bin/python
# /*  Name:    Merlin Cherian
#  *  Class:   CS 536 (Computer Graphics)
#  *
#  *  Evaluates a 3D arbitrary-degree Bezier curve and approximates it with a polyline
#  *
#  */

import numpy as np
import argparse

xVals, yVals, zVals = [], [], []
pX, pY, pZ = [], [], []
x, y, z = [], [], []
tmpX = []
tmpY = []
tmpZ = []
testX = []
testY = []
testZ = []


# reads xyz coordinates into array
def readfile(fname):
        with open(fname) as fobj:
            for line in fobj:
                row = line.split()
                x.append(row[0])
                y.append(row[1])
                z.append(row[-1])

        global xVals, yVals, zVals
        xVals = list(map(float, x))
        yVals = list(map(float, y))
        zVals = list(map(float, z))


# generates the array of t values
def gentvals(t):
    tVals = np.arange(0.0, 1.01, t)
    return tVals


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def fact(k, i):
    return factorial(k)/(factorial(i)*factorial(k-i))


# evaluates the curve
def bezier(xVals, yVals, zVals, tVals, n):
    for t in tVals:
        for i in range(0, n+1):
            cx = float(xVals[i]) * fact(n, i) * pow((1 - t), (n - i)) * pow(t, i)
            cy = float(yVals[i]) * fact(n, i) * pow((1 - t), (n - i)) * pow(t, i)
            cz = float(zVals[i]) * fact(n, i) * pow((1 - t), (n - i)) * pow(t, i)
            tmpX.append(cx)
            tmpY.append(cy)
            tmpZ.append(cz)
        testX.append(sum(tmpX))
        testY.append(sum(tmpY))
        testZ.append(sum(tmpZ))
        del tmpX[:]
        del tmpY[:]
        del tmpZ[:]


# prints the Open Inventor Format to stdout
def print_stdout(radius):
    print ("#Inventor V2.0 ascii"
             "\n"
             "\n"
             "Separator {LightModel {model BASE_COLOR} Material {diffuseColor 1.0 1.0 1.0}"
             "\n"
             "Coordinate3 { 	point [ "
             "\n")
    finalX = [round(elem, 6) for elem in testX]
    finalY = [round(elem, 6) for elem in testY]
    finalZ = [round(elem, 6) for elem in testZ]
    for i in range(0, len(finalX)):
        line = finalX[i], finalY[i], finalZ[i]
        a = str(line).strip("()")
        a = a.replace(',', '')
        print a
        print (",\n")
    print ("] } \nIndexedLineSet {coordIndex [\n")
    for i in range(0, len(finalX)):
        num = str(i)
        num += ", "
        print (num)
    print ('-1')
    print (
        "\n] } }\nSeparator {LightModel {model PHONG}Material {	diffuseColor 1.0 1.0 1.0}\nTransform {translation\n")
    for i in range(0, len(xVals)):
        line = xVals[i], yVals[i], zVals[i]
        a = str(line).strip("()")
        a = a.replace(',', '')
        a.replace('\'', '')
        print (a)
        if i != len(xVals) - 1:
            print ("\n"
                     "}Sphere {	radius " + radius + " }}\nSeparator {LightModel {model PHONG}Material {	diffuseColor 1.0 1.0 1.0}\nTransform {translation\n")
        else:
            print ("\n"
                     "}Sphere {	radius " + radius + " }}")


# redirect output to file in directory
def print_file(radius):
    f1 = open('./out.iv', 'w+')
    f1.write("#Inventor V2.0 ascii"
             "\n"
             "\n"
             "Separator {LightModel {model BASE_COLOR} Material {diffuseColor 1.0 1.0 1.0}"
             "\n"
             "Coordinate3 { 	point [ "
             "\n")
    finalX = [round(elem, 6) for elem in testX]
    finalY = [round(elem, 6) for elem in testY]
    finalZ = [round(elem, 6) for elem in testZ]
    for i in range(0, len(finalX)):
        line = finalX[i], finalY[i], finalZ[i]
        a = str(line).strip("()")
        a = a.replace(',', '')
        f1.write(a)
        f1.write(",\n")
    f1.write("] } \nIndexedLineSet {coordIndex [\n")
    for i in range(0, len(finalX)):
        num = str(i)
        num += ", "
        f1.write(num)
    f1.write('-1')
    f1.write("\n] } }\nSeparator {LightModel {model PHONG}Material {	diffuseColor 1.0 1.0 1.0}\nTransform {translation\n")
    for i in range(0, len(xVals)):
        line = xVals[i], yVals[i], zVals[i]
        a = str(line).strip("()")
        a = a.replace(',', '')
        a.replace('\'', '')
        f1.write(a)
        if i!=len(xVals)-1:
            f1.write("\n"
                     "}Sphere {	radius " + radius + " }}\nSeparator {LightModel {model PHONG}Material {	diffuseColor 1.0 1.0 1.0}\nTransform {translation\n")
        else:
            f1.write("\n"
                     "}Sphere {	radius " + radius + " }}")

    f1.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--u', help='Description for argument foo argument', required=False)
    parser.add_argument('-r', '--r', help='Description for r argument', required=False)
    parser.add_argument('-f', '--f', help='Description for r argument', required=False)
    args = vars(parser.parse_args())
    if args['f']:
        readfile(args['f'])
    else:
        readfile('sampleInput.txt')
    numPoints = len(xVals)-1
    if args['u']:
        t = float(args['u'])
    else:
        t = 0.05
    if args['r']:
        r = args['r']
    else:
        r = str(0.1)
    tVals = gentvals(t)
    tVals = [ round(elem, 6) for elem in tVals ]
    bezier(xVals, yVals, zVals, tVals, numPoints)
    print_stdout(r)
    #print_file(r)


if __name__ == '__main__':
    main()
