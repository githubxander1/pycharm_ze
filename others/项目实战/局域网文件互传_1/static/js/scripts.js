document.getElementById('file-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    fetch('{{ url_for("upload_file") }}', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById('upload-result').textContent = '文件上传成功';
            updateFileList();
        } else {
            document.getElementById('upload-result').textContent = '文件上传失败';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('upload-result').textContent = '文件上传失败';
    });
});

document.getElementById('text-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    fetch('{{ url_for("upload_text") }}', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById('upload-result').textContent = '文本上传成功';
            updateFileList();
        } else {
            document.getElementById('upload-result').textContent = '文本上传失败';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('upload-result').textContent = '文本上传失败';
    });
});

function updateFileList() {
    fetch('{{ url_for("get_files") }}')
        .then(response => response.json())
        .then(data => {
            const fileList = document.getElementById('file-list');
            const noFiles = document.getElementById('no-files');
            fileList.innerHTML = '';
            noFiles.style.display = 'none';

            if (data.length === 0) {
                noFiles.style.display = 'block';
            } else {
                data.forEach(file => {
                    const listItem = document.createElement('li');
                    const link = document.createElement('a');
                    link.href = `/uploads/${encodeURIComponent(file.name)}`;
                    link.textContent = file.name;
                    link.target = "_blank"; // 打开新标签页查看文件
                    const downloadButton = document.createElement('button');
                    downloadButton.textContent = '下载';
                    downloadButton.onclick = () => downloadFile(file.name);
                    const copyButton = document.createElement('button');
                    copyButton.textContent = '复制';
                    copyButton.onclick = () => copyTextToClipboard(file.name);
                    const sizeText = document.createElement('span');
                    sizeText.textContent = `大小: ${file.size} bytes`;
                    const timeText = document.createElement('span');
                    timeText.textContent = ` - 上传时间: ${file.upload_time}`;
                    const deleteButton = document.createElement('button');
                    deleteButton.textContent = '删除';
                    deleteButton.onclick = () => deleteFile(file.name);

                    listItem.appendChild(downloadButton);
                    listItem.appendChild(copyButton);
                    listItem.appendChild(link);
                    listItem.appendChild(sizeText);
                    listItem.appendChild(timeText);
                    listItem.appendChild(deleteButton);
                    fileList.appendChild(listItem);
                });
            }
        });
}

function downloadFile(filename) {
    window.location.href = `/uploads/${encodeURIComponent(filename)}`;
}

function copyTextToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        alert('文本已复制到剪贴板');
    }, function(err) {
        console.error('无法复制文本: ', err);
    });
}

function deleteFile(filename) {
    if (confirm("确定要删除此文件吗？")) {
        fetch(`/delete/${encodeURIComponent(filename)}`, { method: 'DELETE' })
        .then(response => {
            if (response.ok) {
                alert('删除成功');
                updateFileList();
            } else {
                alert('删除失败');
            }
        })
        .catch(error => console.error('Error:', error));
    }
}

// 初始化文件列表
updateFileList();

// 每隔 2 秒更新一次文件列表
setInterval(updateFileList, 2000);