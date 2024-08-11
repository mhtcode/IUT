module jk_FF(clk, J, K, Q, Qbar);
	input clk, J, K;
	output Q, Qbar;

	wire a, b, c, Kbar;
	not g1(Kbar, K);
	and g2(a, Kbar, Q);
	and g3(b, J, Qbar);
	or g4(c, a, b); // D = JQ'+K'Q
	d_latch_gated res(clk, c, Q, Qbar);
endmodule
