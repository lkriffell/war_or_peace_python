from minitest import *

import operator

# declare a variable for test
tself = get_test_self()
# you could put all your test variables on tself
# just like declare your variables on setup.

tself.jc = "jc"
# declare a test
with test(object.must_equal):
    tself.jc.must_equal('jc')
    None.must_equal(None)

with test(object.must_true):
    True.must_true()
    False.must_true()

with test(object.must_false):
    True.must_false()
    False.must_false()

# using a funcation to test equal.
with test("object.must_equal_with_func"):
    (1).must_equal(1, key=operator.eq)
    (1).must_equal(2, key=operator.eq)

def div_zero():
    1/0

# test exception
with test("test must_raise"):
    (lambda : div_zero()).must_raise(ZeroDivisionError)
    (lambda : div_zero()).must_raise(ZeroDivisionError, "integer division or modulo by zero")
    (lambda : div_zero()).must_raise(ZeroDivisionError, "in")

# when assertion fails, it will show the failure_msg
with test("with failure_msg"):
    the_number = 10
    (the_number % 2).must_equal(1,
        failure_msg="{0} is the number".format(the_number))
    # it wont show the failure_msg
    (the_number % 2).must_equal(0,
        failure_msg="{0} is the number".format(the_number))

    (True).must_false(
        failure_msg="{0} is the number".format(the_number))

    (lambda : div_zero()).must_raise(ZeroDivisionError, "in",
        failure_msg="{0} is the number".format(the_number))

def print_msg_twice(msg):
    print msg
    print msg
    return msg

with test("capture_output"):
    with capture_output() as output:
        result = print_msg_twice("foobar")
    result.must_equal("foobar")
    output.must_equal(["foobar","foobar"])

with test("must output"):
    (lambda : print_msg_twice("foobar")).must_output(
            ["foobar","foobar"])
    (lambda : print_msg_twice("foobar")).must_output(
            ["foobar","wrong"])
