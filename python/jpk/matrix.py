class Matrix:
    '''A matrix, with standard operations'''
    def __init__(self, m,n, vals):
        self.vals = vals
        self.n = n
        self.m = m
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
    def elem(self,x,y):
        '''Get a single element by index'''
        return self.vals[y*self.n +x]
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
    def __repr__(self):
        '''Just emit the rows for a representation.'''
        return "\n".join(["\t".join([str(i) for i in row]) for row in self.rows()])
    def additively_conformable(self, m2):
        '''Returns True iff m1 + m2 is a legitimate operation'''
        return self.n == m2.n and self.m == m2.m
    def multi_conformable (self, m2):
        '''Returns True iff m1 * m2 is a legitimate operation'''
        return self.n == m2.m
    

    ####  dunder methods ###
    def __add__(self, m2):
        return add(self, m2)

    def __sub__(self, m2):
        return add(self, -m2);

    def __neg__(self):
        return Matrix(self.m, self.n, [-v for v in self.vals])
    def __rmul__(self, alpha):
        # hope alpha is a scalar
        # something more effective than hope is wanted here

        return scalar_mult(self, alpha)

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



m1 = mat_from_grid("1 2")
m2 = mat_from_grid("3\n4")



