syms s;
R=120;
C=10e-9;
L=1000e-6;
H= R/(R+s*L +1/(s*C));
step=H/s;
K=ilaplace(step);

w0=1/(L*C)**(1/2);