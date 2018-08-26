hold off
syms x;
g(x)=47680*x;
%f(x)=((-1.24*(10^(-5))*exp((-x)/(7.05*(10^(-6)))))+(3.23*(10^(-4)))*(4.7*(10^3))-1.49);
f(x)=((-1.24*(10^(-5))*exp((-x)/(7.05*(10^(-6)))))+(3.23*(10^(-4))))*(4.7*(10^3))-1.49;
hold on
fplot(f,[0 (6.25*(10^(-5)))],'blue') %calculado teóricamente
hold on
%plot(time,vr) %proveniente del osciloscopio
plot(time+(0.0861*10^-3)-(0.6*10^-4),vr) %proveniente del osciloscopio
hold on
xlabel('Tiempo (s)')
ylabel('Vr (V)')
grid on
%FALTA: Agregar indicación en gráfico de a qué corresponde cada línea
% la roja es la calculada a mano y la azul la del osciloscopio