module xor_test;
	reg a, b;
	wire res;
	xor_gate g1(a, b, res);

	initial
	begin
	#100 {a, b} = 2'b00;
	#100 {a, b} = 2'b01;
	#100 {a, b} = 2'b10;
	#100 {a, b} = 2'b11;
	#100;
	end
endmodule
