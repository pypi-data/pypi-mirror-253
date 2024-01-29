// The `Streamlit` object exists because our html file includes
// `streamlit-component-lib.js`.
// If you get an error about "Streamlit" not being defined, that
// means you're missing that file.

function sendValue(value) {
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


    getGeolocation();

    button_sensor = document.getElementById("button");
    button_sensor.addEventListener("click", onClick);

    window.rendered = true
  }
}


function getGeolocation() {
  const watchId = navigator.geolocation.watchPosition(successCallback, errorCallback);
}
function successCallback(position) {
  const latitude = position.coords.latitude;
  const longitude = position.coords.longitude;

  // Do something with the updated geolocation data
  console.log("Updated Geolocation:", { latitude, longitude });
  // You can send the updated values to Streamlit or perform other actions here
  sendValue({ latitude, longitude });
}
function errorCallback(error) {
  console.error("Error:", error);
}


function handleOrientation(event) {
  console.log("Orientation event");

  heading = event.alpha; 
  console.log("Heading:", heading);
  label_sensor = document.getElementById("sensor");
  label_sensor.innerHTML = "Heading: " + heading;

}


function onClick() {
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
}

// Render the component whenever python send a "render event"
Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
// Tell Streamlit that the component is ready to receive events
Streamlit.setComponentReady()
// Render with the correct height, if this is a fixed-height component
Streamlit.setFrameHeight(100)
