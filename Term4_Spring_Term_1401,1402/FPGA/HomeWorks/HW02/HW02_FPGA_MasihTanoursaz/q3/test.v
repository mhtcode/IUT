module test_log;
reg[15:0] number;
reg[2:0] base;
wire [4:0] result;
logarithm lg1(number, base, result);

initial 
begin
    $monitor("number = %d, base = %d, result = %d", number, base, result);
    #100;
    number = 256;
    base = 2;
    #100;
    number = 1024;
    base = 2;
    #100;
    number = 49;
    base = 7;
    #100;
    number = 91;
    base = 3;
    #100;
    number = 216;
    base = 6;
    #100;
end
    
endmodule