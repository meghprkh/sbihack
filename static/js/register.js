var camera = new JpegCamera("#camera");

function register() {
  var snapshot = camera.capture();
  snapshot.upload({ api_url: '/register_face' })
}

window.onload = function() {
  var uid = prompt('UID')
  var pwd = prompt('Password')
  $.post('/start_register/', {
    uid: uid,
    pwd: pwd
  })
}
