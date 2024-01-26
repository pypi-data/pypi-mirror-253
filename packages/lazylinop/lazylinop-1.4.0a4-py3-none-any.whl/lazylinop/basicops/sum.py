from lazylinop import LazyLinearOp

def sum(*lops, mt=False, af=False):
    """
    Sums (lazily) all linear operators in lops.

    Args:
        lops:
             the objects to add up as a list of LazyLinearOp-s or other compatible linear operator.
        mt:
             True to active the multithread experimental mode (not advisable, so far it's not faster than sequential execution).
        af:
             this argument defines how to compute L @ M = sum(lops) @ M, with M a numpy array. If True, the function adds the lops[i] into s before computing s @ M. Otherwise, by default, each lops[i] @ M are computed and then summed.

    Returns:
        The LazyLinearOp for the sum of lops.

    Example:
        >>> import numpy as np
        >>> from lazylinop import sum, aslazylinearoperator
        >>> from pyfaust import dft, Faust
        >>> from scipy.sparse import diags
        >>> nt = 10
        >>> d = 64
        >>> v = np.random.rand(d)
        >>> terms = [dft(d) @ Faust(diags(v, format='csr')) @ dft(d) for _ in range(nt)]
        >>> ls = sum(*terms) # ls is the LazyLinearOp sum of terms
    """
    lAx = lambda A, x: A @ x
    lAHx = lambda A, x: A.T.conj() @ x
    for l in lops[1:]:
        if l.shape != lops[0].shape:
            raise ValueError('Dimensions must agree')
    def matmat(x, lmul):
        if af:
            S = lops[0]
            for T in lops[1:]:
                S = S + T
            return S @ x
        from threading import Thread
        from multiprocessing import cpu_count
        Ps = [None for _ in range(len(lops))]
        n = len(lops)
        class Mul(Thread):
            def __init__(self, As, x, out, i):
                self.As = As
                self.x = x
                self.out = out
                self.i = i
                super(Mul, self).__init__(target=self.run)

            def run(self):
                for i, A in enumerate(self.As):
                    self.out[self.i + i] = lmul(A, self.x)

        if mt:
            ths = []
            nths = min(cpu_count(), n)
            share = n // nths
            #print("nths:", nths, "share:", share)
            rem = n - share * nths
            for i in range(nths):
                start = i*share
                if i == nths - 1:
                    end = n
                else:
                    end = (i+1) * share
                #print("i:", i, "start:", start, "end:", end)
                ths += [Mul(lops[start:end], x, Ps, start)]
                ths[-1].start()
            for i in range(nths):
                ths[i].join()
        else:
            for i, A in enumerate(lops):
                Ps[i] = lmul(A, x)
        S = Ps[-1]
        for i in range(n-2, -1, -1):
            S = S + Ps[i]
        return S
    return LazyLinearOp(lops[0].shape, matmat=lambda x: matmat(x, lAx),
                              rmatmat=lambda x: matmat(x, lAHx))

