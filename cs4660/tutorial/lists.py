"""Lists defines simple list related operations"""

def get_first_item(li):
    return li[0]


def get_last_item(li):
    return li[-1]


def get_second_and_third_items(li):
    return li[1:3]

def get_sum(li):
    a = sum(li)
    return a


def get_avg(li):
    x = sum(li)
    avg = x/len(li)
    return avg