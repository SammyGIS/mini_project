def myfunction(*args, **kwargs):
    print(args[0])
    print(args[0])
    print(args[0])
    print(args[0])
    print(args[0])
    print(kwargs['KEYONE'])
    print(kwargs['KEYTWO'])
myfunction('hey',True,38,'wow',
           'KEYONE'=1, 'KEYTWO'=3)