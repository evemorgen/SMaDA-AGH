create (n69715906779:InputNeuron { name: 'input1', value: 1, delta: 0, learning_factor: 0.1, network: 'xor'}),(n58327315313:InputNeuron { name: 'input3', value: 1, delta: 0, learning_factor: 0.1, network: 'xor'}),(n45850458882:Neuron { name: 'Eartha4', value: 0, delta: 0, learning_factor: 0.1, network: 'xor'}),(n2138266191:Neuron { name: 'Fulu5', value: 0, delta: 0, learning_factor: 0.1, network: 'xor'}),(n1809821924:Neuron { name: 'Galaxy6', value: 0, delta: 0, learning_factor: 0.1, network: 'xor'}),(n55690469380:Neuron { name: 'Helvetios7', value: 0, delta: 0, learning_factor: 0.1, network: 'xor'}),(n54691218711:OutputNeuron { name: 'output9', value: 0, delta: 0, learning_factor: 0.1, network: 'xor'}),(n21300350160:BiasNeuron { name: 'Kang10', value: 0.3, delta: 0, learning_factor: 0.1, network: 'xor'});
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input1' and b.name = 'Eartha4'
                    create (a)-[r:connected {weight: 4.194596839581317, network: 'xor'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input1' and b.name = 'Fulu5'
                    create (a)-[r:connected {weight: 2.547774554880915, network: 'xor'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input3' and b.name = 'Eartha4'
                    create (a)-[r:connected {weight: -1.2333201477219777, network: 'xor'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input3' and b.name = 'Fulu5'
                    create (a)-[r:connected {weight: 2.7885841849219317, network: 'xor'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input1' and b.name = 'Eartha4'
                    create (a)-[r:connected {weight: 4.194596839581317, network: 'xor'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input3' and b.name = 'Eartha4'
                    create (a)-[r:connected {weight: -1.2333201477219777, network: 'xor'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Eartha4' and b.name = 'Galaxy6'
                    create (a)-[r:connected {weight: -1.836623572439338, network: 'xor'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Eartha4' and b.name = 'Helvetios7'
                    create (a)-[r:connected {weight: 1.1384233195313822, network: 'xor'}]->(b);
                
                    match (a:Neuron), (b:BiasNeuron)
                    where a.name = 'Eartha4' and b.name = 'Kang10'
                    create (a)-[r:connected {weight: -1.172178639589064, network: 'xor'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input1' and b.name = 'Fulu5'
                    create (a)-[r:connected {weight: 2.547774554880915, network: 'xor'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input3' and b.name = 'Fulu5'
                    create (a)-[r:connected {weight: 2.7885841849219317, network: 'xor'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Fulu5' and b.name = 'Galaxy6'
                    create (a)-[r:connected {weight: -1.4116226311698483, network: 'xor'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Fulu5' and b.name = 'Helvetios7'
                    create (a)-[r:connected {weight: -0.876264014708287, network: 'xor'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Eartha4' and b.name = 'Galaxy6'
                    create (a)-[r:connected {weight: -1.836623572439338, network: 'xor'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Fulu5' and b.name = 'Galaxy6'
                    create (a)-[r:connected {weight: -1.4116226311698483, network: 'xor'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Galaxy6' and b.name = 'output9'
                    create (a)-[r:connected {weight: -2.5581358448732603, network: 'xor'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Eartha4' and b.name = 'Helvetios7'
                    create (a)-[r:connected {weight: 1.1384233195313822, network: 'xor'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Fulu5' and b.name = 'Helvetios7'
                    create (a)-[r:connected {weight: -0.876264014708287, network: 'xor'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Helvetios7' and b.name = 'output9'
                    create (a)-[r:connected {weight: 2.10235452900461, network: 'xor'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Galaxy6' and b.name = 'output9'
                    create (a)-[r:connected {weight: -2.5581358448732603, network: 'xor'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Helvetios7' and b.name = 'output9'
                    create (a)-[r:connected {weight: 2.10235452900461, network: 'xor'}]->(b);
                
                    match (a:Neuron), (b:BiasNeuron)
                    where a.name = 'Eartha4' and b.name = 'Kang10'
                    create (a)-[r:connected {weight: -1.172178639589064, network: 'xor'}]->(b);
                