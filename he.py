# https://en.xen.wiki/w/Harmonic_Entropy

import numpy as np
from scipy.special import gamma

def calcDyadHE(c):
    js = rationals()
    return shannonEntropy(js, c)

def shannonEntropy(js, c):
    s = 0
    for j in js:
        a = p(j, c, js)
        s -= a * np.log1p(a)
    return s

def p(j, c, js):
    s = 0
    for ji in js:
        s += q(ji, c)
    return q(j, c) / s

def q(j, c):
    jn = j[0]
    jd = j[1]
    return s(jn / jd, c) / h(jn, jd)

def h(jn, jd, t="Weil"):
    if t == "Tenney":
        return np.sqrt(jn * jd)
    elif t == "Weil":
        return max(jn, jd)

def s(x, c):
    return ggd(frac2cent(x), c, 17*1.414, 2)

def frac2cent(x):
    return 1200 * np.log2(x)

def ggd(x, mu, alpha, beta): 
    return beta / (2 * alpha * gamma(1/beta)) * np.exp(-np.power(np.abs(x - mu)/alpha, beta))


def rationals(o=50, interval=(0,3)):
    rs = []
    for i in range(interval[0], interval[1]):
        rs.extend(farey(o, i))
    rs.pop(0) # remove 0/1
    print(rs)
    return rs


def farey(n, k):
    if n == 1:
        return [(k,1), (k+1,1)]
    else:
        return deepen(farey(n-1, k) , n)

def deepen(arr, k):
    n = len(arr)
    for i in range(n - 1): 
        l = arr[n - i - 2]
        r = arr[n - i - 1]
        num = l[0] + r[0]
        denom = l[1] + r[1]
        if(denom < k + 1):
            arr.insert(n - i - 1, (num, denom))
    return arr

