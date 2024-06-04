function(e) {

    var response = {};
    var enemy = e.data.enemyTank;
    var me = e.data.myTank;

    var input = [me.x/500.0, me.y/500.0, me.rotation/360.0];

    var weights1 = [[0.469707190990448, 0.015171557664871216, -1.0566596984863281, -0.03467557579278946], [-0.26583370566368103, -0.05403166264295578, 0.828546941280365, -0.13687510788440704], [-0.14759941399097443, 0.22920820116996765, 0.1436581313610077, -0.33593568205833435], [0.12857216596603394, -0.39240580797195435, 0.2858048677444458, 0.3360889256000519], [-0.33789029717445374, -0.024244673550128937, 0.7948184609413147, -0.17035016417503357], [-0.1365824192762375, -0.08542539179325104, -0.5259692668914795, 0.15220661461353302]]
    var bias1 = [1.0032048225402832, -0.322238028049469, 1.5959007740020752, -0.290200799703598];

    var hidden = [0,0,0];

    var i,j;
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            hidden[i] = input[j] * weights1[i*3+j];
        }
        hidden[i] = hidden[i] + bias1[i];
        hidden[i] = 1/(1 + Math.pow(Math.E, -hidden[i]));
    }

    var weights2 = [[2.0227553844451904], [-0.23896346986293793], [0.9771156311035156], [-0.30267131328582764]];
    var bias2 = [0.8896425366401672];

    var output = [0,0,0,0];

    for (i = 0; i < 4; i++) {
        for (j = 0; j < 3; j++) {
            output[i] = hidden[j] * weights2[i*3+j];
        }
        output[i] = output[i] + bias2[i];
        output[i] = 1/(1 + Math.pow(Math.E, -output[i]))
        output[i] = Math.round(output[i]);
    }

    // output[2] = 1;
    // output[3] = 1;
    response.turnLeft = output[0];
    response.turnRight = output[1];
    response.goForward = output[2];
    response.goBack = output[3];

    self.postMessage(response);

}

