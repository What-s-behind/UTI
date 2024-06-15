import streamlit as st
from st_pages import add_page_title

add_page_title()


# Let's add some info about the app to the sidebar.
st.sidebar.write(
    """
    App created by AIO_Explorer
    """
)

st.markdown("""

    The project is actively developed. If you guys have any questions or want to develop the project with me, please, do be hesitate to contact us via:
            
| Team Member | Email | LinkedIn Profile |
|---|---|---|
| Lê Đức Minh | deutschlernen2303@gmail.com | https://www.linkedin.com/in/minh-le-duc-a62863172/ |
| Lê Nguyễn Đăng Khoa | khoale.maiu@gmail.com | https://www.linkedin.com/in/khoale-maiu/ |
| Trần Ngọc Đại | ngocdai101004@gmail.com | https://www.linkedin.com/in/ngoc-dai-tran-621b62292/ |
| Minh Mẫn | phamminhman1312005@gmail.com | https://www.linkedin.com/in/m%E1%BA%ABn-ph%E1%BA%A1m-47b493311/ | 
""")