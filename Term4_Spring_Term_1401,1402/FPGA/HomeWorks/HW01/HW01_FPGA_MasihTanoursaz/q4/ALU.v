module ALU (input [1:0]select, input [4:0]a, input [4:0]b, output reg [5:0]out);
	always@(select or a or b)
	begin
		case (select)
			0 : out = a;
			1 : out = a + b;
			2 : out = a - b;
			3 : out = a + 1;
		endcase
	end
	
endmodule