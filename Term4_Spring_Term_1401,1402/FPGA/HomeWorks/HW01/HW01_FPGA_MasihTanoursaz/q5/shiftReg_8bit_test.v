module shiftReg_8bit_test;
reg clk, load, clear, shift, dir;
reg [0:7]data;
wire [0:7]out;
shiftReg_8bit SR(clk, load, data, clear, shift, dir, out);

initial
begin
assign clk = 1'b1;
$monitor("out is: %b & load is: %b & clear is: %b & shift is: %b", out, load, clear, shift);
#100;
assign clk = 1'b0;
assign clear = 1'b0;
assign shift = 1'b0;
assign dir = 1'b0;
assign load = 1'b1;
$display("now load is: 1");
assign data = 8'b11111111;
#100 $display("\n");
assign clk = 1'b1;
#100 $display("\n");
assign clk = 1'b0;
assign clear = 1'b1;
$display("now clear is: 1");
assign load = 1'b0;
#100 $display("\n");
assign clk = 1'b1;
#100 $display("\n");
assign clk = 1'b0;
assign clear = 1'b0;
assign load = 1'b1;
$display("now load is: 1");
assign data = 8'b11001100;
#100 $display("\n");
assign clk = 1'b1;
#100 $display("\n");
assign  clk = 1'b0;
assign load = 1'b0;
assign shift = 1'b1;
$display("now shift is: 1 & dir is: 0");
#100 $display("\n");
assign clk = 1'b1;
#100 $display("\n");
assign  clk = 1'b0;
assign dir = 1'b1;
$display("now shift is: 1 & dir is: 1");
#100 $display("\n");
assign clk = 1'b1;
#100 $display("\n");
assign clk = 1'b0;
assign clear = 1'b1;
$display("now clear is: 1");
assign shift = 1'b0;
end
endmodule
