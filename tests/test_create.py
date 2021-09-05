import subprocess 

def test_create_object():
    output = subprocess.check_output(['unrival', 'create'])
    print(output)
    assert False
