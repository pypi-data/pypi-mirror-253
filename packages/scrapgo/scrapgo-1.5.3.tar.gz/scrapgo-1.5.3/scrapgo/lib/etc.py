from typing import Mapping, Union
import math
from random import random


def gen_random_value(low:int, high:int, rounds=2):
    width = high - low
    v = low+random()*width
    return round(v, rounds)


def format_bytes_size(length, ndigits=None):
    k = 1024
    m = k**2
    g = k**3

    if length > k:
        unit = 'K'
        v = length / k
    elif length > m:
        unit = 'M'
        v = length / m
    elif length > g:
        unit = 'G'
        v = length / g
    else:
        unit = 'bytes'
        v = length
    return f'{round(v, ndigits)}{unit}'


def array2matrix(array:list, n:int, orphan=True):
    length = len(array)
    s, e = 0, n
    result = []
    while e < length:
        slc = array[s:e]
        s = e
        e = e + n
        result.append(slc)

    rest = array[s:e]
    is_orphan = rest and len(rest) < n

    if not is_orphan:
        result.append(rest)
    
    if is_orphan:
        if orphan:
            result.append(rest)
    return result


def get_next_rotate(iterable, current):
    rotater = list(iterable) * 2
    for i, value in enumerate(rotater):
        if current == value:
            return rotater[i+1]
    raise ValueError(f'Cannot find {current} in {iterable}')


def get_rotate(iterable):
    if iterable:
        first, *rest = iterable
        return [*rest, first]
    raise ValueError(f'{iterable}must have at least one element')


def npaginator(page_size:Union[int, Mapping]=None, total_count:int=0, last_page_number:int=None, start:int=1, step:int=1, page_param:str=None, paramset:dict=None):
    if page_param:
        for page in npaginator(page_size, total_count, last_page_number, start, step):
            if not paramset:
                yield {page_param: page}
            else:
                yield {**paramset, page_param:page}

    else:
        if isinstance(page_size, int):
            last = last_page_number or math.ceil(total_count / page_size)
            if start == 0:
                yield from range(start, last, step)
            else:
                yield from range(start, last + 1, step)

        elif page_size is None:
            if last_page_number:
                yield from range(start, last_page_number + 1, step)
            else:
                page = start
                while True:
                    yield page
                    page += step

        elif isinstance(page_size, Mapping):
            yield start
            _page_size = page_size.get('page_size')
            _total_count = page_size.get('total_count')
            _last_page_number = page_size.get('last_page_number') or page_size.get('last_page')
            yield from npaginator(_page_size, _total_count, _last_page_number, start, step)
        
        else:
            raise ValueError(page_size)


