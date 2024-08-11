module division(input [0:7] maghsoom, input [0:7] maghsoom_elaih, output reg [0:7] kharej_ghesmat, output reg [0:7] baghimandeh);
	reg [0:7] number, counter;
	always@ (maghsoom or maghsoom_elaih) 
	begin
		if ( maghsoom_elaih<=8 && 1<=maghsoom_elaih) 
		begin 
			number = maghsoom;
			counter = 0;
			while ( number >= maghsoom_elaih) 
			begin
			 	number = number - maghsoom_elaih;
			 	counter = counter + 1;
			end
			kharej_ghesmat = counter;
			baghimandeh = number;
		end
		else
			$display("lotfan maghsoom_elaih daroon range(1 - 8) vared konid:)");
	end
endmodule
