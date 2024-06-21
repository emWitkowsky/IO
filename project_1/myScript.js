function(e) {
    var response = {};

    let enemy = e.data.enemyTank;
    let me = e.data.myTank;

    if (e.data.currentGameTime>20000) {
        // response.cannonLeft = 1;
        // response.goForward = 1;
        if (me.x < 250.0) {
            response.go
        }
    } else {
        response.cannonRight = 1;
        response.goBack = 1;
    }
    if(me.shootCooldown == 0) {
        response.shoot = 1;
    }

    self.postMessage(response);
}
