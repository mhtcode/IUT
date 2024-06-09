module shiftReg_8bit(input clk, input load, input [0:7]data, input clear, input shift, input dir, output reg [0:7]out);
	integer index;
	always@(negedge clk)
	begin
		if(load == 1)
			out = data;
		else if(clear == 1)
			out = 0;
		else if(shift == 1)
		begin
			if (dir == 0)
				begin
					for(index = 0 ; index < 7 ; index = index + 1 )
							out[index] = out[index + 1];
					out[7] = 0;
				end
			else if (dir == 1)
				begin
					for(index = 7 ; index > 0 ; index = index - 1 )
							out[index] = out[index - 1];
					out[0] = 0;
				end
		end
	end
endmodule