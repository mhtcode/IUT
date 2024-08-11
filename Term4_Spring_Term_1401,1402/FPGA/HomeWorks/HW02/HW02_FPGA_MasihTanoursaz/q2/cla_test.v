module cla_test;

  reg [3:0] a;
  reg [3:0] b;
  reg cin;


  wire [3:0] sum;
  wire cout;


  CLA_adder cl_ad (a, b, cin, cout, sum);


  initial 
  begin
    $monitor("Test : %d + %d + %d = %d (carry out), %d (sum)", a, b, cin, cout, sum);
    a = 2;
    b = 4;
    cin = 0;
    #100;
    a = 6;
    b = 4;
    cin = 0;
    #100;
    a = 5;
    b = 0;
    cin = 1;
    #200;
  end
endmodule
