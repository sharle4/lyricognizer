import lzma
import bz2
import zlib

def compress_data(data, method):
    if method == 'lzma':
        return lzma.compress(data.encode('utf-8'))
    elif method == 'bz2':
        return bz2.compress(data.encode('utf-8'))
    elif method == 'zlib':
        return zlib.compress(data.encode('utf-8'))

def ncd(x, y, method):
    x_y = x + ' ' + y
    x_comp = compress_data(x, method)
    y_comp = compress_data(y, method)
    x_y_comp = compress_data(x_y, method)

    return (len(x_y_comp) - min(len(x_comp), len(y_comp))) / max(len(x_comp), len(y_comp))
