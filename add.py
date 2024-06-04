
from app import create_app, db
from app.models import TinhThanhPhoMl, HuyenQuanMl, QuyHoachMl

def add_data():
    # Tạo ứng dụng Flask
    app = create_app()

    # Thiết lập ngữ cảnh ứng dụng
    with app.app_context():
        # Tạo bảng trong cơ sở dữ liệu (nếu chưa tồn tại)
        db.create_all()

        # Thêm dữ liệu vào cơ sở dữ liệu
        tinh_thanh_pho_list = [
            TinhThanhPhoMl(TenTinhThanhPho='Ha Noi'),
            TinhThanhPhoMl(TenTinhThanhPho='Ho Chi Minh'),
            TinhThanhPhoMl(TenTinhThanhPho='Da Nang')
        ]

        huyen_quan_list = [
            HuyenQuanMl(TenHuyenQuan='Ba Dinh', TinhThanhPhoID=1),
            HuyenQuanMl(TenHuyenQuan='Cau Giay', TinhThanhPhoID=1),
            HuyenQuanMl(TenHuyenQuan='Hoan Kiem', TinhThanhPhoID=1),
            HuyenQuanMl(TenHuyenQuan='Hai Ba Trung', TinhThanhPhoID=1),
            HuyenQuanMl(TenHuyenQuan='Hoang Mai', TinhThanhPhoID=1),
            HuyenQuanMl(TenHuyenQuan='Dong Da', TinhThanhPhoID=1),
            HuyenQuanMl(TenHuyenQuan='Tay Ho', TinhThanhPhoID=1),
            HuyenQuanMl(TenHuyenQuan='Thanh Xuan', TinhThanhPhoID=1),
            HuyenQuanMl(TenHuyenQuan='Bac Tu Liem', TinhThanhPhoID=1),
            HuyenQuanMl(TenHuyenQuan='Ha Dong', TinhThanhPhoID=1),
            HuyenQuanMl(TenHuyenQuan='Long Bien', TinhThanhPhoID=1),
            HuyenQuanMl(TenHuyenQuan='Nam Tu Liem', TinhThanhPhoID=1),
            HuyenQuanMl(TenHuyenQuan='Ba Vi', TinhThanhPhoID=1),
            HuyenQuanMl(TenHuyenQuan='Chuong My', TinhThanhPhoID=1),
            HuyenQuanMl(TenHuyenQuan='Dan Phuong', TinhThanhPhoID=1),
        ]

        quy_hoach_list = [
            QuyHoachMl(HuyenQuanID=1, HinhanhQuyHoach='path/to/image1.jpg'),
            QuyHoachMl(HuyenQuanID=2, HinhanhQuyHoach='path/to/image2.jpg'),
            # Thêm các đối tượng quy_hoach_list khác vào đây
        ]

        db.session.add_all(tinh_thanh_pho_list)
        db.session.add_all(huyen_quan_list)
        db.session.add_all(quy_hoach_list)

        # Commit để lưu các thay đổi vào cơ sở dữ liệu
        db.session.commit()

# Gọi hàm để thêm dữ liệu khi chạy script
if __name__ == "__main__":
    add_data()
