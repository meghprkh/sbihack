var camera = new JpegCamera("#camera");

window.setInterval(function() {
  var snapshot = camera.capture();
  snapshot.upload({ api_url: '/upload' })
}, 500)

window.onload = function() {
  var uid = prompt('UID')
  $.get('/start_auth/' + uid)
}
