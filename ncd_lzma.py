import lzma

def ncd(x,y):       
    """gets the NCD between two files x and y"""
    x_y = x + y
    x_comp = lzma.compress(x.encode("utf-8"))  # compress file 1
    y_comp = lzma.compress(y.encode("utf-8"))  # compress file 2
    x_y_comp = lzma.compress(x_y.encode("utf-8"))  # compress file concatenated

    return (len(x_y_comp) - min(len(x_comp), len(y_comp))) / max(len(x_comp), len(y_comp))