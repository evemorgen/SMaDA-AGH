create (n7573386803:InputNeuron { name: 'input1', value: 1, delta: 0, learning_factor: 0.3, network: 'som', layer: 'NormalInput'}),(n50743938800:InputNeuron { name: 'input3', value: 1, delta: 0, learning_factor: 0.3, network: 'som', layer: 'NormalInput'}),(n70376047974:InputNeuron { name: 'input5', value: 1, delta: 0, learning_factor: 0.3, network: 'som', layer: 'NormalInput'}),(n92469900450:InputNeuron { name: 'input7', value: 1, delta: 0, learning_factor: 0.3, network: 'som', layer: 'NormalInput'}),(n40600937780:Neuron { name: 'Rocket16', value: 0, delta: 0, learning_factor: 0.3, network: 'som', layer: 'layer'}),(n30991915229:Neuron { name: 'Soleil17', value: 0, delta: 0, learning_factor: 0.3, network: 'som', layer: 'layer'}),(n90999309296:Neuron { name: 'Urania18', value: 0, delta: 0, learning_factor: 0.3, network: 'som', layer: 'layer'}),(n29863202202:OutputNeuron { name: 'output0', value: 0, delta: 0, learning_factor: 0.3, network: 'som', layer: 'OutputLayer'}),(n69016120357:OutputNeuron { name: 'output2', value: 0, delta: 0, learning_factor: 0.3, network: 'som', layer: 'OutputLayer'}),(n36428903496:OutputNeuron { name: 'output4', value: 0, delta: 0, learning_factor: 0.3, network: 'som', layer: 'OutputLayer'}),(n6058550579:InputNeuron { name: 'input9', value: 1, delta: 0, learning_factor: 0.3, network: 'som', layer: 'InputSom'}),(n62592942362:InputNeuron { name: 'input11', value: 1, delta: 0, learning_factor: 0.3, network: 'som', layer: 'InputSom'}),(n64871085298:InputNeuron { name: 'input13', value: 1, delta: 0, learning_factor: 0.3, network: 'som', layer: 'InputSom'}),(n64107656863:InputNeuron { name: 'input15', value: 1, delta: 0, learning_factor: 0.3, network: 'som', layer: 'InputSom'});
                    match (a:Neuron), (b:InputNeuron)
                    where a.name = 'Urania18' and b.name = 'input11'
                    create (a)-[r:connected {weight: -1.812483899378584, network: 'som'}]->(b);
                
                    match (a:Neuron), (b:InputNeuron)
                    where a.name = 'Rocket16' and b.name = 'input15'
                    create (a)-[r:connected {weight: 0.1775442617430727, network: 'som'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Rocket16' and b.name = 'output4'
                    create (a)-[r:connected {weight: -0.8988732136156967, network: 'som'}]->(b);
                
                    match (a:Neuron), (b:InputNeuron)
                    where a.name = 'Soleil17' and b.name = 'input9'
                    create (a)-[r:connected {weight: -0.9150064762561145, network: 'som'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input1' and b.name = 'Soleil17'
                    create (a)-[r:connected {weight: 0.08832273537886115, network: 'som'}]->(b);
                
                    match (a:Neuron), (b:InputNeuron)
                    where a.name = 'Soleil17' and b.name = 'input15'
                    create (a)-[r:connected {weight: 0.5088411053943189, network: 'som'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input7' and b.name = 'Soleil17'
                    create (a)-[r:connected {weight: -0.3991405798923542, network: 'som'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Soleil17' and b.name = 'output2'
                    create (a)-[r:connected {weight: -1.217129130805764, network: 'som'}]->(b);
                
                    match (a:Neuron), (b:InputNeuron)
                    where a.name = 'Soleil17' and b.name = 'input11'
                    create (a)-[r:connected {weight: 1.448872180901485, network: 'som'}]->(b);
                
                    match (a:Neuron), (b:InputNeuron)
                    where a.name = 'Soleil17' and b.name = 'input13'
                    create (a)-[r:connected {weight: -1.4262071392815807, network: 'som'}]->(b);
                
                    match (a:Neuron), (b:InputNeuron)
                    where a.name = 'Urania18' and b.name = 'input9'
                    create (a)-[r:connected {weight: 0.8558849420927159, network: 'som'}]->(b);
                
                    match (a:Neuron), (b:InputNeuron)
                    where a.name = 'Urania18' and b.name = 'input15'
                    create (a)-[r:connected {weight: -1.9595098491895833, network: 'som'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Rocket16' and b.name = 'output2'
                    create (a)-[r:connected {weight: 0.571727601466526, network: 'som'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Urania18' and b.name = 'output2'
                    create (a)-[r:connected {weight: 0.8160872463835029, network: 'som'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Urania18' and b.name = 'output0'
                    create (a)-[r:connected {weight: 1.2037583135055998, network: 'som'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Rocket16' and b.name = 'output0'
                    create (a)-[r:connected {weight: 0.17472769065583282, network: 'som'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Urania18' and b.name = 'output4'
                    create (a)-[r:connected {weight: -0.6042407540676376, network: 'som'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input3' and b.name = 'Urania18'
                    create (a)-[r:connected {weight: 1.9393329657729916, network: 'som'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input3' and b.name = 'Rocket16'
                    create (a)-[r:connected {weight: 0.6450334110165925, network: 'som'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Soleil17' and b.name = 'output4'
                    create (a)-[r:connected {weight: 1.167692765005146, network: 'som'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input3' and b.name = 'Soleil17'
                    create (a)-[r:connected {weight: 1.0044354897732335, network: 'som'}]->(b);
                
                    match (a:Neuron), (b:InputNeuron)
                    where a.name = 'Rocket16' and b.name = 'input9'
                    create (a)-[r:connected {weight: -0.29737790874567294, network: 'som'}]->(b);
                
                    match (a:Neuron), (b:InputNeuron)
                    where a.name = 'Urania18' and b.name = 'input13'
                    create (a)-[r:connected {weight: 1.4770150032107856, network: 'som'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Soleil17' and b.name = 'output0'
                    create (a)-[r:connected {weight: 0.21424453166658397, network: 'som'}]->(b);
                
                    match (a:Neuron), (b:InputNeuron)
                    where a.name = 'Rocket16' and b.name = 'input13'
                    create (a)-[r:connected {weight: -0.6453109189036321, network: 'som'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input7' and b.name = 'Rocket16'
                    create (a)-[r:connected {weight: -0.8304992372720297, network: 'som'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input1' and b.name = 'Rocket16'
                    create (a)-[r:connected {weight: -0.030271093247412395, network: 'som'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input5' and b.name = 'Rocket16'
                    create (a)-[r:connected {weight: -0.5198503739994811, network: 'som'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input5' and b.name = 'Soleil17'
                    create (a)-[r:connected {weight: 0.6084286100213823, network: 'som'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input5' and b.name = 'Urania18'
                    create (a)-[r:connected {weight: 1.4740618809872186, network: 'som'}]->(b);
                
                    match (a:Neuron), (b:InputNeuron)
                    where a.name = 'Rocket16' and b.name = 'input11'
                    create (a)-[r:connected {weight: -0.7436784368851899, network: 'som'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input7' and b.name = 'Urania18'
                    create (a)-[r:connected {weight: 0.27258146054116983, network: 'som'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input1' and b.name = 'Urania18'
                    create (a)-[r:connected {weight: 0.808153241895047, network: 'som'}]->(b);
                