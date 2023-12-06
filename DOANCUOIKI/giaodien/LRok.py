import os
import streamlit as st
import pandas as pd
import numpy as np
import pyodbc
import random
import string
import pickle
import matplotlib.pyplot as plt

# Kết nối tới CSDL SQL Server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-KNIJTEG\SQLEXPRESS;'
                      'Database=ChuanDoanCKD;'
                      'Trusted_Connection=yes;')

# Tạo đối tượng cursor để thao tác với CSDL
cursor = conn.cursor()
st.set_page_config(page_title="Kidney Disease Prediction", page_icon=":hospital:", layout="wide")
# Load the model
model = pickle.load(open('E:\\Nam 3\\TH ML\\Nhom02_ChuanDoanBenhThanManTinh\\Nhom02\\HocMayTH\\LR1.h5', 'rb'))
st.title(" LR ")
# Function to preprocess the input data
def preprocess_data(age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane):
    input_data = {
        'age': age,
        'blood_pressure': {'normal': 0, 'above normal': 1, 'well above normal': 2}[bp],
        'specific_gravity': {'normal': 0, 'abnormal': 1}[sg],
        'albumin': {'normal': 0, 'abnormal': 1}[al],
        'sugar': {'normal': 0, 'abnormal': 1}[su],
        'red_blood_cells': {'normal': 1, 'abnormal': 0}[rbc],
        'pus_cell': {'normal': 1, 'abnormal': 0}[pc],
        'pus_cell_clumps': {'present': 1, 'not present': 0}[pcc],
        'bacteria': {'present': 1, 'not present': 0}[ba],
        'blood_glucose_random': bgr,
        'blood_urea': bu,
        'serum_creatinine': sc,
        'sodium': sod,
        'potassium': pot,
        'hemoglobin': hemo,
        'packed_cell_volume': pcv,
        'white_blood_cell_count': wc,
        'red_blood_cell_count': rc,
        'hypertension': {'yes': 1, 'no': 0}[htn],
        'diabetes_mellitus': {'yes': 1, 'no': 0, 'unknown': 0}[dm],
        'coronary_artery_disease': {'yes': 1, 'no': 0}[cad],
        'appetite': {'good': 1, 'poor': 0}[appet],
        'pedal_edema': {'yes': 1, 'no': 0}[pe],
        'anemia': {'yes': 1, 'no': 0}[ane]
    }

    new_data = np.array([[input_data['age'], input_data['blood_pressure'], input_data['specific_gravity'],
                         input_data['albumin'], input_data['sugar'], input_data['red_blood_cells'],
                         input_data['pus_cell'], input_data['pus_cell_clumps'], input_data['bacteria'],
                         input_data['blood_glucose_random'], input_data['blood_urea'], input_data['serum_creatinine'],
                         input_data['sodium'], input_data['potassium'], input_data['hemoglobin'],
                         input_data['packed_cell_volume'], input_data['white_blood_cell_count'],
                         input_data['red_blood_cell_count'], input_data['hypertension'], input_data['diabetes_mellitus'],
                         input_data['coronary_artery_disease'], input_data['appetite'], input_data['pedal_edema'],
                         input_data['anemia']]])

    return new_data.astype(np.float64)
def main():
   
    st.sidebar.title("Lựa chọn")

    # Sidebar navigation
    navigation = st.sidebar.selectbox("Go to", ["New Patient", "Medical History"])

    if navigation == "New Patient":
        st.title("Chẩn đoán bằng LogisticRegression")
        # Add input fields
        trieuchung = st.text_input("Nhập mã triệu chứng")
        id_benh_nhan = st.text_input("Vui lòng nhập lại ID bệnh nhân")
        age = st.slider("Nhập tuổi của bệnh nhân", 1, 100, 25, 1)
        bp = st.selectbox("Chọn huyết áp của bạn", ["normal", "above normal", "well above normal"])
        sg = "abnormal"
        al = st.selectbox("Chọn albumin của bạn", ["normal", "abnormal"])
        su = st.selectbox("Chọn đường huyết của bạn", ["normal", "abnormal"])
        rbc = st.selectbox("Chọn số lượng tế bào máu đỏ của bạn", ["normal", "abnormal"])
        pc = st.selectbox("Chọn số lượng tế bào ủ bằng của bạn", ["normal", "abnormal"])
        pcc = st.selectbox("Chọn các cục máu trắng trong nước tiểu của bạn", ["present", "notpresent"])
        ba = st.selectbox("Chọn vi khuẩn trong nước tiểu của bạn", ["present", "notpresent"])
        bgr = st.slider("Chọn đường huyết ngẫu nhiên của bạn", 1, 500, 100, 1)
        bu = st.slider("Chọn ure trong máu của bạn", 1, 200, 50, 1)
        sc = st.slider("Chọn creatinin trong huyết tương của bạn", 1.0, 15.0, 1.2, 0.1)
        sod = st.slider("Chọn nồng độ natri của bạn", 1, 200, 100, 1)
        pot = st.slider("Chọn nồng độ kali của bạn", 1.0, 10.0, 4.0, 0.1)
        hemo = st.slider("Chọn hàm lượng hemoglobin của bạn", 1.0, 20.0, 15.0, 0.1)
        pcv = st.slider("Chọn tỷ lệ tế bào đỏ của bạn", 1, 54, 40, 1)
        wc = st.slider("Chọn đếm tế bào trắng của bạn", 1, 26400, 9800, 1)
        rc = st.slider("Chọn số lượng tế bào đỏ của bạn", 1.0, 18.0, 5.0, 0.1)
        htn = st.selectbox("Chọn tình trạng tăng huyết áp của bạn", ["yes", "no"])
        dm = st.selectbox("Chọn tình trạng tiểu đường của bạn", ["yes", "no"])
        cad = st.selectbox("Chọn bệnh động mạch vành của bạn", ["yes", "no"])
        appet = st.selectbox("Chọn tình trạng ăn uống của bạn", ["good", "poor"])
        pe = st.selectbox("Chọn tình trạng ứ nước của bạn", ["yes", "no"])
        ane = st.selectbox("Chọn tình trạng thiếu máu của bạn", ["yes", "no"])
        
          # Preprocess the input data
        new_data = preprocess_data(age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane)


                        # Make prediction
        prediction = model.predict(new_data)

                        # Get the prediction probabilities
        probabilities = model.predict_proba(new_data)

                        # Calculate the percentage of positive and negative predictions
        negative_percentage = round(probabilities[0][0] * 100, 2)
        positive_percentage = round(probabilities[0][1] * 100, 2)

                        # Display the percentages
        st.sidebar.write("Tỉ lệ không mắc bệnh:", negative_percentage, "%")
        st.sidebar.write("Tỉ lệ mắc bệnh:", positive_percentage, "%")
                # tạo chuỗi ngẫu nhiên bao gồm các ký tự chữ cái và số, có độ dài là 5
     
        # Display the prediction result
        if prediction == 0:
               st.sidebar.success('Khách hàng không bị bệnh thận.')
        else:
         st.sidebar.warning('Khách hàng bị bệnh thận.')

        if st.sidebar.button('Lưu dữ liệu triệu chứng xuống csdl'):
                try:
                    cursor.execute("""
                        INSERT INTO trieuchung (
                            matrieuchung, id, tuoi, huyetap, tytrongnuoctieu, albumin,
                            mucdoduongtrongnuoctieu, hongcautrongnuoctieu, tebaomutrongnuoctieu,
                            bongumutrongnuoctieu, vikhuantrongnuoctieu, luongduonghuyet,
                            nongdo_ure, nongdo_creatinine, nongdonatri, nongdokali,
                            nongdo_hemoglobin, thetichhongcau, soluongbachcau, soluonghongcau,
                            tanghuyetap, tieuduong, benhdongmachvanh, ngonmieng, phu_chan
                        )
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?)
                    """, (trieuchung, id_benh_nhan, age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe))
                    conn.commit()
                    st.success('Lưu thông tin bệnh nhân thành công!')    
                    try:
                                random_string1 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=2))
                                # thêm đoạn "tc" vào đầu chuỗi
                                malichsukham = "kq" + random_string1
                                    # Display the prediction result
                                if prediction == 0:
                                        ketluan = 'Bệnh nhân không bị bệnh.'
                                else:
                                    ketluan = 'Bệnh nhân bị bệnh thận.'
                                cursor.execute("INSERT INTO ketqua ( malichsukham, matrieuchung, tilemacbenh, tilekhongmacbenh, ketluan) VALUES (?, ?, ?,?,?)", (malichsukham, trieuchung, float(negative_percentage), float(positive_percentage),ketluan))
                                conn.commit()
                                st.success('Lưu thông tin thành công!')
                    except Exception as e:
                                st.write('<span style="color:red">Lưu lịch sử khám bệnh nhân thất bại!</span>', unsafe_allow_html=True)
                                print("Error:", e)
                except Exception as e:
                    st.write('<span style="color:red">Lưu thông tin bệnh nhân thất bại!</span>', unsafe_allow_html=True)
                    print("Error:", e)  
    else:
        st.title("Lịch sử khám bệnh")
        st.write("Trang web này hiển thị thông tin về lịch sử khám bệnh của bệnh nhân.")

        query = """SELECT thongtinbenhnhan.id, tenbenhnhan, diachi, sdt, gioitinh, 
        trieuchung.matrieuchung,tuoi ,huyetap, albumin, 
        mucdoduongtrongnuoctieu, hongcautrongnuoctieu, tebaomutrongnuoctieu, bongumutrongnuoctieu, 
        vikhuantrongnuoctieu, luongduonghuyet, nongdo_ure, nongdo_creatinine, nongdonatri, nongdokali, 
        nongdo_hemoglobin, thetichhongcau, soluongbachcau, soluonghongcau, tanghuyetap, tieuduong, 
        benhdongmachvanh, ngonmieng, phu_chan, ketqua.malichsukham,tilemacbenh,tilekhongmacbenh,ketluan
        FROM thongtinbenhnhan 
        JOIN trieuchung ON thongtinbenhnhan.id = trieuchung.id 
        LEFT JOIN ketqua ON trieuchung.matrieuchung = ketqua.matrieuchung
        """
        df = pd.read_sql(query, conn)

        # Display data on Streamlit app
        st.write("")
        st.write("## Thông tin khám bệnh:")
        st.write("Dưới đây là bảng thông tin chi tiết về lịch sử khám bệnh của bệnh nhân.")
        st.write("")
        st.dataframe(df)
        fig, ax = plt.subplots(1, 2, figsize=(12, 5))
        # Display age histogram
        st.write("")
        st.write("## Thống kê tuổi của bệnh nhân:")
        st.write("Dưới đây là biểu đồ thống kê về tuổi của bệnh nhân.")
        st.write("")
        fig, ax = plt.subplots(1, 2, figsize=(12, 5))

        # Plot age histogram
        ax[0].hist(df["tuoi"].astype(int), bins=20, alpha=0.8)
        ax[0].set_xlabel("Tuổi")
        ax[0].set_ylabel("Số lượng")
        ax[0].set_title("Biểu đồ tuổi")

        # Plot gender count chart
        gender_counts = df["gioitinh"].value_counts()
        ax[1].bar(gender_counts.index, gender_counts.values)
        ax[1].set_xlabel("Giới tính")
        ax[1].set_ylabel("Số lượng")
        ax[1].set_title("Thống kê giới tính")

        # Adjust spacing between subplots
        plt.tight_layout()
        # Đếm số lượng bệnh nhân theo cột "ketluan"

        # Display the subplots
        st.pyplot(fig)
          # Đếm số lượng bệnh nhân theo cột "ketluan"
        ketluan_counts = df["ketluan"].value_counts()

        # Tạo biểu đồ thanh ngang
        fig, ax = plt.subplots()
        ax.barh(ketluan_counts.index, ketluan_counts.values)

        # Đặt nhãn trục x và y
        ax.set_xlabel("Số lượng")
        ax.set_ylabel("Kết luận")

        # Đặt tiêu đề cho biểu đồ
        ax.set_title("Thống kê số lượng bệnh nhân theo kết luận")

        # Thiết lập kích thước biểu đồ
        fig.set_size_inches(4, 2)

        # Hiển thị biểu đồ trên Streamlit
        st.pyplot(fig)


        # Display patient status count chart
        st.write("")
        st.write("## Thống kê tình trạng bệnh của bệnh nhân:")
        status_counts = df["tilemacbenh"].value_counts(normalize=True)
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%')
        ax.axis('equal')
        ax.set_title("Thống kê tình trạng bệnh")
        fig.set_size_inches(4, 4)
        st.pyplot(fig)
        

     
    
# Run the main function
if __name__ == "__main__":
    main()
