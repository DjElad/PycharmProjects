import base64

base64_message = 'CgkJICAgICAgICAgICAgICAgIAo' \
                 'gICAgICAgICAgICAgICAuLS0tW1tfX11dLS' \
                 '0tLS4KICAgICAgICAgICAgICA7LS0tLS0tLS0tLS' \
                 '0tLS58ICAgICAgIF9fX18KICAgICAgICAgICAgICB8ICA' \
                 'gICAgICAgICAgIHx8ICAgLi0tW1tfX11dLS0tLgogICAgIC' \
                 'AgICAgICAgIHwgICAgICAgICAgICAgfHwgIDstLS0tLS0tLS0' \
                 'tLS58CiAgICAgICAgICAgICAgfCAgICAgICAgICAgICB8fCA' \
                 'gfCAgICAgICAgICAgfHwKICAgICAgICAgICAgICB8X19fX19f' \
                 'X19fX19fX3wvICB8ICAgICAgICAgICB8fAogICAgICAgICAgI' \
                 'CAgICAgICAgICAgICAgICAgICAgIHxfX19fX19fX19fX3wvC' \
                 'go='
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')

print(message)