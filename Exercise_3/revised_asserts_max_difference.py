# spec1
assert (len(pairs) == 0 and res == -1) or len(pairs) > 0

# spec2
if len(pairs) > 0:
    assert isinstance(res, (int, float))

# spec3
diffs = [abs(p[1] - p[0]) for p in pairs]; 
assert res == max(diffs)

# spec4
for (a, b) in pairs: 
    assert res >= abs(b - a)

# spec5
assert any(abs(b - a) == res for (a, b) in pairs)

