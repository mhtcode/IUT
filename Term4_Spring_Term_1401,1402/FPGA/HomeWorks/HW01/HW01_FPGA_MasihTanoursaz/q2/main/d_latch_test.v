module d_latch_test;
	reg d, clk;
	wire q, qbar;
	d_latch_gated g1(clk, d, q, qbar);
	initial
	begin
	#100 {clk, d} = 2'b00;
	#100 {clk, d} = 2'b01;
	#100 {clk, d} = 2'b10;
	#100 {clk, d} = 2'b11;
	#100;
	end
endmodule
