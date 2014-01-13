class Matrix:
    '''A matrix, with standard operations
    We use logical AND and OR to represent elementwise multiplication and addition (.* and .+) 
    since we need operators for these, and those make sense'''
    def __init__(self, m,n, vals):
        self.vals = vals
        self.n = n
        self.m = m
        self.transposed = False

    def row(self, y):
        '''Retrieve a row of the matrix. Currently returned as a simple list. Should be a Vector.'''
        return self.vals[self.n*y: self.n*(y+1)]
    def rows(self):
        '''Retrieve the rows of the matrix. Currently returned as a list of lists. Should be a list of Vectors'''
        return [self.row(j) for j in range(self.m)]
    def col(self, x):
        '''Returns a column of the matrix. Currently returns a simple list. Should be a Vector.'''
        return [self.row(y)[x]  for y in range(self.m)]
    def cols(self):
        '''Returns the columns of this matrix. Currently returns a list of elements. Shoud be a Vector.'''
        return [self.col(i) for i in range(self.n)]
    def set_row(self, y, row):
        '''Sets one row of this matrix to the proffered value. 
        To do: dimension checking, work on vectors instead of simple lists.'''
        self.vals[self.n*y: self.n*(y+1)] = row
    def set_col(self, x, col):
        '''Sets one column of this matrix to the proffered value. 
        To do: dimension checking, accept vectors instead of lists.'''
        for j in range(self.m):
            self.vals[j*self.n +x] = col[j]

    def elem(self,row,col):
        '''Get a single element by index'''        
        return self.vals[row*self.m +col]

    def set(self,x,y, value):
        '''Set a single element at (x,y) to a value. 
        To do: dimension checking'''
        self.vals[y*self.n +x] = value
    def add_row(self, i, new_row):
        '''add a row BEFORE i - ie, if i = 0 then we insert a first row. If self has n rows, 
        then adding at n will add a last row. '''
        self.vals = self.vals[:i*self.n] + new_row + self.vals[i*self.n:]
        self.m +=1
    def add_col(self, j, new_col):
        '''same as add_col: adds before j'''
        self.n +=1
        for i in range(self.m):
            self.vals.insert(i*self.n + j, new_col[i])
    def additively_conformable(self, m2):
        '''Returns True iff m1 + m2 is a legitimate operation'''
        return self.n == m2.n and self.m == m2.m
    def multi_conformable (self, m2):
        '''Returns True iff m1 * m2 is a legitimate operation'''
        return self.n == m2.m
    
    ### Propositions ###

    def triangular(self):
        ''' Returns true if this matrix is either upper- or lower-
        triangular'''
        return self.upper_triangular() or self.lower_triangular()

    def upper_triangular(self, strict = False):
        '''Returns true if all non-zero elements in this matrix are on
        or above the major diagonal. If "strict" is True, returns True if matrix is
        strictly upper: all non-zero elements are strictly above the diagonal'''
        if strict:
            vals = [val for (key, val) in enumerate(self.vals) if key % self.n <= key / self.m] 
        else:
            vals = [val for (key, val) in enumerate(self.vals) if key % self.n < key / self.m] 
        return all ([v == 0 for v in vals])
                
    def lower_triangular(self, strict = False):
        '''Returns true if all non-zero elements in this matrix are on
        or below the major diagonal. If "strict" is True, returns true if matrix is
        strictly lower: all non-zero elements are strictly below the major diagonal.'''
        if strict:
            vals = [val for (key, val) in enumerate(self.vals) if key % self.n >= key / self.m] 
        else:
            vals = [val for (key, val) in enumerate(self.vals) if key % self.n > key / self.m] 
        return all ([v == 0 for v in vals])


    ### Standard matrix operations ###
    def matrix_multiply(self, other):
        '''Multiply this matrix by other. Naive algorithm to start with. 
        '''
        if not self.multi_conformable(other):
            return None
        mat = zero(self.m, other.n)
        for i in range(mat.m):
            for j in range(mat.n):
                mat.set(i,j, sum([u * v for (u,v) in zip(self.row(i), other.col(j))]))
        return mat


    ####  dunder methods ###
    def __repr__(self):
        '''Just emit the rows for a representation.'''
        return "\n".join(["\t".join([str(i) for i in row]) for row in self.rows()])


    def __add__(self, m2):
        return add(self, m2)

    def __sub__(self, m2):
        '''Defined as self + negated m2. In case you're using a weird 
        field where p -q != p + -q. In which case, why?'''
        return add(self, -m2);

    def __neg__(self):
        '''Negate all elements in the matrix'''
        return Matrix(self.m, self.n, [-v for v in self.vals])

    def __mul__(self, other):
        return self.matrix_multiply(other)

    def __rmul__(self, alpha):
        # hope alpha is a scalar
        # something more effective than hope is wanted here
        return scalar_mult(self, alpha)

    def __pow__(self, x):
        '''Not implemented yet'''
        return None

    def __or__(self, other):
        
        if not self.additively_conformable( other):
            return None
        return [v1 + v2 for (v1, v2) in zip(self.vals, other.vals)]
    def __and__(self, other):
        '''We use & for element-wise multiplication, since we don't have a 
        way to use .* and logical and makes sense in at least one case. (consider 
        filtering against a binary matrix)'''
        if not self.additively_conformable( other):
            return None
        return [v1 * v2 for (v1, v2) in zip(self.vals, other.vals)]

    def __eq__(self, other):
        '''Matrices are equal iff their dimensions are the same and all of
        their elements are equal'''
        return all ([self.m == other.m, 
                     self.n == other.n,  
                     all(v1 == v2 for (v1, v2) in zip (self.vals, other.vals))])

    def __getitem__(self, xy):
        x,y = xy
        return self.elem(x, y)

        

def mat_from_grid(grid):
    grid = grid.strip()
    grid = grid.split("\n")
    m = len(grid)
    grid = [row.split() for row in grid]
    n = len(grid[0])
    vals = []
    for row in grid:
        vals.extend([int (i) for i in row])
    return Matrix(m,n,vals)

def add(m1, m2):
    '''Return the result of adding m1 and m2. Throw an exception if the matrices are not 
    additively conformable.'''
    if not m1.additively_conformable(m2):
        print "I'd better throw an exception here"
        return None
    return Matrix(m1.m, m1.n, [v1+v2 for (v1, v2) in zip(m1.vals, m2.vals)])

def scalar_mult(m1, alpha):
    return Matrix(m1.m, m1.n, [v * alpha for v in m1.vals])

    
        ### Special Matrices ###
def zero(x = 1, y = None):
    '''returns a zero matrix of dimensions x, y. Assumes square matrix if y not specified.'''
    if y == None:
        y = x
    return Matrix(x,y, x* y * [0])

def ones(x = 1, y =None):
    '''returns an xy Matrix whose elements are all equal to 1'''
    if y == None:
        y = x
    return Matrix(x,y, x*y*[1])

def identity(x = 1, y = None):
    '''Returns the identity matrix of size x,y. If no y specified, assumes a 
    square matrix is desired'''
    if y == None:
        y = x
    m = zero(x,y)
    for i in range(min(x,y)):
        m.set(i,i, 1)
    return m


def mirror(x = 1, y = None):
    '''Returns a matrix with ones on the minor diagonal. 
    This matrix reflects left-to-right or top-to-bottom, depending
    on whether it is multiplied from the left or right.'''
    if y== None:
        y = x
    m = zero(x,y)
    for i in range(min(x,y-1)):
        m.set(i, y-1, 1)
    return m

m1 = mat_from_grid("1 2")
m2 = mat_from_grid("3\n4")
m3 = mat_from_grid("0 1 1 1\n 0 0 1 1 \n 0 0 0 1\n 0 0 0 0");
m4 = mat_from_grid("0 0 0 0\n 1 0 0 0 \n 1 1 0 0\n 1 1 1 0");


