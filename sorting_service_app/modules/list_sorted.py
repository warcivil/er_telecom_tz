def quicksort(data):
    array = data.get('array')
    reverse = data.get('reverse', True)
    return sorted(array, reverse=reverse)