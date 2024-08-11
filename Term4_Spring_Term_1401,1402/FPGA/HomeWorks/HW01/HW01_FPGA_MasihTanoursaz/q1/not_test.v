module not_test;
	reg a;
	wire res;
	not_gate g1(a, res);
	initial
	begin
	#100 a=1'b0;
	#100 a=1'b1;
	#100;
	end

endmodule
