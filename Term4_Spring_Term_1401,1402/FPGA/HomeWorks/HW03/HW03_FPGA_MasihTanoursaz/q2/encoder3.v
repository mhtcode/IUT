primitive encoder3(valid, a, b, c, d, enable);
    output valid;
    input a, b, c, d, enable;
    table
        ? ? ? ? 0 : 0;
        1 ? ? ? 1 : 1;
        0 1 ? ? 1 : 1;
        0 0 1 ? 1 : 1; 
        0 0 0 1 1 : 1;
        0 0 0 0 1 : 0;
    endtable

endprimitive
