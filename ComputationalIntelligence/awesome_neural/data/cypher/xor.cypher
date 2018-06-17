create (n56921658194:InputNeuron { name: 'input1', value: 1, delta: -0.06134907502497106, learning_factor: 0.3, network: 'xor'}),(n98844475228:InputNeuron { name: 'input3', value: 0, delta: -0.061351694306394776, learning_factor: 0.3, network: 'xor'}),(n28555631118:Neuron { name: 'Eartha4', value: 0.17124305362817088, delta: 0.19809358937246652, learning_factor: 0.3, network: 'xor'}),(n9522352503:Neuron { name: 'Fulu5', value: 0.0010319822101084355, delta: -0.1945767338962776, learning_factor: 0.3, network: 'xor'}),(n29309716559:Neuron { name: 'Galaxy6', value: 0.17285624914023584, delta: -0.07306248507564907, learning_factor: 0.3, network: 'xor'}),(n77964469139:Neuron { name: 'Helvetios7', value: 0.7794111845867354, delta: 0.03292152537776485, learning_factor: 0.3, network: 'xor'}),(n27389248516:OutputNeuron { name: 'output9', value: 0.9425223272781305, delta: 0.05886705896737321, learning_factor: 0.3, network: 'xor'}),(n36411170394:BiasNeuron { name: 'Kang10', value: 0.1, delta: 0, learning_factor: 0.3, network: 'xor'});
                    match (a:Neuron), (b:BiasNeuron)
                    where a.name = 'Eartha4' and b.name = 'Kang10'
                    create (a)-[r:connected {weight: -0.40627101791055287, network: 'xor'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input3' and b.name = 'Fulu5'
                    create (a)-[r:connected {weight: -9.74434251580493, network: 'xor'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input3' and b.name = 'Eartha4'
                    create (a)-[r:connected {weight: -2.260573558846505, network: 'xor'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Eartha4' and b.name = 'Galaxy6'
                    create (a)-[r:connected {weight: -13.139581891140187, network: 'xor'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input1' and b.name = 'Fulu5'
                    create (a)-[r:connected {weight: -9.82177333609712, network: 'xor'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Fulu5' and b.name = 'Galaxy6'
                    create (a)-[r:connected {weight: 13.18586651312593, network: 'xor'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Fulu5' and b.name = 'Helvetios7'
                    create (a)-[r:connected {weight: -9.883578984623433, network: 'xor'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input1' and b.name = 'Eartha4'
                    create (a)-[r:connected {weight: -2.2526328709232932, network: 'xor'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Eartha4' and b.name = 'Helvetios7'
                    create (a)-[r:connected {weight: 10.589610879809275, network: 'xor'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Helvetios7' and b.name = 'output9'
                    create (a)-[r:connected {weight: 10.095249560038898, network: 'xor'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Galaxy6' and b.name = 'output9'
                    create (a)-[r:connected {weight: -22.402448522806008, network: 'xor'}]->(b);
                