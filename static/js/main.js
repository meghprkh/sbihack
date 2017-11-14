var uid;
var camera = new JpegCamera("#camera").ready(function () {

var int = window.setInterval(function() {
  var snapshot = camera.capture();
  snapshot.upload({ api_url: '/upload' })
          .done(function (data) {
            data = JSON.parse(data)
            if (!data.status) {
              console.log('abc')
              $.get('/start_auth/' + uid)
            }
            if (data.status && data.done) {
              alert('Authenticated!')
              window.clearInterval(int)
            }
          })
}, 2000)

});

window.onload = function () {
  uid = prompt('UID')
  $.get('/start_auth/' + uid)
}
