module test_adder;
    reg [7:0] a, b;
    reg carry_in;
    wire [7:0] sum;
    wire carry_out;     
    ripple_carry_adder r1(a, b, carry_in, sum, carry_out);
    initial 
    begin
        a = 15;
        b = 18;
        carry_in = 0;
    #200 $display("Test1 : %d + %d + %d = %d (carry out), %d (sum)", a, b, carry_in, carry_out, sum);
    #400;
    end
endmodule