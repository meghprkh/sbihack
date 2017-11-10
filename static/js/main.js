var uid;
var camera = new JpegCamera("#camera").ready(function () {

window.setInterval(function() {
  var snapshot = camera.capture();
  snapshot.upload({ api_url: '/upload' })
          .done(function (data) {
            data = JSON.parse(data)
            if (!data.success) $.get('/start_auth/' + uid)
            if (data.success && data.done) {
              alert('Authenticated!')
            }
          })
}, 500)

});

window.onload = function () {
  uid = prompt('UID')
  $.get('/start_auth/' + uid)
}
