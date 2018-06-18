create (n7891222375:InputNeuron { name: 'input1', value: 0, delta: 4.7385345292276936e-05, learning_factor: 0.3, network: 'snek', layer: 'InputLayer'}),(n32597717988:InputNeuron { name: 'input3', value: 0, delta: -6.191343141027029e-05, learning_factor: 0.3, network: 'snek', layer: 'InputLayer'}),(n95551372911:InputNeuron { name: 'input5', value: 0, delta: -3.7240013043688365e-05, learning_factor: 0.3, network: 'snek', layer: 'InputLayer'}),(n6243331058:InputNeuron { name: 'input7', value: -1, delta: 4.4687619354802594e-05, learning_factor: 0.3, network: 'snek', layer: 'InputLayer'}),(n69050686442:InputNeuron { name: 'input9', value: 0.17780768448935277, delta: -6.519558738382158e-05, learning_factor: 0.3, network: 'snek', layer: 'InputLayer'}),(n45857060421:Neuron { name: 'Kang10', value: 0.038144920288224506, delta: -1.6496211094345186e-05, learning_factor: 0.3, network: 'snek', layer: 'layer'}),(n70025669503:Neuron { name: 'Luna11', value: 0.0014261631404416538, delta: 4.5982702961581477e-05, learning_factor: 0.3, network: 'snek', layer: 'layer'}),(n42741691411:Neuron { name: 'Mars12', value: 0.05393112462546516, delta: -1.703473778267405e-05, learning_factor: 0.3, network: 'snek', layer: 'layer'}),(n1889420275:Neuron { name: 'Nova13', value: 0.3970545067715891, delta: 0.00011281887053001499, learning_factor: 0.3, network: 'snek', layer: 'layer'}),(n35309905384:Neuron { name: 'Orion14', value: 0.5132376248213798, delta: 7.241742457292453e-05, learning_factor: 0.3, network: 'snek', layer: 'layer'}),(n68254010485:Neuron { name: 'Pluto15', value: 0.5584553316490567, delta: 7.548515014161058e-05, learning_factor: 0.3, network: 'snek', layer: 'layer'}),(n18439670065:OutputNeuron { name: 'output17', value: 0.9865880094892688, delta: 0.0053612214529228375, learning_factor: 0.3, network: 'snek', layer: 'OutputLayer'});
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input7' and b.name = 'Luna11'
                    create (a)-[r:connected {weight: 6.251612114175301, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input9' and b.name = 'Mars12'
                    create (a)-[r:connected {weight: 6.916430873651566, network: 'snek'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Kang10' and b.name = 'Orion14'
                    create (a)-[r:connected {weight: 8.20612103889036, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input5' and b.name = 'Luna11'
                    create (a)-[r:connected {weight: -3.7356743760849387, network: 'snek'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Luna11' and b.name = 'Nova13'
                    create (a)-[r:connected {weight: 9.257740616256589, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input3' and b.name = 'Mars12'
                    create (a)-[r:connected {weight: -8.947335092997683, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input7' and b.name = 'Kang10'
                    create (a)-[r:connected {weight: 4.68282144429137, network: 'snek'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Kang10' and b.name = 'Pluto15'
                    create (a)-[r:connected {weight: -4.371017848663032, network: 'snek'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Kang10' and b.name = 'Nova13'
                    create (a)-[r:connected {weight: -3.4502709472980615, network: 'snek'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Mars12' and b.name = 'Orion14'
                    create (a)-[r:connected {weight: -4.991455611030178, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input1' and b.name = 'Kang10'
                    create (a)-[r:connected {weight: -0.045820984857519426, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input7' and b.name = 'Mars12'
                    create (a)-[r:connected {weight: 4.12333759977665, network: 'snek'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Luna11' and b.name = 'Orion14'
                    create (a)-[r:connected {weight: 6.781016959716803, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input9' and b.name = 'Luna11'
                    create (a)-[r:connected {weight: -2.057860549891019, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input1' and b.name = 'Mars12'
                    create (a)-[r:connected {weight: 5.149151381318496, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input3' and b.name = 'Luna11'
                    create (a)-[r:connected {weight: -9.532718117574138, network: 'snek'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Nova13' and b.name = 'output17'
                    create (a)-[r:connected {weight: 3.9462891445501302, network: 'snek'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Luna11' and b.name = 'Pluto15'
                    create (a)-[r:connected {weight: 5.149600977927259, network: 'snek'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Mars12' and b.name = 'Nova13'
                    create (a)-[r:connected {weight: -5.628766356477494, network: 'snek'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Mars12' and b.name = 'Pluto15'
                    create (a)-[r:connected {weight: 7.354863958922089, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input3' and b.name = 'Kang10'
                    create (a)-[r:connected {weight: -6.435985787318816, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input9' and b.name = 'Kang10'
                    create (a)-[r:connected {weight: 8.001620022931316, network: 'snek'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Pluto15' and b.name = 'output17'
                    create (a)-[r:connected {weight: 2.6404018772363207, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input5' and b.name = 'Kang10'
                    create (a)-[r:connected {weight: 9.693637056830411, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input5' and b.name = 'Mars12'
                    create (a)-[r:connected {weight: -9.883488143811952, network: 'snek'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input1' and b.name = 'Luna11'
                    create (a)-[r:connected {weight: 5.64872547390578, network: 'snek'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Orion14' and b.name = 'output17'
                    create (a)-[r:connected {weight: 2.5330960582362416, network: 'snek'}]->(b);
                