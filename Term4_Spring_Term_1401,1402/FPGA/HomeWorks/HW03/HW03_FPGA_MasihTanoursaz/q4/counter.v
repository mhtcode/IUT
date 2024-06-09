module counter(enable, reset, clk, Q);
    input enable, reset, clk;
    output Q;
    parameter COUNT = 4;
    wire [COUNT - 1 : 0] Q;
    wire [COUNT - 1 : 0] state;
    T_FF tff0(Q[0], enable, 0, reset, clk);
    and g1(state[0], enable, Q[0]);
    generate
        genvar i;
        for (i = 1 ; i < COUNT ; i = i + 1) 
        begin
                and g2(state[i], state[i-1], Q[i - 1]);
                T_FF tff1(Q[i], state[i], 0, reset, clk);
        end
    endgenerate
endmodule
