print("            Wlecome to fun with QR code                ")
print("Enter your choice")
print("1.Creating a QR code")
print("2.Reading a QR code from system")
print("3.Reading QR code from camera")
x=int(input())
if x==1:
    import qrcode
    from PIL import Image
    from qrcode.image.pil import PilImage
    print("enter the text to be incoded")
    k=input()
    img=qrcode.make(k)
    img.save("q.jpg")
    p=Image.open("q.jpg")

    p.show()
    
elif x==2:
    import cv2
    from pyzbar.pyzbar import decode
    print("enter the name of the image with format")
    img=input()
    img1=cv2.imread(img)
    for code in decode(img1):
       print(code.data.decode('utf-8'))
    
elif x==3:
    import cv2
    from pyzbar.pyzbar import decode
    print("INformation in QR code is")
    cap=cv2.VideoCapture(0)
    i=0
    while i<1:
       _,frame=cap.read()
       for code in decode(frame):
          print(code.data.decode('utf-8'))
          i=i+1
       cv2.imshow("Screen",frame)
       cv2.waitKey(5)
    cv2.destroyAllWindows()