

def add(*lists):
    output = []
    for item in lists:
        if not isinstance(item, list):
            raise TypeError('required input is lists')
        output