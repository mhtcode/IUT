module division_test;
reg [0:7]maghsoom, maghsoom_elaih;
wire [0:7]kharej_ghesmat, baghimandeh;
division g1(maghsoom, maghsoom_elaih, kharej_ghesmat, baghimandeh);
initial
begin
maghsoom = 15;
maghsoom_elaih = 6;
$display("Test1 : maghsoom = %d, maghsoom_elaih = %d", maghsoom, maghsoom_elaih);
#100 $display("Test1 :\nkharej_ghesmat = %d, baghimandeh = %d\n", kharej_ghesmat, baghimandeh);
maghsoom = 49;
maghsoom_elaih = 7;
$display("Test2 : maghsoom = %d, maghsoom_elaih = %d", maghsoom, maghsoom_elaih);
#100 $display("Test2 :\nkharej_ghesmat = %d, baghimandeh = %d\n", kharej_ghesmat, baghimandeh);
maghsoom = 6;
maghsoom_elaih = 8;
$display("Test3 : maghsoom = %d, maghsoom_elaih = %d", maghsoom, maghsoom_elaih);
#100 $display("Test3 :\nkharej_ghesmat = %d, baghimandeh = %d\n", kharej_ghesmat, baghimandeh);
maghsoom = 255;
maghsoom_elaih = 12;
$display("Test4 : maghsoom = %d, maghsoom_elaih = %d", maghsoom, maghsoom_elaih);
end
endmodule
