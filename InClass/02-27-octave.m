I = 1:10 %Set to 1 thru 10
J = 2:2:10 %evens only

sum = 0;
for i = I 
	sum += sum + 1/i;
end

sum
