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
      };

  btnToggleLed.onclick = toggleLed;
  btnLeft.onclick = onLeft;
  btnRight.onclick = onRight;
  
})();
