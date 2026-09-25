"""rgb"""
r1, g1, b1 = map(int, input().split())
r2, g2 ,b2 = map(int, input().split())

def mix(c1, c2):
    """mix"""
    return (c1 + c2) // 2

rMix = mix(r1, r2)
gMix = mix(g1, g2)
bMix = mix(b1, b2)

print(rMix, gMix, bMix)
