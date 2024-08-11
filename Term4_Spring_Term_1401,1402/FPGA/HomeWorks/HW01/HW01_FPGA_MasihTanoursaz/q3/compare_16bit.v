module compare_16bit (input [0:15]first, input [0:15]second, output x, output y, output z);	
	wire [0:3]x1,y1, z1;
	compare_4bit g1(first[0:3],second[0:3],x1[0],y1[0],z1[0]);
	compare_4bit g2(first[4:7],second[4:7],x1[1],y1[1],z1[1]);
	compare_4bit g3(first[8:11],second[8:11],x1[2],y1[2],z1[2]);
	compare_4bit g4(first[12:15],second[12:15],x1[3],y1[3],z1[3]);
	assign x = x1>y1;
	assign y = x1<y1;
	assign z = z1 == 4'b1111;

endmodule
