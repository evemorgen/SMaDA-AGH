create (n67074755946:InputNeuron { name: 'input1', value: 1, delta: -8.387821714151271e-05, learning_factor: 0.3, network: 'snek', layer: 'InputLayer'}),(n13013104035:InputNeuron { name: 'input3', value: 0, delta: 6.124348186088107e-06, learning_factor: 0.3, network: 'snek', layer: 'InputLayer'}),(n21798432121:InputNeuron { name: 'input5', value: 0, delta: 7.2748948699445945e-06, learning_factor: 0.3, network: 'snek', layer: 'InputLayer'}),(n9107604150:InputNeuron { name: 'input7', value: 0, delta: -7.115124204214612e-07, learning_factor: 0.3, network: 'snek', layer: 'InputLayer'}),(n42557068410:Neuron { name: 'Io8', value: 0.15617434046305181, delta: 3.318178802937504e-06, learning_factor: 0.3, network: 'snek', layer: 'layer'}),(n60237605202:Neuron { name: 'Jupiter9', value: 0.9699193782233223, delta: -1.6308360980805167e-05, learning_factor: 0.3, network: 'snek', layer: 'layer'}),(n2879383829:Neuron { name: 'Kang10', value: 0.015665668873218155, delta: 1.5326591592915957e-05, learning_factor: 0.3, network: 'snek', layer: 'layer'}),(n57057606800:Neuron { name: 'Luna11', value: 0.015939983326889565, delta: 1.6344010871017816e-05, learning_factor: 0.3, network: 'snek', layer: 'layer'}),(n10183847676:Neuron { name: 'Mars12', value: 0.026072022184137008, delta: 1.394498658853445e-05, learning_factor: 0.3, network: 'snek', layer: 'layer'}),(n47069139337:OutputNeuron { name: 'output14', value: 0.012292813558320053, delta: 0.0015189397002709493, learning_factor: 0.3, network: 'snek', layer: 'OutputLayer'});
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input7' and b.name = 'Jupiter9'
                    create (a)-[r:connected {weight: -0.13619404123657802, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input7' and b.name = 'Kang10'
                    create (a)-[r:connected {weight: -0.3613489525740858, network: 'snek'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Io8' and b.name = 'output14'
                    create (a)-[r:connected {weight: 1.4403864894735212, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input1' and b.name = 'Luna11'
                    create (a)-[r:connected {weight: -5.889794657680867, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input1' and b.name = 'Kang10'
                    create (a)-[r:connected {weight: -5.914991406684923, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input3' and b.name = 'Io8'
                    create (a)-[r:connected {weight: 0.8177308194374179, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input7' and b.name = 'Mars12'
                    create (a)-[r:connected {weight: -0.8762816847836159, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input5' and b.name = 'Luna11'
                    create (a)-[r:connected {weight: -0.033587961094180455, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input3' and b.name = 'Jupiter9'
                    create (a)-[r:connected {weight: -0.4258942467963774, network: 'snek'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Jupiter9' and b.name = 'output14'
                    create (a)-[r:connected {weight: -7.079285034788343, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input3' and b.name = 'Kang10'
                    create (a)-[r:connected {weight: 0.403882882374553, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input1' and b.name = 'Jupiter9'
                    create (a)-[r:connected {weight: 4.961902547391814, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input7' and b.name = 'Io8'
                    create (a)-[r:connected {weight: -0.6169788985261779, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input3' and b.name = 'Luna11'
                    create (a)-[r:connected {weight: 1.4509809690123543, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input5' and b.name = 'Io8'
                    create (a)-[r:connected {weight: -1.8094115974296112, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input5' and b.name = 'Mars12'
                    create (a)-[r:connected {weight: 1.1660682749375726, network: 'snek'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Luna11' and b.name = 'output14'
                    create (a)-[r:connected {weight: 7.094760995021463, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input1' and b.name = 'Mars12'
                    create (a)-[r:connected {weight: -5.172106519637513, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input7' and b.name = 'Luna11'
                    create (a)-[r:connected {weight: 0.8863639443860801, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input5' and b.name = 'Kang10'
                    create (a)-[r:connected {weight: 1.330488989926275, network: 'snek'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Kang10' and b.name = 'output14'
                    create (a)-[r:connected {weight: 6.653110174364843, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input1' and b.name = 'Io8'
                    create (a)-[r:connected {weight: -2.4099613691738666, network: 'snek'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Mars12' and b.name = 'output14'
                    create (a)-[r:connected {weight: 6.0533700981059155, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input3' and b.name = 'Mars12'
                    create (a)-[r:connected {weight: -0.9388364304044338, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input5' and b.name = 'Jupiter9'
                    create (a)-[r:connected {weight: 0.05632906024610265, network: 'snek'}]->(b);
                