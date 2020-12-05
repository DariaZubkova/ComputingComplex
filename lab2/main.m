x=infsup(-5,5)
y=infsup(-5,5)
%x=infsup(-10,10)
%y=infsup(-10,10)
z = globopt0([x,y])

for i = 1:1000
    disp(i);
    answer = z(i).Estim;
    disp(answer);
    xl = z(i).Box(1).inf
    xr = z(i).Box(1).sup
    yl = z(i).Box(2).inf
    yr = z(i).Box(2).sup
    rectangle('Position',[xl yl xr-xl yr-yl])
end
axis([-8 8 -8 8])
%axis([-12 12 -12 12])