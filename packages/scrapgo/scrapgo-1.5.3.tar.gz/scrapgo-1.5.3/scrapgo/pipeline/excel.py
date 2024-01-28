from typing import Union
import listorm, os, atexit, functools

from scrapgo.lib import pluralize


def excel2context(path, context_name, asvalues:Union[str, tuple]=None, sheetname=None):
    def wrapper(renderer):
        @functools.wraps(renderer)
        def load(*args, **kwargs):
            records = listorm.read_excel(path, sheet_name=sheetname)
            if asvalues:
                records = listorm.values(records, asvalues)
            kwargs[context_name] = records
            return renderer(*args, **kwargs)
        return load
    return wrapper




def pipe2excel(path, sheet_name=None, unique_keys=None, mode='append', bulk_size=1000, image_fields=None):
    records_buffer = []
    exists_values = []

    if os.path.exists(path):
        if unique_keys:
            exists_values = listorm.values(listorm.read_excel(path), unique_keys)
            
        if mode == 'overwrite':
            with open(path, 'wb') as fp:
                fp.close()

    def _feed_excel(records):
        print(f'pipe2excel: feed {len(records)} records to {path}...')
        listorm.write_excel(records, path, sheet_name, mode='append', image_fields=image_fields)

    def __flush_buffer():
        _feed_excel(records_buffer)

    atexit.register(__flush_buffer)

    def pipe(records, **kwargs):
        nonlocal records_buffer
        records = pluralize(records)

        for row in records:
            if unique_keys:
                values = listorm.asvalues(row, unique_keys)
                if values in exists_values:
                    continue
                exists_values.append(values)
            records_buffer.append(row)

        buffer_size = len(records_buffer)

        if buffer_size >= bulk_size:
            _feed_excel(records_buffer)
            records_buffer = []
    return pipe
        

