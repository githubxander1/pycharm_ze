from flask import Flask, request, send_from_directory, render_template, jsonify, url_for
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)

# 设置上传文件夹
app.config['UPLOAD_FOLDER'] = 'uploads'

# 确保上传文件夹存在
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# 处理默认路由
@app.route('/')
def index():
    return render_template('index.html')

# 处理上传文件
@app.route('/upload_file', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'success': True, 'filename': filename, 'type': 'file'})
    else:
        return jsonify({'success': False})

# 处理上传文本
@app.route('/upload_text', methods=['POST'])
def upload_text():
    text = request.form.get('text')
    if text:
        filename = f"uploaded_text_{len(os.listdir(app.config['UPLOAD_FOLDER'])) + 1}.txt"
        with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'w') as f:
            f.write(text)
        return jsonify({'success': True, 'filename': filename, 'type': 'text'})
    else:
        return jsonify({'success': False})

# 获取已上传文件列表
@app.route('/get_files')
def get_files():
    files = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        files.append({
            'name': filename,
            'size': os.path.getsize(file_path),
            'upload_time': datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify(files)

# 展示已上传文件
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

# 删除文件
@app.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'File not found'})

# 处理 favicon 请求
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)