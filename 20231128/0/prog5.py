import readline  #можно редактировать ввод и производить поиск по истории как в терминале, достаточно этого импорта
while s:=input('> '):
    match s.split():
        case ['mov', r1, r2]:
            print(f'moving {r2} to {r1}')
        case ['push' | 'pop' as cmd, *reglist]:
            x = ' '.join(reglist)
            print(f'{cmd}ing {x}')
        case [cmd, r1]:
            print(f'making {cmd} with {r1}')
        case _:
            print('Parse error!')