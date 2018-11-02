syms R3;
syms X3;
syms dR3;
Z3 = (R3*1j*X3)/(R3+1j*X3);
dZ3 = (((R3+dR3)*1j*X3)/(R3+dR3+1j*X3))-Z3;
[N,D]=numden(dZ3);
 D