from saleapp import app, db
from saleapp.models import Category

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        c1 = Category(name="Laptop")
        c2 = Category(name="Mobile")
        c3 = Category(name="Tablet")

        db.session.add_all([c1, c2, c3])
        db.session.commit()

        print("✅ Dữ liệu mẫu đã được thêm vào database!")
