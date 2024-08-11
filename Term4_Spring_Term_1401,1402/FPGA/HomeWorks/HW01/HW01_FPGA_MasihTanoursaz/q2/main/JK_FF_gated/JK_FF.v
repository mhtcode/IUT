module JK_FF(clk, j , k , q , qbar);
	input j , k;
	input clk;
	output q , qbar;
	wire nand1 , nand2 ;
	
	nand g1(nand2 , k , q , clk) ;
	nand g2(nand1 , j , qbar , clk) ;
	nand g3(q , nand1 , qbar) ;
	nand g4(qbar , nand2 , q ) ;
endmodule
