from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import User, Project, Menu, Page

admin = Blueprint('admin', __name__)

@admin.route('/')
@login_required
def dashboard():
    project_count = Project.query.count()
    menu_count = Menu.query.count()
    page_count = Page.query.count()
    return render_template('admin/dashboard.html', p_count=project_count, m_count=menu_count, pg_count=page_count)

# --- MANAJEMEN MENU ---
@admin.route('/menus')
@login_required
def manage_menus():
    menus = Menu.query.order_by(Menu.position).all()
    return render_template('admin/menus.html', menus=menus)

@admin.route('/menu/add', methods=['POST'])
@login_required
def add_menu():
    name = request.form['name']
    url = request.form['url']
    new_menu = Menu(name=name, url=url, position=Menu.query.count() + 1)
    db.session.add(new_menu)
    db.session.commit()
    flash('Menu baru berhasil ditambahkan!', 'success')
    return redirect(url_for('admin.manage_menus'))

# --- MANAJEMEN HALAMAN (CMS) ---
@admin.route('/pages')
@login_required
def manage_pages():
    pages = Page.query.all()
    return render_template('admin/pages.html', pages=pages)

@admin.route('/page/add', methods=['GET', 'POST'])
@login_required
def add_page():
    if request.method == 'POST':
        title = request.form['title']
        slug = request.form['slug'].lower().replace(' ', '-')
        content = request.form['content']
        new_pg = Page(title=title, slug=slug, content=content)
        db.session.add(new_pg)
        db.session.commit()
        flash('Halaman baru berhasil dibuat!', 'success')
        return redirect(url_for('admin.manage_pages'))
    return render_template('admin/form_page.html')

# --- MANAJEMEN PROYEK ---
@admin.route('/projects')
@login_required
def manage_projects():
    projects = Project.query.all()
    return render_template('admin/projects.html', projects=projects)

