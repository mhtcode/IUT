primitive T_FF(Q, t, set, reset, clk);
    input t, set, reset, clk;
    output reg Q;
    initial Q = 0;
    table
        ? ? 1 ? : ? : 0 ;
        ? 1 0 ? : ? : 1 ;
        ? 0 0 (1 ?) : ? : - ;
        ? 0 0 (x ?) : ? : - ;
        ? 0 0 (0 x) : ? : - ;
        ? 0 0 0 : ? : - ;
        0 0 0 ? : ? : - ;
        1 0 0 (0 1) : 0 : 1 ;
        1 0 0 (0 1) : 1 : 0 ;
    endtable
endprimitive
