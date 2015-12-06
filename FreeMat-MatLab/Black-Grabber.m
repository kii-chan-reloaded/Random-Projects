pic=imread('YOUR FILE.jpg');
x=length(pic(:,1));
y=length(pic(1,:));
for i=1:x
    for k=1:y
        black(i,k)=0;
        alpha(i,k)=255-pic(i,k);
    end
end
imwrite('YOUR FILE.png' black gray alpha)
clear all
