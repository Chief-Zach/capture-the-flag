import base64
x = "mJsNcbm3yOvvjYbPkeb5VNyaZgIJERnsyR!oFZTXRpl-EkuFBCSsHxIpXBiS7WQ63Qu-OgYDQFoowXX11Yis2K65yc3cRwRQnsh!yqtPUNTHD1p0LLSOyOVQQhQfCsF6tYfyzQn0Don8JzlUZMS3qwDiXFO4Add1z04RgySEc5AKUQPKdTQEHWIDEJ-MQitfjqjvDJT9OkDBRaKbBHeiGg~~ "
replaced = x.replace('~', '=').replace('!', '/').replace('-', '+')
print(replaced)
replaced = bytes(replaced, 'utf-8')
b64d = base64.decodebytes(replaced)
print(b64d)