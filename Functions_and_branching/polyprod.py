def poly(roots, x):
    p = 1
    for i in range(len(roots)):
        p *= (x - roots[i])
    return p


roots = [-1, 1, 2]

print(poly(roots, 3))
success = poly(roots, 3) == 8
msg = 'Wrong!'
assert success, msg
