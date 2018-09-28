syms w;
syms 
Z1= 1./(1i.*w*C);
Z2= R + 1i.*w*L;
Z= (Z1.*Z2)./(Z1+Z2);