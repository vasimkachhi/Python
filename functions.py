def f(a, b):
    con = 1
    con2 = 2
    a = a
    b = b
    c = a + b
    print c/con
f(10, 20)

print f.func_code
c = f.func_code
print c.co_consts
print f.func_code.co_varnames
print f.func_code.co_argcount
print f.func_closure
print f.func_dict
print f.func_doc
print f.func_name