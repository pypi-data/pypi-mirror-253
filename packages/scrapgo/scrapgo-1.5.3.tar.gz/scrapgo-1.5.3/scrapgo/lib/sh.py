import os, glob



def get_uniquify_path(path):
    n_path = path
    f, ext = os.path.splitext(path)
    n = 1
    while os.path.exists(n_path):
        n_path = f'{f}({n}){ext}'
        n += 1
    return n_path


def mkdirs(path, exists_ok=True):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir, exist_ok=exists_ok)


def fsave(content, path, exists='overwrite', dir_exists_ok=True, **kwargs):
    '''ifexists: overwrite|skip|distinct
    '''
    if isinstance(content, str):
        mode = 'wt'
    elif isinstance(content, bytes):
        mode = 'wb'
    else:
        raise ValueError(f'content must be bytes or text object. not {type(content)}')

    mkdirs(path, exists_ok=dir_exists_ok)

    if exists == 'distinct':
        path = get_uniquify_path(path)
    elif exists == 'skip':
        if os.path.exists(path):
            return 0
    elif exists == 'overwrite':
        pass
    else:
        raise ValueError(f'exists must be in overwrite, distinct, skip')

    with open(path, mode, **kwargs) as fp:
        fp.write(content)
    return len(content)


def fcount(pathname, recursive=False):
    files = [f for f in glob.glob(pathname, recursive=recursive)]
    count = len(files)
    return count


def ffind(pathname, recursive=False, many=True):
    files = [f for f in glob.glob(pathname, recursive=recursive)]
    if many:
        return files
    if files:
        return files[0]

def fdirname(p):
    return os.path.dirname(p)

def fbasename(p):
    return os.path.basename(p)


def fextname(p):
    return os.path.splitext(p)[1]


def fexists(path):
    return os.path.exists(path)


def fjoin(path, *paths):
    return os.path.join(path, *paths)


def clear4pathname(name_for_path:str):
    iligals = dict.fromkeys('\/:*?"<>|.')
    trantab = str.maketrans(iligals)
    return name_for_path.translate(trantab).strip()
