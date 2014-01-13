misc_funcs;  % load some useful functions
   
function cont = prob1 ()
  cont = 1;
  m = rand_int(5);
  n = rand_int(5);
  A = rand_int_mat (m,n);
  eq = mod(rand_int(2), 2);
  if eq
    B = A;
  else
    B = rand_int_mat (m,n);
  endif
  printf("Let A = \n"); disp (A);
  printf("and let B = \n"); disp (B);

  yn = input ("Are they equal? (y/n) ", "s");
  
  if yn == "y"
    yn = 1;
  elseif yn == "n"
    yn =0;
  endif;
  if yn == all((A == B))
    printf ("Correct \n");
  else 
    printf("Incorrect \n");
  endif;
endfunction;

function cont = prob2()
  % test knowledge of additive compatibility
  cont = 1;
  a_dims = [rand_int(5), rand_int(5)];
  A = rand_int_mat(a_dims(1), a_dims(2));
  foo = rand_int(3);
  if foo == 1
    B = mcompatible_mat(A);
  elseif foo == 2 
    B = acompatible_mat(A);
  else
    B = any_int_mat();
  endif;
  printf ("Let A = \n"); disp( A );
  printf ("and let B = \n");  disp ( B );
  yn = input("Is A + B a valid addition? (y/n) ", "s");
  if yn == "y"
    yn = 1;
  elseif yn == "n"
    yn = 0;
  endif
  if yn == (size(A)==size(B))
    printf("Correct!\n");
  else
    printf("Incorrect. A has size (%d, %d) and B has size (%d, %d). \n",
	   size(A, 1), size(A, 2), size(B, 1), size (B, 2));
    if size(A) == size(B)
      printf("The sum A + B is the %d X %d matrix \n",
	     size(A,1), size(A,2));
      disp(A + B);
      endif;
  endif;

endfunction

function cont = prob3()
  % test knowledge of multiplicative compatibility

  cont = 1;
  a_dims = [rand_int(5), rand_int(5)];
  A = rand_int_mat(a_dims(1), a_dims(2));
  foo = rand_int(3);
  if foo == 1
    B = mcompatible_mat(A);
  elseif foo == 2 
    B = acompatible_mat(A);
  else
    B = any_int_mat();
  endif;
  printf ("Let A = \n"); disp( A );
  printf ("and let B = \n");  disp ( B );
  yn = input("Is A X B a valid multiplication? (y/n) ", "s");
  if yn == "y"
    yn = 1;
  elseif yn == "n"
    yn = 0;
  endif
  if yn == (size(A,2)==size(B,1))
    printf("Correct!\n");
  else
    printf("Incorrect. A has %d columns and B has %d rows \n",
	   size(A,2), size(B, 1));
    printf("The product A X B is the %d X %d matrix \n",
	   size(A,1), size(B,2));
    disp(A * B);
  endif;
endfunction

function cont = prob4()
  % Matrix addition
  cont = 1;
  correct = 0;
  A = any_int_mat();
  B = acompatible_mat(A);
  row_num = rand_int(size(A,1));
  printf("Let A = \n"); disp(A);
  printf("and let B = \n"); disp(B);
  printf("A and B are additively compatible.\nEnter row %d ", row_num);
  printf("of the sum A + B, as a row vector [a b c ...]\n");
  printf("(remember that matrices are 1-indexed; there is no zero row)\n");
  correct_answer = (A + B)(row_num, :);
  answer = input ("Your answer: ");
  if size(correct_answer) == size(answer)
    if correct_answer == answer
      correct = 1
    endif
  endif
  if correct
    printf("Correct!\n");
  else
    printf("Incorrect. The correct answer is\n");
    disp (correct_answer);
  endif
endfunction

function cont = prob5()
  % Matrix multiplication
  cont = 1;
  correct = 0;
  A = any_int_mat();
  B = mcompatible_mat(A);
  row_num = rand_int(size(A,1));
  printf("Let A = \n"); disp(A);
  printf("and let B = \n"); disp(B);
  printf("A and B are multiplicatively compatible.\nEnter row %d ", row_num);
  printf("of the product A * B, as a row vector [a b c ...]\n");
  printf("(remember that matrices are 1-indexed; there is no zero row)\n");
  correct_answer = (A * B)(row_num, :);
  answer = input ("Your answer: ");
  if size(correct_answer) == size(answer)
    if correct_answer == answer
      correct = 1
    endif
  endif
  if correct
    printf("Correct!\n");
  else
    printf("Incorrect. The correct answer is\n");
    disp (correct_answer);
  endif
endfunction


function cont = prob6()
  % Matrix multiplication as linear combination
  cont = 1;
  correct = 0;
  A = any_int_mat();
  B = mcompatible_mat(A);
  row_num = rand_int(size(A,1));
  printf("Let A = \n"); disp(A);
  printf("and let B = \n"); disp(B);
  printf("Row i of a product matrix AB can be expressed as the vector of\n");
  printf("the sums A(i,j), ");
  printf("(remember that matrices are 1-indexed; there is no zero row)\n");
  correct_answer = (A * B)(row_num, :);
  answer = input ("Your answer: ");
  if size(correct_answer) == size(answer)
    if correct_answer == answer
      correct = 1
    endif
  endif
  if correct
    printf("Correct!\n");
  else
    printf("Incorrect. The correct answer is\n");
    disp (correct_answer);
  endif
  

endfunction

function cont = prob7()
  % Conversion of system of equations to matrix form
  
  cont = 1;
  alpha = any_int_mat(4);
  y = rand_int_mat(size(alpha,1), 1);
  printf("Consider the following system of equations: \n");
  display_alpha_y_as_eq(alpha, y);
  if rand_int(2) == 1
    printf("Enter the matrix corresponding to the coefficients α\n");
    printf("(enter matrices as [ a b c ; d e f ; ...])\n");
    correct_solution= alpha;
  else
    printf("Enter the vector corresponding to the solution y\n");
    printf("Remember that y is a column vector... \n");    
    correct_solution = y;
  endif;
  correct = 0;
  answer = input("Your answer: ");
  if (size(answer) == size(correct_solution))
    if (answer == correct_solution)
      correct = 1;
    endif;
  endif;
  if correct
    printf("Correct!\n");
  else
    printf("Sorry, incorrect\nThe correct solution is:\n");
    disp(correct_solution);
  endif
endfunction

function cont = zexit()
  cont = 0;
endfunction;

probs = ["prob1";"prob2";
	 "prob3";"prob4"; 
	 "prob5";"prob7";
	 "zexit"];

probs = cellstr(probs);

cont = 1;
while cont
  p1 = menu ("Exercises 1: Matrix Operations", 
	     "Matrix Equality", 
	     "Additive Compatibility", 
	     "Multiplicative Compatibility",
	     "Matrix Addition",
	     "Matrix Multiplication", 
	     "Equation to Matrix",
	     "Exit"
	     );
  cont = feval(probs{p1});
endwhile



