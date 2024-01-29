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


def main():
    st.write("## Example")


    value = streamlit_sensors()
    st.write(value)

if __name__ == "__main__":
    main()
