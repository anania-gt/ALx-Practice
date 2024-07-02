class A:
    def __init__(self):
        print("A's init")

class B(A):
    def __init__(self):
        super().__init__()
        print("B's init")

class C(A):
    def __init__(self):
        super().__init__()
        print("C's init")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D's init")

# Usage
d = D()  # Output: A's init, C's init, B's init, D's init
