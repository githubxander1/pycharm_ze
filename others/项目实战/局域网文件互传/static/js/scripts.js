document.getElementById('file-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    fetch('{{ url_for("upload_file") }}', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('upload-result').textContent = data.success ? '文件上传成功' : '文件上传失败';
        if (data.success) {
            updateFileList();
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('upload-result').textContent = '文件上传失败';
    });
});

document.getElementById('text-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    fetch('{{ url_for("upload_text") }}', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('upload-result').textContent = data.success ? '文本上传成功' : '文本上传失败';
        if (data.success) {
            updateFileList();
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('upload-result').textContent = '文本上传失败';
    });
});