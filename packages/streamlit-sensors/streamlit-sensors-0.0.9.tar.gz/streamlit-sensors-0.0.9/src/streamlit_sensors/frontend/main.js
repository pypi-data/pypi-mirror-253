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
    // You most likely want to get the data passed in like this
    var { height, width } = event.detail.args;
           
    let video = document.getElementById('video');
    let canvas = document.getElementById('canvas');
    let button = document.getElementById("button_id");


    video.setAttribute('width', '100%');
    video.setAttribute('height', 'auto');

    const constraints =  { facingMode: 'environment', advanced : [{focusMode: "continuous"}]};
    
    navigator.permissions.query({ name: 'camera' })
      .then(permissionStatus => {
        if (permissionStatus.state === 'granted') {
          initializeCamera();
        } else {
          console.log('Camera permission denied.');
        }
      })
      .catch(err => {
        console.error('Error checking camera permission:', err);
      });
    
    function initializeCamera() {
      const constraints = { facingMode: 'environment', advanced: [{ focusMode: 'continuous' }] };
      navigator.mediaDevices.getUserMedia({ video: constraints })
        .then(function (stream) {
          video.srcObject = stream;
          video.play();
        })
        .catch(function (err) {
          console.log("An error occurred: " + err);
        });
    }

    function takePicture() {
      let context = canvas.getContext('2d');
      width = video.srcObject.getVideoTracks()[0].getSettings().width;
      height = video.srcObject.getVideoTracks()[0].getSettings().height;
      canvas.width = width;
      canvas.height = height;
      context.drawImage(video, 0, 0, width, height);      
      var data = canvas.toDataURL('image/png');
      sendValue(data);
    }      
      
      Streamlit.setFrameHeight(height);

    button.addEventListener("touchstart", onClick);
    video.addEventListener('touchstart', takePicture);

    // function updateButton() {

    //   // navigator.geolocation.getCurrentPosition((position) => {
    //   //   let latitude = position.coords.latitude;
    //   //   let longitude = position.coords.longitude;
    //   //   sendValue({latitude, longitude});
    //   // })
      
    //   requestDeviceOrientation()
    //   sendValue(handleOrientation(event))
        
    //   }

    window.rendered = true
  }
}

function handleOrientation(event) {
  let alpha = event.alpha
  let beta = event.beta
  let gamma = event.gamma

  console.log(alpha, beta, gamma)
  let label = document.getElementById("coords");
  label.innerHTML = `alpha: ${alpha}, beta: ${beta}, gamma: ${gamma}`;
  sendValue({alpha, beta, gamma});
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
