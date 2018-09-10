def sum_1k(m):
    s = 0
    for i in range(1, m):
        s += 1 / i
    return s


def test_sum_1k():
    s_3 = sum_1k(3)
    success = s_3 - 1.5 < 1e-10
    msg = 'Error!'
    assert success, msg


test_sum_1k()