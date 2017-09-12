(function() {
  var button = document.getElementById('led-toggle'),

      sendRequest = function(url) {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.open('GET', url, true);
        xmlhttp.send();
      },

      toggle = function() {
        var isOn = button.className === 'on';
        if (isOn) {
          button.className = 'off';
          button.innerHTML = 'ON';
          sendRequest('off');
        } else {
          button.className = 'on';
          button.innerHTML = 'OFF';
          sendRequest('on');
        }
      };

  button.onclick = toggle;
})();
