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

    requestPosition();
    getGeolocation2();

    window.rendered = true
  }
}

function requestPosition() {
  navigator.geolocation.getCurrentPosition(
    (position) => {
      const latitude = position.coords.latitude;
      const longitude = position.coords.longitude;
      console.log("Requested Geolocation:", { latitude, longitude });
    },
    (error) => {
      console.error("Error requesting geolocation:", error);
    }
  );
}


function getGeolocation2() {
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


function getHeading() {
  window.addEventListener('deviceorientation', handleOrientation, true);
}

function handleOrientation(event) {
  console.log("Orientation event");
  console.log(event);
  // Extract heading information from the event and send it to Streamlit
  const heading = event.alpha || 0; // alpha is the compass direction (0 to 360 degrees)
  console.log("Heading:", heading);
  // Note: You may need to convert the heading value based on your requirements
}





// Render the component whenever python send a "render event"
Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
// Tell Streamlit that the component is ready to receive events
Streamlit.setComponentReady()
// Render with the correct height, if this is a fixed-height component
Streamlit.setFrameHeight(100)
