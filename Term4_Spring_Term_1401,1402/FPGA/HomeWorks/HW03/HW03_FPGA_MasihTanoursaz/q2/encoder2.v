primitive encoder2(out2, a, b ,c, d, enable);
input a, b, c, d, enable;
output out2;

table
    ? 0 ? 0 1: 0;
    ? 0 ? 1 1: 1;
    ? 1 ? 0 1: 1;
    ? 1 ? 1 1: 1;
    ? ? ? ? 0: x;
endtable
endprimitive
