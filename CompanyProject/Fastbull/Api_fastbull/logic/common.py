import hashlib

def generate_btoken(client_type, client_version, uuid, device_no):
    raw_str = f"{client_type}_{client_version}_{uuid}_{device_no}"
    btoken = hashlib.md5(raw_str.encode('utf-8')).hexdigest().lower()
    return btoken

# 示例：使用测试的uuid和deviceNo（web）
uuid_web = "22fe60c8ab2abcf803c386d8edd4353f"
device_no = "2a3cd0189ea31b1d5f177b66df8705f8"  # 根据实际情况填写设备号
client_type_web = "4"  # web客户端类型
client_version_web = "latest"

btoken_web = generate_btoken(client_type_web, client_version_web, uuid_web, device_no)
print(f"Web客户端的bToken: {btoken_web}")

# 如果是其他环境或客户端类型，替换相应的uuid、client_type和client_version即可。