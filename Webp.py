import os
from PIL import Image
import streamlit as st

# عنوان اپلیکیشن
st.title("Image Converter to WebP")

# آپلود تصاویر
uploaded_files = st.file_uploader("Choose images", accept_multiple_files=True, type=['jpg', 'jpeg', 'png'])

# دایرکتوری پیش‌فرض برای ذخیره تصاویر
output_directory = "converted_images"

# دکمه شروع تبدیل
if st.button("Convert to WebP"):
    if not uploaded_files:
        st.warning("Please upload at least one image.")
    else:
        # ایجاد دایرکتوری خروجی در صورت عدم وجود
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # پردازش و تبدیل تصاویر به WebP
        for uploaded_file in uploaded_files:
            try:
                # باز کردن تصویر
                image = Image.open(uploaded_file)
                
                # نام فایل ورودی و محاسبه حجم اولیه
                input_size = uploaded_file.size / 1024  # تبدیل به KB
                
                # نام فایل خروجی
                output_path = os.path.join(output_directory, f"{os.path.splitext(uploaded_file.name)[0]}.webp")
                
                # ذخیره به فرمت WebP
                image.save(output_path, "webp")
                
                # محاسبه حجم فایل WebP
                output_size = os.path.getsize(output_path) / 1024  # تبدیل به KB

                # نمایش حجم قبل و بعد
                st.write(f"Image {uploaded_file.name}:")
                st.write(f"Original Size: {input_size:.2f} KB")
                st.write(f"Converted Size: {output_size:.2f} KB")
                
                # ارائه فایل برای دانلود
                with open(output_path, "rb") as file:
                    btn = st.download_button(
                        label=f"Download {os.path.splitext(uploaded_file.name)[0]}.webp",
                        data=file,
                        file_name=f"{os.path.splitext(uploaded_file.name)[0]}.webp",
                        mime="image/webp"
                    )

                st.success(f"Image {uploaded_file.name} converted and saved to {output_path}")

            except Exception as e:
                st.error(f"Error converting {uploaded_file.name}: {str(e)}")
