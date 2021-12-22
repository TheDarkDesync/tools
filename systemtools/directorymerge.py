from os import walk
from os.path import join
from shutil import copy2, move # preserves timestamp
from tkinter import Tk
from tkinter.filedialog import askdirectory

from util.path import get_unique_path

def merge_dir(src: str, dst: str, move: bool = False, depth: int = 0) -> None:
    '''
    Merges Directories, by moving contents
    of subdirectories of `src` into `dst`.

    specify `move` as true to move instead of moving
    (default=False, copy)

    specify `depth` to configure depth of search in `src`
    (default=0, only first subdirectories)
    '''

    walker = walk(src) # files and directories

    # scnd argument: default
    directories, filenames = next(walker, (None, [], []))[1:]

    for dir in directories:
        path = join(src, dir)
        if depth >= 0:
            merge_dir(path, dst, move, depth - 1)

    for file in filenames:
        src_path = join(src, file)
        dst_path = get_unique_path(dst, file)
        try:
            move(src_path, dst_path) if move else copy2(src_path, dst_path)
        except IOError:
            print(f'Couldn\'t write to {dst}')
            return

if __name__ == "__main__":
    Tk().withdraw()
    src = askdirectory(title='Select directoy which contents you want to merge')
    dst = askdirectory(title='Select directoy where you want to merge')
    merge_dir(src, dst)
