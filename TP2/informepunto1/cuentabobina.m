clear;
clc;

syms R;
syms w;
syms L;
syms C;

Z1 = R+ 1i*w*L;
Z2 = 1/(1i*w*C);

Zeq= (Z1*Z2)*(Z1+Z2);
H = simplify(Zeq);
[N,D] = numden(H);
N = expand(N);
N = collect(N,w);
D = expand(D);
D = collect(D,w);
H= N/D;
H=simplify(H);

imag(H)
