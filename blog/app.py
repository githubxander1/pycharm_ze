# 用于启动Flask应用
import os

from blog import routes
from blog.routes import app

# 设置上传文件的保存路径
upload_dir = os.path.abspath('uploads')
app.config['UPLOAD_FOLDER'] = upload_dir

# 设置允许的文件类型
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app.run(debug=True)