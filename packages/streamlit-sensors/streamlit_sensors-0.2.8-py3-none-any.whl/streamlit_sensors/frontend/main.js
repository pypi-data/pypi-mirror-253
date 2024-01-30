// The `Streamlit` object exists because our html file includes
// `streamlit-component-lib.js`.
// If you get an error about "Streamlit" not being defined, that
// means you're missing that file.

function sendValue(value) {
  // console.log("Sending value to Python", value)
  Streamlit.setComponentValue(value)
}

/**
 * The component's render function. This will be called immediately after
 * the component is initially loaded, and then again every time the
 * component gets new data from Python.
 */
function onRender(event) {
  // Only run the render code the first time the component is loaded.
  if (!window.rendered) {

    button_sensor = document.getElementById("button");
    button_sensor.addEventListener("click", startSensors);

    window.rendered = true
  }
}

var latitude = 0;
var longitude = 0;
var heading = 0;
var image_data = 0;
var started = false;
const streaming = false;

function successCallback(position) {
  latitude = position.coords.latitude;
  longitude = position.coords.longitude;

  latitude_label = document.getElementById("latitude");
  latitude_label.innerHTML = "Latitude: " + latitude;

  longitude_label = document.getElementById("longitude");
  longitude_label.innerHTML = "Longitude: " + longitude;
}
function errorCallback(error) {
  console.error("Error:", error);
}


function handleOrientation(event) {

  heading = event.alpha; 
  label_sensor = document.getElementById("heading");
  label_sensor.innerHTML = "Heading: " + heading;
  window.removeEventListener('deviceorientation', handleOrientation);

}

function requestLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      function (position) {
        successCallback(position);
      },
      function (error) {
        errorCallback(error);
      }
    );
  } else {
    console.error("Geolocation is not supported by this browser.");
  }
}


function getVideo(){

  if ('mediaDevices' in navigator && 'getUserMedia' in navigator.mediaDevices) {
  
    navigator.mediaDevices.getUserMedia({
      video: {
        width: {
          min: 600
        },
        height: {
          min: 400
        },
        facingMode: 'environment'
      }
    })

    .then(function(stream) {

      var video = document.getElementById('video');
      video.srcObject = stream;

      video.onloadedmetadata = function (e) {
        video.play();
      };

      video.addEventListener(
        "canplay",
        (ev) => {
          if (!streaming) {
            height = (video.videoHeight / video.videoWidth) * width;
      
            video.setAttribute("width", width);
            video.setAttribute("height", height);
            canvas.setAttribute("width", width);
            canvas.setAttribute("height", height);
            streaming = true;
          }
        },
        false,
      );

      // Add click event listener to the video element
      video.addEventListener('click', function () {
        takePicture(video);
      });

    })

  }
}

function takePicture(video) {
  // Create a canvas element to capture the video stream
  var canvas = document.createElement('canvas');
  var context = canvas.getContext('2d');

  // Set the canvas dimensions to match the video stream
  canvas.width = video.videoWidth/8;
  canvas.height = video.videoHeight/8;

  // Capture a frame from the video stream without drawing it on the canvas
  context.drawImage(video, 0, 0, canvas.width, canvas.height);
  image_data = canvas.toDataURL('image/png');

  console.log(image_data);
  sendValue({ latitude, longitude, heading, image_data});
}

function startSensors() {

  getVideo();
  requestLocation();
  navigator.geolocation.watchPosition(successCallback, errorCallback);

  if (typeof DeviceMotionEvent.requestPermission === 'function') {
    // Handle iOS 13+ devices.
    if (started === false) { 
      DeviceMotionEvent.requestPermission()
        .then((state) => {
          if (state === 'granted') {
            window.addEventListener('deviceorientation', handleOrientation);
            started = true;
          } else {
            console.error('Request to access the orientation was rejected');
          }
        })
        .catch(console.error);
    } else {
      window.addEventListener('deviceorientation', handleOrientation);
    }

  } else {
    // Handle regular non iOS 13+ devices.
    window.addEventListener('deviceorientation', handleOrientation);
    started = true;
  }

  document.getElementById("button").disabled = true;

}



// Render the component whenever python send a "render event"
Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
// Tell Streamlit that the component is ready to receive events
Streamlit.setComponentReady()
// Render with the correct height, if this is a fixed-height component
Streamlit.setFrameHeight(500)
