(function() {

  var btnToggleLight = document.getElementById('light-toggle'),

      connection,

      toggleLed = function() {
        var isOn = btnToggleLight.className === 'on',

            sendRequest = function(url) {
              var xmlhttp = new XMLHttpRequest();
              xmlhttp.open('GET', url, true);
              xmlhttp.send();
            };

        if (isOn) {
          btnToggleLight.className = 'off';
          btnToggleLight.innerHTML = 'EIN';
          sendRequest('off');
        } else {
          btnToggleLight.className = 'on';
          btnToggleLight.innerHTML = 'AUS';
          sendRequest('on');
        }
      },

      initWebsocket = function() {
        // TODO make URL relative
        connection = new WebSocket("ws://musk.local:8080/ws");

        connection.onerror = function (error) {
          // TODO UI alert
          console.log(error);
        };

        connection.onmessage = function (e) {
          // TODO server will send distance readings - handle!
          console.log(e.data);
        };
      },

      initHeadingControl = function() {
        var steering = jQuery('.slider').roundSlider({
          sliderType: 'default',
          circleShape: 'quarter-top-left',
          showTooltip: false,
          handleShape: 'round',
          handleSize: 48,
          width: 4,
          radius: 250,
          value: 50,
        });

        steering.on('drag', function(e) {
          var angle = (e.value - 50) * 1.8;
          connection.send('heading=' + e.value);
        });

        steering.on('stop', function(e) {
          steering.roundSlider('setValue', 50);
          connectoin.send('heading=50');
        });
      };

  btnToggleLight.onclick = toggleLight;

  initHeadingControl();
  initWebsocket();
})();
