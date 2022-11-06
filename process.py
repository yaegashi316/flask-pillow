from PIL import Image

img = Image.open("images/cat.png")
frame = Image.open("images/frame.png")

resized_frame = frame.resize((img.width, img.height))
# resizeする
img.paste(resized_frame, (0, 0), resized_frame)
    # resizeした画像を重ねる

img.save("images/out.png")
img.show()
