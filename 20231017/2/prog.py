from math import *
funcs = {}
funcs_with_1_param = set()
str_number = 0
while s := input():
    if s[0] == ':':
        func_name = s.split()[0][1:]
        params = s.split()[1:-1]
        if len(params) == 1:
            funcs_with_1_param.add(func_name)
        params_str = ','.join(params)
        func_str = f'lambda {params_str}:{s.split()[-1]}'
        funcs[func_name] = eval(func_str)
    elif s.split()[0] == 'quit':  
        expr = ' '.join(s.split()[1:]) + f'.format({len(funcs) + 1}, {str_number + 1})'
        print(eval(expr))
        break
    else:
        func_name, *params = s.split()
        if func_name in funcs_with_1_param:
            params = []
            params.append(s[s.find(' '):])
        params = (eval(param) for param in params)
        print(funcs[func_name](*params))   
    str_number += 1 
