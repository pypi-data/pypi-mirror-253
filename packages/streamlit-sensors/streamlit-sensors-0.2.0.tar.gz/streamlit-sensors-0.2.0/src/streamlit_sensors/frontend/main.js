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

  sendValue({ latitude, longitude, heading });
}


function startSensors() {

  if (typeof DeviceMotionEvent.requestPermission === 'function') {
    // Handle iOS 13+ devices.
    DeviceMotionEvent.requestPermission()
      .then((state) => {
        if (state === 'granted') {
          window.addEventListener('deviceorientation', handleOrientation);
        } else {
          console.error('Request to access the orientation was rejected');
        }
      })
      .catch(console.error);
  } else {
    // Handle regular non iOS 13+ devices.
    window.addEventListener('deviceorientation', handleOrientation);
  }

  navigator.geolocation.watchPosition(successCallback, errorCallback);

  document.getElementById("button").disabled = true;

}

// Render the component whenever python send a "render event"
Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
// Tell Streamlit that the component is ready to receive events
Streamlit.setComponentReady()
// Render with the correct height, if this is a fixed-height component
Streamlit.setFrameHeight(100)
