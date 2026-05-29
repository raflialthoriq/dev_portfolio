from flask import Blueprint, render_template, abort
from app.models import Menu, Page, Project

main = Blueprint('main', __name__)

@main.context_processor
def inject_menus():
    menus = Menu.query.order_by(Menu.position).all()
    return dict(menus=menus)

@main.route('/')
def index():
    # 1. Definisikan data profil Anda (sementara menggunakan dictionary)
    profile = {
        'name': 'M. Rafli Al Thoriq',
        'bio': 'Fokus pada riset dan pengembangan model deep learning, khususnya arsitektur Convolutional Neural Networks (CNN) untuk otomatisasi di bidang pertanian. Berpengalaman dalam men-deploy model machine learning menggunakan Flask dan integrasi tunneling (Ngrok) untuk akses nirkabel secara real-time. Selain kecerdasan buatan, juga aktif mengembangkan sistem pendukung keputusan dan dashboard administratif berbasis web.'
    }
    
    # 2. Ambil data proyek dari database
    projects = Project.query.order_by(Project.created_at.desc()).limit(6).all()
    
    # 3. Sertakan variabel 'profile' ke dalam render_template
    return render_template('index.html', projects=projects, profile=profile)

@main.route('/<slug>')
def dynamic_page(slug):
    page = Page.query.filter_by(slug=slug).first_or_404()
    return render_template('page.html', page=page)