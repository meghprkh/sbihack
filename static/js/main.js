var uid;
var uploaded = true;
var camera = new JpegCamera("#camera").ready(function () {

var int = window.setInterval(function() {
  if (!uploaded) return;
  uploaded = false;
  var snapshot = camera.capture();
  snapshot.upload({ api_url: '/upload' })
          .done(function (data) {
            uploaded = true;
            data = JSON.parse(data)
            if (!data.status) {
              console.log('abc')
              $.get('/start_auth/' + uid)
            }
            if (data.status && data.done) {
              alert('Authenticated!')
              window.clearInterval(int)
            }
          }).fail(function (err) {
            uploaded = true;
          })
}, 1000)

});

window.onload = function () {
  uid = prompt('UID')
  $.get('/start_auth/' + uid)
}
