from flask import Flask, request, send_from_directory, render_template_string
import os

app = Flask(__name__)

# 设置上传文件夹
app.config['UPLOAD_FOLDER'] = 'uploads'

# 确保上传文件夹存在
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# 创建 HTML 表单和展示页面
html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>文件上传与管理</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
        }
        h1 {
            font-size: 2em;
            color: #333;
        }
        form {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 20px;
        }
        input[type="file"] {
            margin-bottom: 10px;
            font-size: 1.2em;
        }
        input[type="submit"] {
            font-size: 1.2em;
            padding: 10px 20px;
            cursor: pointer;
        }
        .files-list {
            margin-top: 20px;
            width: 80%;
            max-width: 600px;
            background-color: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .files-list ul {
            list-style: none;
            padding: 0;
        }
        .files-list li {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
            font-size: 1.2em;
        }
        .files-list a {
            color: blue;
            text-decoration: none;
        }
        .files-list button {
            background-color: red;
            color: white;
            border: none;
            padding: 5px 10px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>上传文件</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <br><br>
        <input type="submit" value="上传文件">
    </form>
    <div class="files-list" id="files-list">
        <ul id="file-list">
        </ul>
    </div>

    <script>
        function updateFileList() {
            fetch('/get_files')
                .then(response => response.json())
                .then(data => {
                    const fileList = document.getElementById('file-list');
                    fileList.innerHTML = '';
                    data.files.forEach(file => {
                        const listItem = document.createElement('li');
                        const link = document.createElement('a');
                        link.href = '/uploads/' + file;
                        link.textContent = file;
                        const deleteButton = document.createElement('button');
                        deleteButton.textContent = '删除';
                        deleteButton.onclick = () => deleteFile(file);

                        listItem.appendChild(link);
                        listItem.appendChild(deleteButton);
                        fileList.appendChild(listItem);
                    });
                });
        }

        function deleteFile(filename) {
            if (confirm("确定要删除此文件吗？")) {
                fetch('/delete/' + filename, { method: 'DELETE' })
                    .then(response => response.text())
                    .then(data => {
                        if (data === '删除成功') {
                            updateFileList();
                        } else {
                            alert(data);
                        }
                    });
            }
        }

        // 初始化文件列表
        updateFileList();

        // 每隔 2 秒更新一次文件列表
        setInterval(updateFileList, 2000);
    </script>
</body>
</html>
"""

# 处理默认路由
@app.route('/')
def index():
    return render_template_string(html_form)

# 处理上传文件
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return '文件上传成功'
    else:
        return '未接收到文件'

# 获取已上传文件列表
@app.route('/get_files')
def get_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return {'files': files}

# 展示已上传文件
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# 删除文件
@app.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return '删除成功'
    else:
        return '文件不存在'

# 处理 favicon 请求
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
