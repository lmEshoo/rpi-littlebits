var GPIO = require('onoff').Gpio,
led = new GPIO(17, 'out');

setInterval(function() {
  var state = led.readSync();
  led.writeSync(Number(!state));
}, 1000);
