module calc_test();
reg a, b, c, d;
wire ans;

calc c1(ans, a, b, c, d);
integer i;
initial begin
    $monitor("a = %d, b = %d, c = %d, d = %d, ans is: %d",a, b, c ,d, ans);
    for (i = 0; i < 16; i = i+1) 
    begin
        #100 {a, b, c ,d} = i;
    end
    #200;
end


endmodule
