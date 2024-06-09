module sr_latch_gated(clk, S, R, Q, Qbar);
	input  clk, S, R;
	output Q, Qbar; 
	
	wire nand1_out; // output of nand1 
	wire nand2_out; // output of nand2


	nand g1(nand1_out,clk,S); 
	nand g2(nand2_out,clk,R); 
	nand g3(Q,nand1_out,Qbar);
	nand g4(Qbar,nand2_out,Q);

endmodule
