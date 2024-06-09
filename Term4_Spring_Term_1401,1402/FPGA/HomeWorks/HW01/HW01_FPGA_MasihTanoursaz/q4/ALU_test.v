module ALU_test;
	reg [0:1] select;
	reg [0:4] a;
	reg [0:4]b;
	wire [0:5] res;
	ALU g1(select ,a ,b ,res);

	initial 
	begin
		a = 10;
		b = 7;
		select = 0;
		#100 $display("select(binary) is: %b & result is: %d", select, res);
		select = 1;
		#100 $display("select(binary) is: %b & result is: %d", select, res);
		select = 2;
		#100 $display("select(binary) is: %b & result is: %d", select, res);
		select = 3;
		#100 $display("select(binary) is: %b & result is: %d", select, res);
	end
endmodule
