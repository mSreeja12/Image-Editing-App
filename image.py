import streamlit as sl
from PIL import Image
from PIL.ImageFilter import *

sl.markdown("<h1 style='text-align:center;'>Image Editor</h1>",unsafe_allow_html=True)
sl.markdown("---")
image=sl.file_uploader("Upload a Image",type=["jpeg","jpg","png"])

if image is not None:
    try:
        # Open the uploaded file as an image
        img = Image.open(image)
        sl.image(img, caption="Uploaded Image", use_column_width=True)

        # Display image details
        size = sl.empty()
        mode = sl.empty()
        img_format = sl.empty()

        size.markdown(f"Size: {img.size}")
        mode.markdown(f"Mode: {img.mode}")
        img_format.markdown(f"Format: {img.format}")

    except Exception as e:
        sl.error(f"Error loading image: {e}")

else:
    sl.warning("Please upload an image file.")

size=sl.empty()
mode_=sl.empty()
format_=sl.empty()
if image:
   img=Image.open(image)
   size.markdown(f"Size: {img.size}")
   mode_.markdown(f"Mode: {img.mode}")
   format_.markdown(f"Format: {img.format}")
   sl.markdown("---")
   sl.header("Resizing")
   width=sl.number_input("Width",value=img.width)
   height=sl.number_input("Height",value=img.height)
   sl.markdown("---")
   sl.header("Rotation")
   degree=sl.number_input("Degree")
   sl.markdown("---")
   sl.header("Filters")
   filters=sl.selectbox("Filters",options=("blur","contour","detail","emboss","sharpen","smooth","edge enhance","none"))
   btn=sl.button("Submit")
   if btn:
      edited=img.resize((width,height)).rotate(degree)
      
      filtered= edited
      if filters != "none":
        if filters =="blur":
           filtered= edited.filter(BLUR)
        elif filters =="contour":
            filtered=edited.filter(CONTOUR)
        elif filters =="detail":
            filtered=edited.filter(DETAIL)
        elif filters =="emboss":
            filtered=edited.filter(EMBOSS)
        elif filters =="sharpen":
            filtered=edited.filter(SHARPEN)
        elif filters =="smooth":
            filtered=edited.filter(SMOOTH)
        else:
            filtered=edited.filter(EDGE_ENHANCE)
     
      sl.image(filtered)