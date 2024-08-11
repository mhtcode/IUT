module full_adder(input a, input b, input cin, output sum, output carry_out);
    wire w1, w2, w3;
    xor #(8, 4) xor1(w1, a, b);
    xor #(8, 4) xor2(sum, w1, cin);
    and #(5, 3) and1(w2, a, b);
    and #(5, 3) and2(w3, w1, cin);
    or #(6, 3) or1(carry_out, w2, w3);
endmodule
