from app import create_app, db
from app.models import Project, Menu, Page, User

app = create_app()

with app.app_context():
    db.create_all()
    
    if not User.query.filter_by(username='admin').first():
        admin_user = User(username='admin')
        admin_user.set_password('AdminPorto2026!') # Gantilah password ini nanti
        db.session.add(admin_user)
        db.session.commit()
        print("Akun admin default berhasil dibuat. Username: admin, Password: AdminPorto2026!")
    
    # Masukkan data sampel jika database masih kosong
    if not Project.query.first():
        p1 = Project(title="Deteksi Kematangan TBS", description="Klasifikasi 3 tingkat kematangan buah kelapa sawit menggunakan arsitektur ResNet-50.", tech_stack="Python, PyTorch, Flask")
        p2 = Project(title="CyberGuard Dashboard", description="Sistem monitoring modul dan manajemen kuesioner dinamis untuk mahasiswa.", tech_stack="Flask, SQLite, Bootstrap")
        p3 = Project(title="SPK Duta Bahasa", description="Sistem pendukung keputusan seleksi Duta Bahasa Provinsi Aceh menggunakan metode SMART dan TOPSIS.", tech_stack="Python, Scikit-learn")
        db.session.add_all([p1, p2, p3])
        
        m1 = Menu(name="Beranda", url="/", position=1)
        m2 = Menu(name="Tentang", url="/tentang", position=2)
        db.session.add_all([m1, m2])
        
        pg1 = Page(slug="tentang", title="Tentang Saya", content="Latar belakang di bidang rekayasa perangkat lunak dan kecerdasan buatan.")
        db.session.add(pg1)
        
        db.session.commit()
        print("Database diinisialisasi beserta data awal.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)