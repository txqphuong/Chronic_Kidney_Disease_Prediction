import streamlit as st
import os
from pathlib import Path
import subprocess

def main():
    page_bg_img = """
        <style>
        [data-testid="stAppViewContainer"]{
            background-image: url(https://ts.hufi.edu.vn/tttstt/images/tt-tstt/5155dac03c64c13a9875_1.jpg);
            background-size: cover;
            margin-top: 20px;  /* Adjust the margin-top value as needed */
            padding-top: 0px;   /* Adjust the padding-top value as needed */
        }
        .stApp * {
            color: blue !important;
        }
        [data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}
        </style>
                  """

    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Tạo layout cho cột trái và cột phải
    col1, col2 = st.columns(2)

    # Cột trái
    with col1:
        st.title("CKD bằng Logistic Regression")
        if st.button("Mở ứng dụng"):
            script_path = Path("E:/Nam 3/TH ML/Nhom02_ChuanDoanBenhThanManTinh/Nhom02/HocMayTH/DOANCUOIKI/giaodien/thongtinbenhnhanlr.py")
            subprocess.run(["streamlit", "run", str(script_path)])

    # Cột phải
    with col2:
        st.title("CKD bằng Bernoulli Naive Bayes")
        if st.button("Mở ứng dụng 2"):
            script_path = Path("E:/Nam 3/TH ML/Nhom02_ChuanDoanBenhThanManTinh/Nhom02/HocMayTH/DOANCUOIKI/giaodien/thongtinbenhnhanbnb.py")
            subprocess.run(["streamlit", "run", str(script_path)])
if __name__ == "__main__":
    main()
