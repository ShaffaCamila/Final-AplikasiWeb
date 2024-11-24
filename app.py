import streamlit as st
from streamlit_option_menu import option_menu
import base64
import plotly.express as px
from source.home import home
from source.classification import show_animal_dashboard
from source.quiz import quiz
from source.about import about

st.set_page_config(
    page_title="Binatopedia Animal Classification",
    page_icon="./asset/logo.svg",
    layout="centered"
)


def add_local_background(image_path):
    # Read the image file and encode it as Base64
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    # Embed the image in the CSS
    css = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    [data-testid="stHeader"] {{
    background-color: rgb(212, 246, 255);
    }}

    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Add the background
add_local_background("./asset/pagebkg.png")



def main():
    st.markdown("""
        <style>
        body {{
            font-family: "Source Sans Pro", sans-serif;
        }}
        .css-1kyxreq {{
            justify-content: center !important;
        }}
        </style>
    """, unsafe_allow_html=True)

    selected = option_menu(
        None, 
        ['Home', 'Classification', 'Quiz', 'Tentang'],
        icons=['house', 'search', 'book', 'info-circle'],
        menu_icon='cast', 
        default_index=0, 
        orientation='horizontal',
        styles={
            "nav-link": {
                "font-size": "90%",  # Font size 
            }
        }
    )


    if selected == 'Home':
        home()
    elif selected == 'Classification':
        show_animal_dashboard()
    elif selected == 'Quiz':
        quiz()
    elif selected == 'About':
        about()

if __name__ == "__main__":
    main()