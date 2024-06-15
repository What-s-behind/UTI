import streamlit as st
from st_pages import add_page_title

add_page_title()

st.sidebar.write(
    """
    App created by AIO_Explorer
    """
)

# ----- Main content -----
st.subheader("About team")
st.markdown(
"""
##  AIO_Explorer:  Unveiling Marketing Magic with GenAI

Meet AIO_Explorer, a team of passionate visionaries who are revolutionizing the world of marketing analysis using the power of Generative AI (GenAI). We believe in harnessing the potential of AI to extract profound insights from visual data, offering a fresh perspective on understanding consumer behavior and trends.

Our team comprises:

* **Minh Le** ([https://www.linkedin.com/in/minh-le-duc-a62863172/](https://www.linkedin.com/in/minh-le-duc-a62863172/)): A strategic thinker with a keen eye for detail, Minh brings his expertise in data analysis and innovative problem-solving to the forefront.
* **Khoa Le ([https://www.linkedin.com/in/khoale-maiu/](https://www.linkedin.com/in/khoale-maiu/)):** A creative mastermind with a deep understanding of marketing principles, Khoa crafts compelling narratives and drives the vision for our projects.
* **Ngoc Dai Tran ([https://www.linkedin.com/in/m%E1%BA%ABn-ph%E1%BA%A1m-47b493311/](https://www.linkedin.com/in/m%E1%BA%ABn-ph%E1%BA%A1m-47b493311/))** ([https://www.linkedin.com/in/ngoc-dai-tran-621b62292/](https://www.linkedin.com/in/ngoc-dai-tran-621b62292/)): An expert in visual communication and design, Ngoc Dai ensures that our insights are communicated clearly and effectively.
* **Man Pham:** A meticulous researcher with a passion for exploring the world of AI, Mân provides the foundation of knowledge and cutting-edge technology that fuels our explorations.

Together, we form a synergistic team dedicated to unlocking the hidden gems of marketing information contained within images. Our mission is to empower businesses with data-driven insights, enabling them to optimize campaigns, personalize experiences, and achieve impactful results. 

We invite you to join us on this exciting journey as we dive into the world of GenAI-powered marketing analysis. Let's explore, innovate, and transform the future of marketing together!
"""
)

st.subheader("More details")
st.markdown(
"""
    More details about project structure and results of experiments are disscussed in [the project's Github repo](https://github.com/What-s-behind/UTI.git.
"""
)