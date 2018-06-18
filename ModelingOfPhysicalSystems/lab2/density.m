function [] = density(dims, num_of_particles)
    num_of_parts = num_of_particles;
    x = zeros(num_of_parts, 1);
    y = zeros(num_of_parts, 1);

    for i=2:num_of_parts
       x = [x x(:,i-1)+randn(num_of_parts, 1)];
       y = [y y(:,i-1)+randn(num_of_parts, 1)];
    end

    if dims == 1
           histogram(x);
           xlabel('x coordinate');
           ylabel('number of particles');
           title(['1 dimension for ' num2str(num_of_parts) ' particles']);
       elseif dims == 2
           histogram2(x,y);
           xlabel('x coordinate');
           ylabel('y coordinate');
           zlabel('number of particles');
           title(['2 dimensions for ' num2str(num_of_parts) ' particles']);
    end
end
