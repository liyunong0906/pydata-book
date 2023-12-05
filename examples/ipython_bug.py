def works_fine():
    pass

def throws_an_exception():
    a = 5
    assert a == 4

def calling_things():
    works_fine()
    throws_an_exception()

calling_things()
