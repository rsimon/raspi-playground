(function() {
  var btnToggleLed = document.getElementById('led-toggle'),
      btnLeft = document.getElementById('servo-left'),
      btnRight = document.getElementById('servo-right'),

      sendRequest = function(url) {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.open('GET', url, true);
        xmlhttp.send();
      },

      toggleLed = function() {
        var isOn = btnToggleLed.className === 'on';
        if (isOn) {
          btnToggleLed.className = 'off';
          btnToggleLed.innerHTML = 'EIN';
          sendRequest('off');
        } else {
          btnToggleLed.className = 'on';
          btnToggleLed.innerHTML = 'AUS';
          sendRequest('on');
        }
      },

      onLeft = function() {
        sendRequest('left');
      },

      onRight = function() {
        sendRequest('right');
      },

      initWebsocket = function() {

        console.log('start');

        var connection = new WebSocket("ws://localhost:8080/ws");

        // When the connection is open, send some data to the server
        connection.onopen = function () {
          console.log('sending ping');
          connection.send('Ping'); // Send the message 'Ping' to the server
        };

        // Log errors
        connection.onerror = function (error) {
          console.log(error);
        };

        // Log messages from the server
        connection.onmessage = function (e) {
          console.log('Server: ' + e.data);
        };
      };

  initWebsocket();

  btnToggleLed.onclick = toggleLed;
  btnLeft.onclick = onLeft;
  btnRight.onclick = onRight;

})();
