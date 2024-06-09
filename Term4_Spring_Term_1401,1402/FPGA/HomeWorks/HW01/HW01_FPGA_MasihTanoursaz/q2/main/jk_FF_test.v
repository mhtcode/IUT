module jk_FF_test;
	reg j, k, clk;
	wire q, qbar;

	jk_FF g1(clk, j, k, q, qbar);
	/*initial
	begin
	#100 {j, k, clk} = 3'b000;
	#100 {j, k, clk} = 3'b001;
	#100 {j, k, clk} = 3'b010;
	#100 {j, k, clk} = 3'b011;
	#100 {j, k, clk} = 3'b100;
	#100 {j, k, clk} = 3'b101;
	#100 {j, k, clk} = 3'b110;
	#100 {j, k, clk} = 3'b111;
	#100;
	#100;
	end*/
	//4. apply test vectors
initial begin
  clk=0;
     forever #10 clk = ~clk;  
end 
initial begin 
j= 1; k= 0;
 #100; j= 0; k= 1; 
 #100; j= 0; k= 0; 
 #100; j= 1; k=1; 
end 


endmodule
