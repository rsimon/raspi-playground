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

      disableRubberbandScroll = function() {
        document.body.addEventListener('touchmove', function(e) {
          e.preventDefault();
        });
      },

      initWebsocket = function() {
        var loc = window.location,
            uri = 'ws://' + loc.host + ':' + loc.port + '/ws';

        connection = new WebSocket(uri);

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

  disableRubberbandScroll();

  btnToggleLight.onclick = toggleLight;

  initHeadingControl();
  initWebsocket();
})();
