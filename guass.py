def S(seq, i=0):
    if len(seq) == i : return 0
    return seq[i]+S(seq,i+1)

def T(seq, i=0):
    if len(seq) == i : return 1
    return 1+T(seq,i+1)
