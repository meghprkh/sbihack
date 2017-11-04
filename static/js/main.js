var camera = new JpegCamera("#camera");

window.setInterval(function() {
  var snapshot = camera.capture();
  snapshot.upload({ api_url: '/upload' })
}, 500)
