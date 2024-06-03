from .. import db

class TinhThanhPhoMl(db.Model):
    __tablename__ = 'TinhThanhPho'

    TinhThanhPhoID = db.Column(db.Integer, primary_key=True)
    TenTinhThanhPho = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        return f'<TinhThanhPho {self.TenTinhThanhPho}>'
    
class HuyenQuanMl(db.Model):
    __tablename__ = 'HuyenQuan'

    HuyenQuanID = db.Column(db.Integer, primary_key=True)
    TenHuyenQuan = db.Column(db.String(100), nullable=False)
    TinhThanhPhoID = db.Column(db.Integer, db.ForeignKey('TinhThanhPho.TinhThanhPhoID'), nullable = False)

    def __repr__(self):
        return f'<HuyenQuan {self.TenHuyenQuan}>'