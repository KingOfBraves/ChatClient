def test_wrapper(function):
    def wrapper(*args, **kwargs):
        print "Testing: " + function.__name__
        function(*args, **kwargs)
    return wrapper
