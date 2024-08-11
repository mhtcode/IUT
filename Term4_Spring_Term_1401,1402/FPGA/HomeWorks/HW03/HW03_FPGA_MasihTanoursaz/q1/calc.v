primitive calc (ans, a, b, c, d);
input a, b, c, d;
output ans;
table
    ? ? 0 ? : 1;
    ? ? ? 0 : 1;
    0 ? 1 1 : 0;
    1 0 1 1 : 1;
    1 1 1 1 : 0;
endtable
endprimitive
