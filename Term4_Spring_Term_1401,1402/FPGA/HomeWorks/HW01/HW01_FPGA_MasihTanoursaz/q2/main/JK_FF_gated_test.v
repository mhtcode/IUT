module JK_FF_gated_test;
	reg j = 0 , k = 0, clk = 1;
	wire q , qbar;
	JK_FF_gated g1(clk, j , k , q , qbar );
	initial
	begin
  		#100 {k , j , clk} = 3'b101;
		#100 {j, k , clk} = 4;
		#100 {j, k , clk} = 5;
		#100 {j, k , clk} = 2;
		#100 {j, k , clk} = 3;
		#100 {j, k , clk} = 0;
		#100 {j, k , clk} = 1;
		#100 ;
	end
endmodule
