module st_latch_test;
	reg clk , s, r;
wire q, qbar;
	sr_latch_gated g1(clk, s, r, q, qbar);
	initial
	begin
	#100 {s, r ,clk} = 3'b000;
	#100 {s, r ,clk} = 3'b001;
	#100 {s, r ,clk} = 3'b010;
	#100 {s, r ,clk} = 3'b011;
	#100 {s, r ,clk} = 3'b100;
	#100 {s, r ,clk} = 3'b101;
	#100 {s, r ,clk} = 3'b110;
	#100 {s, r ,clk} = 3'b111;
	#100;
	end




endmodule
