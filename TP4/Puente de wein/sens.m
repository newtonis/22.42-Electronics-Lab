f = 5000:1:50000;
w = 2*pi*f;

C = 1e-9;
dR1sobreR1= 0.01; 
%sR1 =( 1./((1./(w*C)) ))*dR1sobreR1;
sR1= 1/R1;
plot(f,sR1);