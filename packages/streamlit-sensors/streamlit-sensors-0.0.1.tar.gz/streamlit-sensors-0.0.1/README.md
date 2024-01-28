# streamlit-sensors

Get geolocation and heading

## Installation instructions 

```sh
pip install streamlit-sensors
```

## Usage instructions

```python
import streamlit as st

from streamlit_sensors import streamlit_sensors

value = streamlit_sensors()

st.write(value)
