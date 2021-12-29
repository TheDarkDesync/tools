from os.path import join, splitext, exists

def get_unique_path(dst: str, file: str) -> str:
    '''
    returns a unique path for the given filename `file`
    in the directory `dst`

    use if filenames might be duplicates
    '''
    base, extension = splitext(file)
    path = join(dst, file)
    path_exists = exists(path)
    i = 0
    while path_exists:
        i += 1
        path = join(dst, f'{base}_{i}{extension}')
        path_exists = exists(path)
    return path
