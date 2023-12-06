create database ChuanDoanCKD
go
use ChuanDoanCKD

create table thongtinbenhnhan
(
 id varchar(10) primary key not null ,
 tenbenhnhan nvarchar(255),
 diachi nvarchar(255),
 sdt varchar(20),
 gioitinh nvarchar(10)
)
go

create table trieuchung 
(matrieuchung varchar(10) primary key not null,
id varchar(10) ,
tuoi int,
huyetap varchar(100),
tytrongnuoctieu varchar(100),
albumin varchar(100) ,
mucdoduongtrongnuoctieu varchar(100),
hongcautrongnuoctieu varchar(100),
tebaomutrongnuoctieu varchar(100) ,
bongumutrongnuoctieu varchar(100) ,
vikhuantrongnuoctieu varchar(100) ,
luongduonghuyet int ,
nongdo_ure int ,
nongdo_creatinine float ,
nongdonatri float,
nongdokali float ,
nongdo_hemoglobin float ,
thetichhongcau int ,
soluongbachcau float ,
soluonghongcau float ,
tanghuyetap varchar(100) ,
tieuduong varchar(100) ,
benhdongmachvanh varchar(100) ,
ngonmieng varchar(100) ,
phu_chan varchar(100) ,
constraint fk_trieuchung_id foreign key (id) references thongtinbenhnhan(id)
)
go
create table ketqua
(
 malichsukham varchar(10) primary key not null ,
 matrieuchung varchar(10),
 tilemacbenh float,
 tilekhongmacbenh float,
 ketluan nvarchar(100),
 constraint fk_1 foreign key (matrieuchung) references trieuchung(matrieuchung)
)
go
INSERT INTO thongtinbenhnhan (id, tenbenhnhan, diachi, sdt, gioitinh)
VALUES
    ('BN001', N'Nguyen Van A', N'Hà Nộii', '0123456789', 'Nam'),
    ('BN002', N'Tran Thi B', N'TP.HCM', '0987654321', N'Nữ'),
    ('BN003', N'Lê Quang C', N'Ðà Nằng', '0912345678', 'Nam'),
    ('BN004', N'Phạm Thị D', N'Hải Phòng', '0845678901', N'Nữ'),
    ('BN005', N'Hoàng Van E', N'Hu?', '0765432190', 'Nam'),
    ('BN006', N'Vu Thị F', N'Cần Tho', '0798765432', N'Nữ'),
    ('BN007', N'Ngô Van G', N'Bình Duong', '0678901234', 'Nam'),
    ('BN008', N'Trần Thị H', N'Quảng Ninh', '0923456789', N'Nữ'),
    ('BN009', N'Lê Van I', N'Vung Tàu', '0865432190', 'Nam'),
    ('BN010', N'Phạm Thị K', N'Long An', '0767890123', N'Nữ');

INSERT INTO trieuchung (matrieuchung, id, tuoi, huyetap, tytrongnuoctieu, albumin, mucdoduongtrongnuoctieu, hongcautrongnuoctieu, tebaomutrongnuoctieu, bongumutrongnuoctieu, vikhuantrongnuoctieu, luongduonghuyet, nongdo_ure, nongdo_creatinine, nongdonatri, nongdokali, nongdo_hemoglobin, thetichhongcau, soluongbachcau, soluonghongcau, tanghuyetap, tieuduong, benhdongmachvanh, ngonmieng, phu_chan)
VALUES
    ('TC001', 'BN001', 30, '120/80', 'Normal', 'Negative', 'Normal', 'Negative', 'Negative', 'Negative', 'Negative', 90, 25, 1.2, 140, 4.5, 13.5, 4500000, 5000, 4500000, 'No', 'No', 'No', 'No', 'No'),
    ('TC002', 'BN002', 45, '130/90', 'High', 'Negative', 'Normal', 'Negative', 'Negative', 'Negative', 'Negative', 100, 30, 1.5, 135, 4.8, 14.2, 5000000, 5500, 4800000, 'Yes', 'No', 'No', 'No', 'No'),
    ('TC003', 'BN003', 50, '140/95', 'High', 'Positive', 'Abnormal', 'Positive', 'Positive', 'Negative', 'Negative', 110, 35, 1.8, 130, 5.2, 14.8, 5500000, 6000, 5100000, 'Yes', 'Yes', 'No', 'No', 'Yes'),
    ('TC004', 'BN004', 35, '125/85', 'Normal', 'Negative', 'Normal', 'Negative', 'Negative', 'Negative', 'Negative', 95, 28, 1.3, 138, 4.7, 14.1, 4800000, 5200, 4700000, 'No', 'No', 'No', 'No', 'No'),
    ('TC005', 'BN005', 60, '150/100', 'High', 'Positive', 'Abnormal', 'Positive', 'Positive', 'Positive', 'Negative', 120, 40, 2.0, 125, 5.5, 15.0, 6000000, 6500, 5200000, 'Yes', 'Yes', 'No', 'No', 'Yes'),
    ('TC006', 'BN006', 42, '135/92', 'High', 'Negative', 'Normal', 'Negative', 'Negative', 'Negative', 'Negative', 105, 32, 1.6, 132, 4.9, 14.4, 5200000, 5700, 4900000, 'Yes', 'No', 'Yes', 'No', 'No'),
    ('TC007', 'BN007', 55, '140/95', 'High', 'Positive', 'Abnormal', 'Positive', 'Positive', 'Positive', 'Negative', 115, 38, 1.9, 128, 5.3, 14.9, 5800000, 6200, 5300000, 'Yes', 'Yes', 'No', 'Yes', 'Yes'),
    ('TC008', 'BN008', 28, '118/82', 'Normal', 'Negative', 'Normal', 'Negative', 'Negative', 'Negative', 'Negative', 88, 24, 1.1, 142, 4.4, 13.4, 4400000, 4800, 4400000, 'No', 'No', 'No', 'No', 'No'),
    ('TC009', 'BN009', 47, '130/88', 'High', 'Positive', 'Abnormal', 'Positive', 'Positive', 'Positive', 'Negative', 98, 29, 1.4, 136, 4.6, 13.9, 4900000, 5400, 4600000, 'Yes', 'Yes', 'No', 'No', 'Yes'),
    ('TC010', 'BN010', 32, '125/85', 'Normal', 'Negative', 'Normal', 'Negative', 'Negative', 'Negative', 'Negative', 93, 26, 1.2, 139, 4.5, 13.6, 4700000, 5100, 4500000, 'No', 'No', 'No', 'No', 'No');
INSERT INTO ketqua (malichsukham, matrieuchung, tilemacbenh, tilekhongmacbenh, ketluan)
VALUES
    ('KQ001', 'TC001', 30.0, 70.0, N'Bệnh nhân không bị bệnh thận.'),
    ('KQ002', 'TC002', 80.0, 20.0, N'Bệnh nhân bị bệnh thận.'),
    ('KQ003', 'TC003', 90.0, 10.0, N'Bệnh nhân không bị bệnh thận.'),
    ('KQ004', 'TC004', 40.0, 60.0, N'Bệnh nhân bị bệnh thận.'),
    ('KQ005', 'TC005', 70.0, 30.0, N'Bệnh nhân không bị bệnh thận.'),
    ('KQ006', 'TC006', 60.0, 40.0, N'Bệnh nhân không bị bệnh thận.'),
    ('KQ007', 'TC007', 90.0, 10.0, N'Bệnh nhân bị bệnh thận.'),
    ('KQ008', 'TC008', 20.0, 80.0, N'Bệnh nhân không bị bệnh thận.'),
    ('KQ009', 'TC009', 80.0, 20.0, N'Bệnh nhân bị bệnh thận.'),
    ('KQ010', 'TC010', 50.0, 50.0, N'Bệnh nhân không bị bệnh thận.');
	

      
