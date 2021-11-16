# Steganography!!!
# Pillow
from PIL import Image

# 08bit binary numbers

def genData(data):
    newd = []
    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd



# Encode or Decode
def encode():
    img = input("Enter the image name(with extension)")
    image = Image.open(img,'r')
    newImage = image.copy()
    newImage.save('test.jpg')


def decode():
    img = input('Enter the name of the image(with extension)')
    image = Image.open(img,'r')
    imgData = image
    return imgData

# 'Sid'
# 100px
# 0px S, 20px i, 40px d


def imgPix(pix,data):
    dataList = genData(data) # All the data

    for i in range(dataList):
        pix = [value for value in dataList.__next__()[:3] + dataList.__next__()[:3]]

    


def main():
    a = int(input("Welcome to Steganography:\n 1.Encode \n 2.Decode"))
    if (a==1):
        encode()
    elif (a==2):
        decode()

    else:
        print("Enter correct input")

# if __name__ == '__main__':
#     main()
