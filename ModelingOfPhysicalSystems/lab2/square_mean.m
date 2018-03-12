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
           xlabel('timestamp');
           ylabel('Square mean of displacement in 1d');
           title(['1 dimension for ' num2str(num_of_parts) ' particles']);
       elseif dims == 2
           plot(sum(x.^2 + y.^2)/num_of_parts');
           xlabel('timestamp');
           ylabel('Square mean of displacement in 2d');
           title(['2 dimensions for ' num2str(num_of_parts) ' particles']);
       elseif dims == 3
           plot(sum(x.^2 + y.^2 + z.^2)/num_of_parts');
           xlabel('timestamp');
           ylabel('Square mean of displacement in 3d');
           title(['3 dimensions for ' num2str(num_of_parts) ' particles']);
    end
end
