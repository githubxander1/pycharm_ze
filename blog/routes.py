from flask import Flask, render_template, request, redirect
import os
from werkzeug.utils import secure_filename, send_from_directory
from bs4 import BeautifulSoup

app = Flask(__name__)

# 设置模板文件夹路径
template_dir = os.path.abspath('templates')
app.template_folder = template_dir

# 设置上传文件夹路径
upload_folder = os.path.abspath('uploads')
app.config['UPLOAD_FOLDER'] = upload_folder

# 设置允许上传的文件类型
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# 假设有一个名为posts的列表，用于存储博客文章
posts = [
    {
        'title': '第一篇博客文章',
        'content': '这是我的第一篇博客文章。',
    },
    {
        'title': '第二篇博客文章',
        'content': '这是我的第二篇博客文章。',
    }
]

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        title = request.form['title']
        content_html = request.form['content']
        file = request.files['file']

        # 检查文件类型是否允许上传
        if file and allowed_file(file.filename):
            # 生成安全的文件名
            filename = secure_filename(file.filename)
            # 保存文件到指定路径
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # 将HTML内容解析为纯文本
            content_plain = BeautifulSoup(content_html, 'html.parser').get_text()

            new_post = {
                'title': title,
                'content': content_plain,
                'filename': filename
            }
            posts.append(new_post)
            return redirect('/')
        print(request.form)

    return render_template('post.html')

@app.route('/admin')
def admin():
    return render_template('admin.html', posts=posts)

@app.route('/admin/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    if request.method == 'POST':
        title = request.form['title']
        content_html = request.form['content']

        # 将HTML内容解析为纯文本
        content_plain = BeautifulSoup(content_html, 'html.parser').get_text()

        posts[index]['title'] = title
        posts[index]['content'] = content_plain
        return redirect('/admin')
    return render_template('edit.html', post=posts[index])

@app.route('/admin/delete/<int:index>')
def delete(index):
    del posts[index]
    return redirect('/admin')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)