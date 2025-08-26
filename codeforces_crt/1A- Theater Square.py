'''
In this question, we need to cover all the theater with the tiles(square granite flagstone)
but the conditions are
1. THE TILES WE NEED TO PUT PARALLEL
2. WE CAN NOT BREAK THE TILES
3. IT IS ALLOWED TO OVERHANG THE TILES OUTSIDE OF THE SQUARE
4. ALL THE ENTIRE AREA SHOULD MUST BE COVER
'''

import math
n, m, c = map(int, input().split())

n = math.ceil(n / c)  # THIS WILL GIVE THE FULL SIZE OF THE FLAGSTONE TO BE COVER THE AREA COMPLETELY
m = math.ceil(m / c)

print(n * m)

