"""
Chris Stadler
RotateImage.py
"""
import Image

def main(fileName, outfile, degrees):
    assert degrees%90 == 0 # can only rotate a multiple of 90.
    im = Image.open(fileName)
    w, h = im.size
    assert w == h # must be square.
    data = im.getdata()
    rotateData(data, degrees)
    im.putdata(data)
    im.save(outfile)

def rotateData(data, degrees):
    return True

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Zip and unzip using Huffman coding")
    parser.add_argument('inImage', help='Image to rotate')
    parser.add_argument('outImage', help='Save as')
    parser.add_argument('degrees', type=int, help='degrees to rotate, multiple of 90')
    args = parser.parse_args()
    main(args.inImage,args.outImage,args.degrees)
