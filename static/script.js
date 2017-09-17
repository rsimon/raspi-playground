(function() {
  var btnToggleLed = document.getElementById('led-toggle'),
      btnLeft = document.getElementById('servo-left'),
      btnRight = document.getElementById('servo-right'),

      connection,

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
        connection.send('left');
      },

      onRight = function() {
        connection.send('right');
      },

      initWebsocket = function() {

        console.log('start');

        connection = new WebSocket("ws://musk.local:8080/ws");

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

  jQuery('.slider').roundSlider({
    sliderType: "min-range",
    handleShape: "round",
    width: 22,
    radius: 100,
    value: 45
  });
  
})();
