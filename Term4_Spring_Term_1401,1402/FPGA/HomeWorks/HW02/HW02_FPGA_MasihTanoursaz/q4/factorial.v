module factorial (
    input [3:0] number,
    output reg [24:0] result
);
  integer i, temp;  // uses in factorial_function
  always @(number) result = factorial_func(number);

  function [24:0] factorial_func;
    input [3:0] arg0;
    begin
      temp = 1;

      for (i = 1; i <= arg0; i = i + 1) temp = temp * i;


      factorial_func = temp;
    end
  endfunction
endmodule
