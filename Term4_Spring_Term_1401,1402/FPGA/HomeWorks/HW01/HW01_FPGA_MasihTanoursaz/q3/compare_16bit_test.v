module compare_16bit_test;
reg [0:15]a, b;
wire x, y, z;
compare_16bit g1(a, b, x, y, z);
initial
begin
a = 400;
b = 504;
$display("a: %d, b: %d", a ,b);
#100 $display("x: %d, y: %d, z: %d\n",x,y,z);
b = 399;
$display("a: %d, b: %d", a ,b);
#100 $display("x: %d, y: %d, z: %d\n",x,y,z);
a = 399;
$display("a: %d, b: %d", a ,b);
#100 $display("x: %d, y: %d, z: %d\n",x,y,z);

end
endmodule
