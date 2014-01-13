1;


yes = "y";
no = "n";
 

function rint = rand_int(limit)
  % returns a random int in the range 1-limit
  % one-indexed for general octave compatibility

  rint = ceil(rand(1,1) * limit);
endfunction

function A = rand_int_mat(m, n)
  % returns an mXn array of random ints
  
  A = rand (m,n);
  A *= 10;
  A = ceil(A);
endfunction
  
function B = mcompatible_mat(A)
  % returns an array B such that A X B is a legitimate multiplication
  B = rand_int_mat(size(A, 2), rand_int(5));
endfunction

function B = acompatible_mat(A)
  % returns an array B such that A + B is a legitimate addition
  B = rand_int_mat(size(A,1), size(A, 2));
endfunction

function A = any_int_mat(max_d = 5)
  % returns an mXn int array, with m and n <= max_d
  m =   rand_int(max_d);
  n =   rand_int(max_d);
  A = rand_int_mat(m,n);
endfunction

function eqs = display_alpha_y_as_eq(alpha,y)
  % given a system of equations defined by a matrix
  % alpha and a column vector y, displays a multi-line string
  % displaying the corresponding system of equations

  if ( 
      (size(alpha, 1) != size (y,1)) |
      (size(y, 2) != 1) 
      )
    printf ("There was a dimensionality problem. \n");
  else
    for i = 1:size(alpha, 1)
      for j = 1: (size(alpha, 2)-1)
	printf("(%d * X_%d) + ", alpha(i,j), j);
      endfor
      printf ("(%d * X_%d) = %d\n", alpha(i,(j+1)), j+1, y(i));
    endfor
  endif
endfunction