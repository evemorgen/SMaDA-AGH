create (n92564364750:InputNeuron { name: 'input1', value: 5.4, delta: -0.0001214591182276905, learning_factor: 0.3, network: 'iris', layer: 'InputLayer'}),(n5171844914:InputNeuron { name: 'input3', value: 3.7, delta: -9.465852921568152e-05, learning_factor: 0.3, network: 'iris', layer: 'InputLayer'}),(n61029678040:InputNeuron { name: 'input5', value: 1.5, delta: 0.00022236460097941347, learning_factor: 0.3, network: 'iris', layer: 'InputLayer'}),(n94687800414:InputNeuron { name: 'input7', value: 0.2, delta: 0.0003155307971942225, learning_factor: 0.3, network: 'iris', layer: 'InputLayer'}),(n54770380045:Neuron { name: 'Io8', value: 0.502575684503213, delta: 5.9871760264400564e-05, learning_factor: 0.3, network: 'iris', layer: 'layer'}),(n8100185270:Neuron { name: 'Jupiter9', value: 0.9998836081313175, delta: -0.001047837951643029, learning_factor: 0.3, network: 'iris', layer: 'layer'}),(n96997042393:Neuron { name: 'Kang10', value: 0.9978238737639455, delta: -0.0010628784447660993, learning_factor: 0.3, network: 'iris', layer: 'layer'}),(n33528052298:Neuron { name: 'Luna11', value: 0.99887878039145, delta: -0.0009753843807012502, learning_factor: 0.3, network: 'iris', layer: 'layer'}),(n60268587192:Neuron { name: 'Mars12', value: 0.00041415781205387945, delta: 0.00014215049600228385, learning_factor: 0.3, network: 'iris', layer: 'layer'}),(n47003889022:Neuron { name: 'Nova13', value: 1.0, delta: -0.00025689615112989555, learning_factor: 0.3, network: 'iris', layer: 'layer'}),(n83380509943:Neuron { name: 'Orion14', value: 3.4453481039251022e-12, delta: 0.00017130867653531348, learning_factor: 0.3, network: 'iris', layer: 'layer'}),(n59192932745:Neuron { name: 'Pluto15', value: 0.9999993107724067, delta: 0.00028810043548018426, learning_factor: 0.3, network: 'iris', layer: 'layer'}),(n58540457191:OutputNeuron { name: 'output17', value: 9.543527770384937e-09, delta: 0.0013132507009330219, learning_factor: 0.3, network: 'iris', layer: 'OutputLayer'}),(n57971993241:OutputNeuron { name: 'output19', value: 0.007602732652975051, delta: -0.0033964734115439145, learning_factor: 0.3, network: 'iris', layer: 'OutputLayer'}),(n60879265239:OutputNeuron { name: 'output1', value: 0.9941136669266334, delta: -0.0006782285445961751, learning_factor: 0.3, network: 'iris', layer: 'OutputLayer'});
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Nova13' and b.name = 'output19'
                    create (a)-[r:connected {weight: 19.17258054858645, network: 'iris'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input3' and b.name = 'Jupiter9'
                    create (a)-[r:connected {weight: 10.577124698099428, network: 'iris'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input7' and b.name = 'Luna11'
                    create (a)-[r:connected {weight: -5.854813379274471, network: 'iris'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Pluto15' and b.name = 'output1'
                    create (a)-[r:connected {weight: 12.611373757738523, network: 'iris'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input3' and b.name = 'Mars12'
                    create (a)-[r:connected {weight: -4.601177047304394, network: 'iris'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input1' and b.name = 'Kang10'
                    create (a)-[r:connected {weight: 7.229740262736691, network: 'iris'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Kang10' and b.name = 'Orion14'
                    create (a)-[r:connected {weight: -13.462798312742361, network: 'iris'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Kang10' and b.name = 'Pluto15'
                    create (a)-[r:connected {weight: 5.94740623677801, network: 'iris'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Luna11' and b.name = 'Nova13'
                    create (a)-[r:connected {weight: 28.476587379350413, network: 'iris'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input7' and b.name = 'Kang10'
                    create (a)-[r:connected {weight: -3.6646777337882965, network: 'iris'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Pluto15' and b.name = 'output19'
                    create (a)-[r:connected {weight: -26.13204963942452, network: 'iris'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input3' and b.name = 'Io8'
                    create (a)-[r:connected {weight: -2.87735291748009, network: 'iris'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input1' and b.name = 'Jupiter9'
                    create (a)-[r:connected {weight: -4.410564407787704, network: 'iris'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Orion14' and b.name = 'output17'
                    create (a)-[r:connected {weight: 14.360716865631264, network: 'iris'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Luna11' and b.name = 'Pluto15'
                    create (a)-[r:connected {weight: 6.50964206808364, network: 'iris'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Kang10' and b.name = 'Nova13'
                    create (a)-[r:connected {weight: 30.14335426111511, network: 'iris'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Jupiter9' and b.name = 'Pluto15'
                    create (a)-[r:connected {weight: 10.498972815661531, network: 'iris'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input1' and b.name = 'Mars12'
                    create (a)-[r:connected {weight: 0.035049103730074, network: 'iris'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Mars12' and b.name = 'Orion14'
                    create (a)-[r:connected {weight: 2.8216831665588824, network: 'iris'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Jupiter9' and b.name = 'Orion14'
                    create (a)-[r:connected {weight: -12.904624477545871, network: 'iris'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Mars12' and b.name = 'Pluto15'
                    create (a)-[r:connected {weight: -9.56361960538607, network: 'iris'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input5' and b.name = 'Mars12'
                    create (a)-[r:connected {weight: 3.518364165090561, network: 'iris'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Orion14' and b.name = 'output1'
                    create (a)-[r:connected {weight: -11.940553025419717, network: 'iris'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input7' and b.name = 'Jupiter9'
                    create (a)-[r:connected {weight: -8.486329710661398, network: 'iris'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input5' and b.name = 'Luna11'
                    create (a)-[r:connected {weight: -3.312030659379815, network: 'iris'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Io8' and b.name = 'Nova13'
                    create (a)-[r:connected {weight: -2.1346345398141064, network: 'iris'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Nova13' and b.name = 'output1'
                    create (a)-[r:connected {weight: -5.283910326211698, network: 'iris'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Mars12' and b.name = 'Nova13'
                    create (a)-[r:connected {weight: -3.0136583613445658, network: 'iris'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Pluto15' and b.name = 'output17'
                    create (a)-[r:connected {weight: -3.796293228999866, network: 'iris'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input3' and b.name = 'Luna11'
                    create (a)-[r:connected {weight: -0.2450104668610459, network: 'iris'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input1' and b.name = 'Io8'
                    create (a)-[r:connected {weight: 2.1351185996385733, network: 'iris'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input5' and b.name = 'Jupiter9'
                    create (a)-[r:connected {weight: -0.4536208228617363, network: 'iris'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Io8' and b.name = 'Pluto15'
                    create (a)-[r:connected {weight: -5.297636933972318, network: 'iris'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input3' and b.name = 'Kang10'
                    create (a)-[r:connected {weight: -5.286438747007909, network: 'iris'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Io8' and b.name = 'Orion14'
                    create (a)-[r:connected {weight: 0.33653628890929577, network: 'iris'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Nova13' and b.name = 'output17'
                    create (a)-[r:connected {weight: -22.58571313476688, network: 'iris'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input5' and b.name = 'Kang10'
                    create (a)-[r:connected {weight: -6.662339537452146, network: 'iris'}]->(b);
                
                    match (a:Neuron), (b:OutputNeuron)
                    where a.name = 'Orion14' and b.name = 'output19'
                    create (a)-[r:connected {weight: -12.271665253507951, network: 'iris'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Luna11' and b.name = 'Orion14'
                    create (a)-[r:connected {weight: -11.552341055793297, network: 'iris'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input7' and b.name = 'Mars12'
                    create (a)-[r:connected {weight: 2.153081017398478, network: 'iris'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input1' and b.name = 'Luna11'
                    create (a)-[r:connected {weight: 3.101613644418654, network: 'iris'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input7' and b.name = 'Io8'
                    create (a)-[r:connected {weight: 2.9898080071328037, network: 'iris'}]->(b);
                
                    match (a:Neuron), (b:Neuron)
                    where a.name = 'Jupiter9' and b.name = 'Nova13'
                    create (a)-[r:connected {weight: 30.09798431424917, network: 'iris'}]->(b);
                
                    match (a:InputNeuron), (b:Neuron)
                    where a.name = 'input5' and b.name = 'Io8'
                    create (a)-[r:connected {weight: -0.9777852782966125, network: 'iris'}]->(b);
                