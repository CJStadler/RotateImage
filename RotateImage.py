"""
Chris Stadler
RotateImage.py

Rotates a square image 90 degrees.
"""
import Image

def main(fileName):
    im = Image.open(fileName)
    w, h = im.size
    assert w == h # must be square.
    data = list(im.getdata())
    #print len(data)
    rotate90(data, w)
    im.putdata(data)
    im.save(fileName)

def rotate90(data, w):
    row = 0
    col = 0
    for ring in range(w/2):
        corner = ring*w + ring
        rw = w - ring*2
        for quad in range(w - 1 - ring*2):
            q1 = corner + quad
            q2 = corner + quad*w + rw -1
            q3 = corner + (rw-1)*w + rw - quad -1
            q4 = corner + (rw-quad-1)*w
            temp = data[q1]
            data[q1] = data[q4]
            data[q4] = data[q3]
            data[q3] = data[q2]
            data[q2] = temp

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Zip and unzip using Huffman coding")
    parser.add_argument('fileName', help='Image to rotate')
    #parser.add_argument('outImage', help='Save as')
    #parser.add_argument('degrees', type=int, help='degrees to rotate, multiple of 90')
    args = parser.parse_args()
    main(args.fileName)
