def f():
    y = "Vasim"
    print "My name is " +str(y)
f()

# change function code dynamically
new_code_text ="""y = "Vasim Kachhi"
print "My Full name is " + str(y)
print z"""
f.func_code =compile(new_code_text, __name__,'exec')
f()

# change function code dynamically
new_code_text ="""y = "Vasim Ahamed Kachhi"
print "My Full name is " + str(y) """
f.func_code =compile(new_code_text,'<string>','exec')
f()
