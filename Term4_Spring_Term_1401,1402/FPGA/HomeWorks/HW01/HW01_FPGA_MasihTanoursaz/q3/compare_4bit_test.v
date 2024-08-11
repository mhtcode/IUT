module compare_4bit_test;
reg [0:3]a, b;
wire x, y, z;
compare_4bit g1(a, b, x, y, z);
initial
begin
a = 10;
b = 3;
$display("a: %d, b: %d", a ,b);
#100 $display("x: %d, y: %d, z: %d",x,y,z);
b = 10;
$display("a: %d, b: %d", a ,b);
#100 $display("x: %d, y: %d, z: %d",x,y,z);
b = 15;
$display("a: %d, b: %d", a ,b);
#100 $display("x: %d, y: %d, z: %d",x,y,z);

end
endmodule
