first, second, third = input().split()

match input().split():
    case [*s] if s[0] == first and 'yes' in s:
        print('first case')
    case [*s] if s[0] == second:
        print('second case')
    case [*s] if s[0] == third and s[-1] == second:
        print('third case')