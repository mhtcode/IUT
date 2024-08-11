module T_FF_test;
    reg t, set, reset, clk;
    wire Q;
    T_FF t_ff(Q, t, set, reset, clk);
    integer i;
    initial 
    begin
        set = 0; reset = 0;
        #100 $monitor("clk = %d, t = %d , Q = %d", clk, t, Q);
        for(i = 0; i < 16; i = i + 1)
            #100 {set, reset, t, clk} = i;
        #200;
    end 
    
endmodule
