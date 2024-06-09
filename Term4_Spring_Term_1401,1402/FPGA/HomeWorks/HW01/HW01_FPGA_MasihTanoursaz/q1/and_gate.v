//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: Masih Tanoursaz
// 
// Create Date:    01:20:00 28/06/2023 
// Design Name: 
// Module Name:    and 
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


module and_gate(in1, in2, out);
	input in1, in2;
	output out;
	
	wire in1_bar, in2_bar;
	not_gate g1(in1, in1_bar);
	not_gate g2(in2, in2_bar);
	nor res(out, in1_bar, in2_bar);
endmodule