import easyocr

reader = easyocr.Reader(["en", "ko"], gpu=False)
text = reader.readtext("./images/facebook_post.jpg")
print(text)
