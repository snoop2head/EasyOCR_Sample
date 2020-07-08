import easyocr

reader = easyocr.Reader(["en", "ko"], gpu=False)
text = reader.readtext("./images/R-540832-1331752044.jpeg.jpg")
print(text)
