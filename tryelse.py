print "Try to try"
try:
    # try block
    # code that can through exception
    z = []
    b = 10/0
    # print z[1]
except ZeroDivisionError:
    print ZeroDivisionError

except TypeError:
    print TypeError

except Exception as e:
    print e
    print "Raised the wrong exception type"

else:
    # will only execute if exception is not raised and try block is properly executed
    # will always execute before finally
    # if exception is raised and caught then also this block will not execute
    # put here code that you want to execute if and only if exception is not there
    print "Didn't raise any exception"

finally:
    # will always execute
    # closing file or cleaning task can be done
    print "Finally block"

print "All done"
