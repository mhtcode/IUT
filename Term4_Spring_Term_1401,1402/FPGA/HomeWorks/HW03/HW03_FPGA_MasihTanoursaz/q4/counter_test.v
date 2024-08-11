module counter_test;
reg enable, reset, clk;
wire [3:0]Q;
counter cntr(enable, reset, clk, Q);

initial 
begin
    enable  = 1;
    reset = 1;
    #100 reset = 0;
    $monitor("Q = %d", Q);
end
initial 
begin
    clk = 0;
    forever 
    begin
        #100 clk = ~clk;
    end
end

endmodule