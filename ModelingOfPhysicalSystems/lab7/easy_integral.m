function sumsum = easy_integral(c_in, i, dt, tt, lambda)
    sum = 0;
    t = i * dt;
    for j = 1:i-1
        tp = j*dt;
        sum = sum + c_in(j) * ...
                    tt^(-1) * ...
                    exp(-1 * (t - tp) / tt) * ... 
                    exp(-1 * lambda * (t - tp));
    end;
    sumsum = sum * dt;
end