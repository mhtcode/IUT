//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: Masih Tanoursaz
// 
// Create Date:    01:12:00 28/06/2023 
// Design Name: 
// Module Name:    not 
// Project Name: 
// Target Devices: 
// Tool versions: 
// Description: 
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////
module not_gate(in, out);
	input in;
	output out;
	reg temp = 1'b0;
	nor g1_not(out, in, temp);
endmodule
