import base64
data = "mJsNcbm3yOvvjYbPkeb5VNyaZgIJERnsyR!oFZTXRpl-EkuFBCSsHxIpXBiS7WQ63Qu-OgYDQFoowXX11Yis2K65yc3cRwRQnsh!yqtPUNTHD1p0LLSOyOVQQhQfCsF6tYfyzQn0Don8JzlUZMS3qwDiXFO4Add1z04RgySEc5AKUQPKdTQEHWIDEJ-MQitfjqjvDJT9OkDBRaKbBHeiGg~~"
b64d = lambda x: base64.decodebytes(x.replace('~', '=').replace('!', '/').replace('-', '+'))
data = b64d(data)
print(data)