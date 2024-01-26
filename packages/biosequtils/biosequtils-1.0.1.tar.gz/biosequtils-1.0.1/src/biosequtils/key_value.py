'''
operate dictionary
'''
from copy import deepcopy

class KeyValue:
    
    @staticmethod
    def print_dict(indict:dict):
        '''
        print dictionary to stdout for debugging
        '''
        n = 1
        for key in sorted(indict.keys()):
            print('{:5}: {:10}\t{}'.format(n, key, indict[key]))
            n += 1
        print(f'Numberof key-value pairs: {n}')

    @staticmethod
    def init_dict(input:dict, keys:list, default_val=None):
        '''
        arg: default_val = '', [], {}
        '''
        curr = input
        if isinstance(input, dict):
            for k in keys[:-1]:
                if k not in curr:
                    curr[k] = {}
                curr = curr[k]
            if keys[-1] not in curr:
                curr[keys[-1]] = default_val if \
                    default_val is not None else ''


    @staticmethod
    def update_dict(input:dict, key, val):
        if key not in ('', '-', None):
            if key not in input:
                input[key] = []
            else:
                if not isinstance(input[key], list):
                    input[key] = [input[key],]
            tmp = val if isinstance(val, list) else [val,]
            for t in tmp:
                if t not in input[key]:
                    input[key].append(t)
   
    @staticmethod
    def merge_dict(d1:dict, d2:dict)->dict:
        '''
        values of corresponding keys between d1 and d2
        should match to each other
        '''
        merged = deepcopy(d1)
        for k in d1:
            if k in d2:
                KeyValue.update_dict(merged, k, d2[k])
                del d2[k]
        if d2:
            merged.update(d2)
        return merged

    @staticmethod
    def get_deep_value(input:dict, keys:list):
        if not keys:
            return []
        val = []
        pool = [(keys, input),]
        while pool:
            curr_keys, curr_input = pool.pop(0)
            # print(curr_keys, curr_input)
            if isinstance(curr_input, dict):
                key = curr_keys[0]
                if key in curr_input:
                    if len(curr_keys) == 1:
                        tmp = []
                        if isinstance(curr_input[key], list):
                            tmp += curr_input[key]
                        else:
                            tmp = [curr_input[key]]
                        for t in tmp:
                            if t not in val and t not \
                                in (None, '', [], {}, '-'):
                                val.append(t)
                    else:
                        pool.append((curr_keys[1:], curr_input[key]))
            elif isinstance(curr_input, list):
                for item in curr_input:
                    pool.append((curr_keys, item))
        return val
    
    @staticmethod
    def switch_key_value(input:dict)->dict:
        '''
        switch key ~ value of a dictionary
        '''
        if not isinstance(input, dict):
            return None
        new = {}
        for key,val in input.items():
            for v in val if isinstance(val, list) else [val,]:
                if type(v) in (str, int, tuple):
                    KeyValue.update_dict(new, v, key)
        return new
