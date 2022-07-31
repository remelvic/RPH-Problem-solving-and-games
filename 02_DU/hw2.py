class MyVector:
 
    def __init__(self, vector_one):
        self.vector = vector_one
 
    def get_vector(self):
        return self.vector
 
    def __mul__(self, other):
        return sum(a * b for a, b in zip(self.get_vector(), other.get_vector()))
 
 
if __name__ == "__main__":
    vec1 = MyVector([1, 2, 3, 7, 8, 9])
    vec2 = MyVector([3, 4, 5, 13, 20, 30])
    print(vec1.get_vector())
    dot_product = vec1 * vec2  # 1 * 3 + 2 * 4 + 3 * 5 ... + 9 * 30 = 547
    print(dot_product)
