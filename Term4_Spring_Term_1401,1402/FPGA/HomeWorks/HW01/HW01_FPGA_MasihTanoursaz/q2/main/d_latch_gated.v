module d_latch_gated(clk, D, Q, Qbar);
	input clk, D;
	output Q, Qbar;
	wire Dbar;
	not g1(Dbar, D);
	sr_latch_gated sr1(clk, D, Dbar, Q, Qbar);
endmodule
