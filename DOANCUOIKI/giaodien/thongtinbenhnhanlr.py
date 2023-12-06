import pyodbc
import streamlit as st
import sqlite3
import subprocess
import os

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-KNIJTEG\SQLEXPRESS;'
                      'Database=ChuanDoanCKD;'
                      'Trusted_Connection=yes;')

# Tạo đối tượng cursor để thao tác với CSDL
cursor = conn.cursor()

# Tiêu đề của trang
st.title("Quản lý bệnh nhân")
# Tạo form để thêm bệnh nhân mới
with st.form("Thêm bệnh nhân mới"):
    # Các trường thông tin của bệnh nhân
    with st.container():
        st.header("Thông tin bệnh nhân mới")
        idbn = st.text_input("Mã Bệnh nhân:")
        tenbn = st.text_input("Tên bệnh nhân:")
        diachi = st.text_input("Địa chỉ:")
        sdt = st.text_input("Số điện thoại:")
        gioitinh = st.radio("Giới tính:", ("Nam", "Nữ"))

    # Nút submit để thêm thông tin bệnh nhân vào CSDL
    submitted = st.form_submit_button("Thêm bệnh nhân")

    if submitted:
        try:
            # Thực hiện thêm thông tin bệnh nhân vào CSDL
            cursor.execute("INSERT INTO thongtinbenhnhan (id, tenbenhnhan, diachi, sdt, gioitinh) VALUES (?, ?,  ?, ?, ?)",
                        (idbn, tenbn, diachi, sdt, gioitinh))
            conn.commit()
            st.success("Thêm bệnh nhân mới thành công!")

            # Run the BNBok.py script using subprocess
            script_path = os.path.join("E:\\Nam 3\\TH ML\\Nhom02_ChuanDoanBenhThanManTinh\\Nhom02\\HocMayTH\\DOANCUOIKI\\giaodien", "LRok.py")
            subprocess.run(["streamlit", "run", script_path])

        except Exception as e:
            st.error("Thêm bệnh nhân mới thất bại! Vui lòng thử lại.")

# Your existing code...

if st.button('Chẩn Đoán Bệnh Với LR'):
    # Run the BNBok.py script using subprocess
    script_path = os.path.join("E:\\Nam 3\\TH ML\\Nhom02_ChuanDoanBenhThanManTinh\\Nhom02\\HocMayTH\\DOANCUOIKI\\giaodien", "LRok.py")
    subprocess.run(["streamlit", "run", script_path])