module CLA_adder (
    input [3:0] in1,
    input [3:0] in2,
    input cin,
    output cout,
    output [3:0] Sum
);
    wire [3:0] or1, and1;
    wire [4:0] c;
    genvar i;

    assign or1  = in1 ^ in2;
    assign and1 = in1 & in2;

    assign c[0] = cin;
    for (i = 0; i < 4; i = i + 1) 
        begin
            assign Sum[i] = or1[i] ^ c[i];
            assign c[i+1] = and1[i] | (or1[i] & c[i]);
        end

    assign cout = c[4];

endmodule
