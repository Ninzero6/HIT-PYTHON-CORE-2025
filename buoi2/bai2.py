a=int(input("Nhap luong nhan vien(trieu dong): "))
if a>15 :
    tn =a-a*0.3
    print("Thu nhap cua nhan vien do la:",tn)
elif 7<=a<=15:
    tn =a-a*0.2
    print("Thu nhap nhan vien do la:",tn)
elif a<7:
    tn= a-a*0.1
    print("Thu nhap nhan vien do la:",tn)

