//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: Masih Tanoursaz
// 
// Create Date:    01:35:00 28/06/2023 
// Design Name: 
// Module Name:    xor 
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
module xor_gate(in1, in2, out);
	input in1, in2;
	output out;
	wire in1_bar, in2_bar, temp1, temp2;
	
	not_gate g1(in1, in1_bar); // not in1 -> in1_bar
	not_gate g2(in2, in2_bar); // not in2 -> in2_bar
	and_gate g3(in1, in2, temp1); // in1.in2 -> temp1
	and_gate g4(in1_bar, in2_bar, temp2); // in1_bar.in2_bar -> temp2
	nor res(out, temp1, temp2); // (temp1.temp2)' -> res
endmodule