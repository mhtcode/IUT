module encoder_test;
    wire out1, out2, valid;
    reg a, b, c, d, enable;
    encoder1 u1(out1, a, b, c, d, enable);
    encoder2 u2(out2, a, b, c, d, enable);
    encoder3 u3(valid, a, b, c, d, enable);
    integer i;
    initial begin
        #100 enable = 1;
        $monitor("out1 = %d, out2 = %d, valid = %d", out1, out2, valid);
        for (i = 0; i < 16; i = i + 1)
            #100 {a, b, c, d} = i;    
        #100;
        enable = 0;
        #100;        
    end
endmodule
