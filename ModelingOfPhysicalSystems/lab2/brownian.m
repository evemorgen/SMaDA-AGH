function [] = brownian(dims, num_of_movements, num_of_particles)
   figure;
   for i = 1:num_of_particles
       N = num_of_movements;
       X(1) = 0;
       Y(1) = 0;
       Z(1) = 0;

       for i=2:N
           X(i) = X(i-1) + randn();
           Y(i) = Y(i-1) + randn();
           Z(i) = Z(i-1) + randn();
       end

       % plot the result
       if dims == 1
           plot(Y);
           ylabel('x coordinate');
           xlabel('timestamp');
       elseif dims == 2
           plot(X,Y);
           xlabel('x coordinate');
           ylabel('y coordinate');
       elseif dims == 3
           plot3(X,Y,Z);
           xlabel('x coordinate');
           ylabel('y coordinate');
           zlabel('z coordinate')
       end
       hold on;
   end
end