function [] = square_mean(dims, num_of_movements, num_of_particles)
    N = num_of_movements;
    num_of_parts = num_of_particles;
    x = zeros(num_of_parts, 1);
    y = zeros(num_of_parts, 1);
    z = zeros(num_of_parts, 1);

    for i=2:N
       x = [x x(:,i-1)+randn(num_of_parts, 1)];
       y = [y y(:,i-1)+randn(num_of_parts, 1)];
       z = [z z(:,i-1)+randn(num_of_parts, 1)];
    end

    if dims == 1
           plot(sum(x.^2)/num_of_parts');
           figure;
           histogram(x);
       elseif dims == 2
           plot(sum(x.^2 + y.^2)/num_of_parts');
           figure;
           histogram2(x,y);
       elseif dims == 3
           plot(sum(x.^2 + y.^2 + z.^2)/num_of_parts');
           figure;
           hist3(x,y,z);
    end
    ylabel('x coordinate');
    xlabel('timestamp');
end
