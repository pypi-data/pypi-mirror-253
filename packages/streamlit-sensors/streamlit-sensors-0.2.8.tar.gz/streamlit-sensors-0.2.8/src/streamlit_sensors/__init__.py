from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components


# Tell streamlit that there is a component called streamlit_sensors,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
	"streamlit_sensors", path=str(frontend_dir)
)

# Create the python function that will be called
def streamlit_sensors(
    key: Optional[str] = None,
):
    """
    Add a descriptive docstring
    """
    component_value = _component_func(
        key=key,
    )

    return component_value


st.set_page_config(
    page_title="Streamlit Sensors",
    page_icon=":compass:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

def main():
    st.write("## Example")


    value = streamlit_sensors()
    if value is not None and "image_data" in value and value["image_data"] is not None and value["image_data"] != 0:
        st.write(value)

        image = value["image_data"]
        st.image(image, use_column_width=True)


if __name__ == "__main__":
    main()
