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
   

    // startUpdates(750);
    getGeolocation2();
    // Update heading using getHeading function


    window.rendered = true
  }
}


function startUpdates(interval) {
  // Set up a periodic update using setInterval
  setInterval(fetchData, interval);
}

async function fetchData() {
  try {
    // Get Device Orientation
    // Get Device Position
    let latitude = null;
    let longitude = null;
    let heading = 0;

    // Update latitude and longitude using getGeolocation function
    var position = await getGeolocation();
    latitude = position.latitude;
    longitude = position.longitude;

    // Update heading using getHeading function
    heading = await getHeading();

    // Now, you can log and send the values
    console.log(latitude, longitude, heading);
    sendValue({ latitude, longitude, heading});

  } catch (error) {
    console.error("Error:", error);
  }
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


function getGeolocation() {
  return new Promise((resolve, reject) => {
      if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(
              (position) => {
                  const latitude = position.coords.latitude;
                  const longitude = position.coords.longitude;
                  resolve({ latitude, longitude });
              },
              (error) => {
                  reject(error);
              }
          );
      } else {
          reject(new Error("Geolocation is not supported by this browser."));
      }
  });
}

function getHeading() {
  return new Promise((resolve, reject) => {
      if (window.DeviceOrientationEvent) {
          window.addEventListener(
              "deviceorientation",
              (event) => {
                  const heading = event.webkitCompassHeading;
                  resolve(heading);
              },
              true
          );
      } else {
          reject(new Error("Device orientation is not supported by this browser."));
      }
  });
}


function handleOrientation(event) {
  let alpha = event.alpha
  let beta = event.beta
  let gamma = event.gamma

  console.log(alpha, beta, gamma)
  let label = document.getElementById("coords");
  label.innerHTML = `alpha: ${alpha}, beta: ${beta}, gamma: ${gamma}`;
  sendValue({alpha, beta, gamma});s
  window.removeEventListener('deviceorientation', handleOrientation);
  window.orientationEventListenerAdded = false;
}

function onClick() {
  // feature detect
  if (typeof DeviceOrientationEvent.requestPermission === 'function') {
    DeviceOrientationEvent.requestPermission()
      .then(permissionState => {
        if (permissionState === 'granted') {
          if (!window.orientationEventListenerAdded) {
            window.addEventListener('deviceorientation', handleOrientation);
            window.orientationEventListenerAdded = true;
          }
          else{
            sendValue("already added");
          }
        }
      })
      .catch(console.error);
  } else {
    sendValue("not iOS / Wrong IOS version");
    console.log("not iOS / Wrong IOS version");
  }
}

async function requestDeviceOrientation() {
  if (typeof DeviceOrientationEvent !== 'undefined' && typeof DeviceOrientationEvent.requestPermission === 'function') {
    //iOS 13+ devices
    try {
      const permissionState = await DeviceOrientationEvent.requestPermission()
      if (permissionState === 'granted') {
        window.addEventListener('deviceorientation', handleOrientation)
      } else {
        alert('Permission was denied')
      }
    } catch (error) {
      alert(error)
    }
  } else if ('DeviceOrientationEvent' in window) {
    //non iOS 13+ devices
    console.log("not iOS");
    window.addEventListener('deviceorientation', handleOrientation)
  } else {
    //not supported
    alert('Not supported')
  }
}


// Render the component whenever python send a "render event"
Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
// Tell Streamlit that the component is ready to receive events
Streamlit.setComponentReady()
// Render with the correct height, if this is a fixed-height component
Streamlit.setFrameHeight(100)
