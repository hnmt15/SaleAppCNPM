import json
from saleapp import db, app
from sqlalchemy import Column, Integer, String, Float, ForeignKey, false
from sqlalchemy.orm import relationship


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), unique=True, nullable=False)
    products = relationship('Product', backref="category", lazy=True)

    def __str__(self):
        return self.name

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), unique=True, nullable=False)
    image = Column(String(300), default="https://ntstore.com.vn/wp-content/uploads/2025/02/ntstore_samsung-galaxy-s24-ultra-xam-1-2.png.webp")
    price = Column(Float, default=0.0)
    cate_id = Column(Integer, ForeignKey(Category.id), nullable=False)



if __name__=="__main__":
    with app.app_context():
        # db.create_all()
        # c1 = Category(name="Laptop")
        # c2 = Category(name="Mobile")
        # c3 = Category(name="Tablet")
        #
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()

        with open("data/product.json", encoding="utf-8") as f:
            products = json.load(f)

            for p in products:
                try:
                    prod = Product(
                        name=p["name"],
                        price=p["price"],
                        image=p["image"],
                        cate_id=p["cate_id"]
                    )
                    db.session.add(prod)
                    db.session.commit()
                except Exception as ex:
                    print(f"Lỗi khi thêm sản phẩm: {p['name']} → {ex}")
                    db.session.rollback()



