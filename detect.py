import easyocr

reader = easyocr.Reader(["en", "ko"], gpu=False)
text = reader.readtext("./images/YBIGTA.jpg")
print(text)
