import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO
import os

# ===========================
# Streamlit App Configuration
# ===========================
st.set_page_config(page_title="QR Code Generator", page_icon="🔳")

st.title("🔳 QR Code Generator")
st.write("Easily generate QR codes for any text or URL with customizable colors.")

# ===========================
# Create Output Folder (Desktop)
# ===========================
output_dir = os.path.join(os.path.expanduser("~"), "Desktop", "generated_qr")
os.makedirs(output_dir, exist_ok=True)

# ===========================
# User Inputs
# ===========================
user_data = st.text_input("Enter URL or Text to Generate QR Code:", "https://www.wscubetech.com/")
fill_color = st.color_picker("Pick QR Color","#000000")  # Default: Green
back_color = st.color_picker("Pick Background Color", "#FFFFFF")  # Default: White

# ===========================
# QR Code Generation
# ===========================
if st.button("Generate QR Code"):
    if user_data.strip() == "":
        st.error("Please enter some text or URL first.")
    else:
        # Create QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(user_data)
        qr.make(fit=True)
        img_qr = qr.make_image(fill_color=fill_color, back_color=back_color)

        # Convert qrcode image to standard Pillow Image
        img = img_qr.convert("RGB")

        # Save Image in Desktop Folder
        safe_name = user_data.replace("https://", "").replace("http://", "").replace("/", "_")[:20]
        file_path = os.path.join(output_dir, f"{safe_name}_qr.png")
        img.save(file_path)

        # Display in Streamlit
        st.image(img, caption="✅ Generated QR Code", use_container_width=True)

        # Download Button
        buf = BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()
        st.download_button(
            label="📥 Download QR Code",
            data=byte_im,
            file_name=f"{safe_name}_qr.png",
            mime="image/png"
        )



# ===========================
# Debug Info (Optional)
# ===========================

