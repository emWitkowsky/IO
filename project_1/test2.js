
// const obj = {
//     data: {
//         enemyTank: {},
//         myTank: {
//             x: 0,
//             y: 0,
//             goBack: 0,
//             goForward: 0,
//             turnLeft: 0,
//             turnRight: 0,
//             rotation: 180,
//             shoot: 0,
//         }
//     }
// }

e = {
    data: {
        myTank: {
            x: 100,
            y: 200,
            rotation: 90,
            shootCooldown: 50,
            controls: {
                turnLeft: 0,
                turnRight: 1,
                goForward: 1,
                goBack: 0,
                shoot: 1,
            }
        },
        enemyTank: {
            x: 300,
            y: 400,
            rotation: 180,
            shootCooldown: 100,
        },
        currentGameTime: 5000
    }
}


function x(e) {

    var response = {};
    var enemy = e.data.enemyTank;
    var me = e.data.myTank;

    // var input = [me.x/500.0, me.y/500.0, me.rotation/360.0, ];
    var input = [
    me.x/500.0,
    me.y/500.0,
    me.rotation/360.0,
    me.shootCooldown/100.0,
    me.controls.turnLeft,
    me.controls.turnRight,
    me.controls.goForward,
    me.controls.goBack,
    me.controls.shoot,
    enemy.x/500.0,
    enemy.y/500.0,
    enemy.rotation/360.0,
    enemy.shootCooldown/100.0,
    e.data.currentGameTime/1000.0
    ];

    var weights1 = [[-1.0338284969329834, -0.38507992029190063, 0.8973819017410278, -0.03299705311655998, 1.2706806659698486], [-0.661546528339386, 0.31577375531196594, -0.4560859799385071, 0.5882501006126404, 0.312751442193985], [-0.8027163743972778, -0.3774127960205078, -0.5876840353012085, 1.4112043380737305, -0.5536596179008484], [0.08797485381364822, 0.6361172795295715, -1.0186642408370972, 0.5492249131202698, 0.28999027609825134], [0.18167583644390106, -0.7581849098205566, 0.5933824181556702, -0.1415126621723175, -0.40436217188835144], [-0.5909397006034851, 0.5194261074066162, -0.6607786417007446, 0.3839384615421295, 0.9677669405937195], [1.0360052585601807, 0.7950882911682129, 0.5932689309120178, -1.3142929077148438, 0.27058646082878113], [-1.294846534729004, -1.3019373416900635, -1.0295988321304321, -1.0595626831054688, 0.18861272931098938], [-1.1032564640045166, 0.8235015273094177, -0.12120813131332397, -1.9728869199752808, -0.01286296546459198], [0.9711506366729736, 0.5296807289123535, -0.19432635605335236, 0.42520180344581604, -1.7095783948898315], [-0.27646946907043457, -0.8523982167243958, 1.1837577819824219, -0.2664785087108612, -0.5559020638465881], [0.035058870911598206, -0.5027052760124207, 0.005974505562335253, -0.10647782683372498, -0.7080003023147583], [1.427172303199768, -0.756071925163269, -0.5717401504516602, 0.015908025205135345, 0.47908949851989746]]
    var bias1 = [1.2013590335845947, 1.068118929862976, 0.9722748398780823, 1.4579793214797974, 1.2309434413909912]
    // console.log(weights1)

    var hidden = [0,0,0,0,0];

    var i,j;
    for (i = 0; i < 4; i++) {
        // console.log("before", hidden)
        for (j = 0; j < input.length; j++) {
            // console.log("input", input[j])
            // console.log("weights1", weights1[i][j])
            hidden[i] += input[j] * weights1[i][j];
        }
        // console.log("After", hidden)
        hidden[i] = hidden[i] + bias1[i];
        hidden[i] = 1/(1 + Math.pow(Math.E, -hidden[i]));
        // console.log(hidden[i])
    }

    console.log(hidden)
    var weights2 = [[1.1089640855789185], [1.2962065935134888], [1.7983654737472534], [1.6474452018737793], [0.6802589893341064]]
    var bias2 = [0.6250424385070801]

    // var output = [0,0,0,0];
    var output = [0,0,0,0,0] //7

    // function customRound(num) {
    //     return (num >= 0.7) ? 1 : 0;
    // }

    for (i = 0; i < 5; i++) {
        // console.log("Hidden", hidden)
        // console.log("Weights2", weights2[i])
        for (j = 0; j < hidden.length; j++) {
            console.log("Hidden", hidden[j])
            // console.log("Weights2", weights2[i*3+j])
            // console.log(output[i])
            output[i] = hidden[j] * weights2[i];
        }
        console.log("output b", output)
        output[i] = output[i] + bias2[0];
        console.log("output c", output)
        output[i] = 1/(1 + Math.pow(Math.E, -output[i]))
        console.log("output d", output)
        // output[i] = Math.round(output[i]);
        // if (i === 0 && output[i] === 1) {
        //     output[1] = 0;
        // } else if (i === 1 && output[i] === 1) {
        //     output[0] = 0;
        // }
        // output[i] = customRound(1/(1 + Math.pow(Math.E, -output[i])));
        console.log("output", output)
    }

    if (output[0] < output[1]) {
        output[0] = 0;
    } else {
        output[1] = 0;
    }
    if (output[2] < output[3]) {
        output[2] = 0;
    } else {
        output[3] = 0;
    }
    for (i = 0; i < 5; i++) {
        output[i] = Math.round(output[i]);
    }
    // output[0] = 0;
    // output[1] = 0;
    // output[2] = 1;
    // output[3] = 0;
    // output[3] = 1;
    response.turnLeft = output[0];
    response.turnRight = output[1];
    response.goForward = output[2];
    response.goBack = output[3];
    response.shoot = output[4];

    self.postMessage(response);
    // console.log(response)

}

x(e);