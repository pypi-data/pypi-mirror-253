import jsonlines, listorm, os, functools
from typing import Union

from scrapgo.lib import pluralize



def read_jsonl(path, **kwargs):
    if os.path.exists(path):
        with jsonlines.open(path, **kwargs) as fp:
            return list(fp)
    return []


def jsonl2context(path, context_name, asvalues:Union[str, tuple]=None):
    def wrapper(renderer):
        @functools.wraps(renderer)
        def load(*args, **kwargs):
            records = read_jsonl(path)
            if asvalues:
                records = listorm.values(records, asvalues)
            kwargs[context_name] = records
            return renderer(*args, **kwargs)
        return load
    return wrapper

    

def pipe2jsonl(file, unique_keys=None, mode='append', **jsonlines_kwargs):
    exists_values = []
    if isinstance(file, str):
        if os.path.exists(file):
            if mode == 'overwrite':
                with open(file, 'w') as fp:
                    fp.close()

            if unique_keys:
                exists_records = read_jsonl(file)
                exists_values = listorm.values(exists_records, unique_keys)
        else:
            os.makedirs(os.path.dirname(file), exist_ok=True)

    def pipe(records, **kwargs):
        records = pluralize(records)
        with jsonlines.open(file, mode='a', **jsonlines_kwargs) as fp:
            for row in records:
                if unique_keys:
                    values = listorm.asvalues(row, unique_keys)
                    if values in exists_values:
                        continue
                    exists_values.append(values)
                fp.write(row)
    return pipe


