import pytesseract
from PIL import Image
import numpy as np

filename = 'API/config/api/backend/originalImages/test.png'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)

print(text)