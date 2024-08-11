module logarithm(input [15:0] number, input [2:0] base, output reg[4:0]result);
reg [4:0]res;

always @(number or base) 
    log_task();

task log_task;
    begin
        res = 0;
        if(base < 1 || base == 1)
            $display("base should be > 1");
        else 
        begin
            while(base ** res < number)
                res = res + 1;
                if(base ** res == number) 
                   //break; // Compile but have error for simulating
		            //$display("Answer is %d", res);
                    result = res;
                else 
                    res = res - 1;
        end
        result = res;
    end
endtask
endmodule
