import base64

base64.b64encode(b"abc")

# 输出: b'YWJj'

base64.b64decode(b"YWJj")

# 输出: b'ab'

base64.b64encode(b"abc123")

# 输出: b'YWJjMjEyMw=='

base64.b64decode(b"YWJjMjEyMw==")

# 输出: b'ab')