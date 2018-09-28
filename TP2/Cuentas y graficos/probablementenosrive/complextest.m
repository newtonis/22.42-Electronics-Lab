syms s;
syms R;
syms L;
syms C;
syms w;

s=1i*w;
Z1= 1 / (s*C);
Z2=  s*L +R ;

Z= (Z1*Z2)/(Z1+Z2);

Z=simplify(Z);

subexpr(Z)

simplify(Z)
