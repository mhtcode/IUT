module compare_4bit (input [0:3]first, input [0:3]second, output x, output y, output z);	
	assign x = first > second;
	assign y = first < second;
	assign z = first == second;
endmodule
