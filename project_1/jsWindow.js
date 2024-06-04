function(e) {

    var response = {};
    let enemy = e.data.enemyTank;
    let me = e.data.myTank;

    var input = [me.x/500.0, me.y/500.0, me.rotation/360.0];

    var weights1 = [0,0,0,0,0,0,0,0,0];
    var bias1 = [0,0,0];

    var hidden = [0,0,0];

    var i,j;
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            hidden[i] = input[j] * weights1[i*3+j];
        }
        hidden[i] = hidden[i]+ bias1[i];
        hidden[i] = 1/(1 + Math.pow(Math.E, -hidden[i]));
    }

    var weights2 = [0,0,0,0,0,0,0,0,0,0,0,0];
    var bias2 = [0,0,0,0];

    var output = [0,0,0,0];

    for (i = 0; i < 4; i++) {
        for (j = 0; j < 3; j++) {
            output[i] = hidden[j] * weights2[i*3+j];
        }
        output[i] = output[i] + bias2[i];
        output[i] = 1/(1 + Math.pow(Math.E, -output[i]))
        output[i] = Math.round(output[i]);
    }

    response.turnLeft = output[0];
    response.turnRight = output[1];
    response.goForward = output[2];
    response.goBack = output[3];

    if(me.shootCooldown == 0) {
        response.shoot = 1;
    }

    self.postMessage(response);

}