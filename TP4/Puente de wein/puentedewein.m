clear;
clc;
syms s;
syms R1;
syms C1;
syms R2;
syms C3;
syms R3;
syms R4;
syms Vin;

Z1 = R1 + (1/(s*C1));
Z3 = (R3*(1/(s*C3)))/(R3+(1/(s*C3)));
VDmas = Vin*(Z3/(Z1+Z3));
VDmas = simplify(VDmas);
VDmenos = Vin*(R4/(R2+R4));
VDmenos = simplify(VDmenos);
VD = VDmas - VDmenos;
VD = simplify(VD);
H = simplify(expand(VD/Vin));
[N,D]= numden(H);
N= collect(N,R4);
%D= collect(D,R3);
H = simplify(N/D);
%w0 = 1/(sqrt(R1*R3*C1*C3));
%Q=1/((C1*R1 + C1*R3+ C3*R3)*(w0));
pretty(H)


