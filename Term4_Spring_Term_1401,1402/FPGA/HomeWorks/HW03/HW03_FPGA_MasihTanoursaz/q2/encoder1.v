primitive encoder1(out1, a, b ,c, d, enable);
input a, b, c, d, enable;
output out1;

table
    0 0 0 1 1 : 0;
    0 0 1 ? 1 : 0;
    0 1 ? ? 1 : 1;
    1 ? ? ? 1 : 1;
    ? ? ? ? 0 : 0;
    0 0 0 0 1 : x;
endtable
endprimitive
