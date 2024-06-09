module fact_test;
reg [3:0] number;
wire [24:0] result;

factorial fac1(number, result);

initial 
begin
    $monitor("number = %d, result = %d", number, result);
    #100;
    number = 3;
    #100;
    number = 4;
    #100;
    number = 6;
    #100;
end
    
endmodule