# spec1
assert (len(pairs) == 0 and res is None) or len(pairs) > 0

# spec2
if len(pairs) > 0:
    assert isinstance(res, (int, float))

# spec3
if len(pairs) > 0:
    diffs = [(p[1] - p[0]) for p in pairs]
    assert res == max(diffs)

# spec4
if len(pairs) > 0:
    for (a, b) in pairs:
        assert res >= (b - a)

# spec5
if len(pairs) > 0:
    assert any((b - a) == res for (a, b) in pairs)
