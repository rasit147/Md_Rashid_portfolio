import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Md Rashid", page_icon="🎓")

#Background
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://png.pngtree.com/thumb_back/fh260/background/20221014/pngtree-gradient-geometric-card-luxury-light-blue-orange-image_1467872.jpg");
        background-size: cover;
        color: black;  /* Text color changed to white for better visibility */
    }
    .custom-header {
        background-color: rgba(0, 0, 0, 0.7);  /* Semi-transparent background for text */
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Custom CSS for text size and spacing
st.markdown(
    """
    <style>
    .profile-pic {
        float: left;
        margin-right: 20px;
        border-radius: 50%;
    }
    .stApp {
        background-color: #f4f4f4;
    }
    h1 {
        font-size: 2.0em;  /* Larger font size for H1 */
    }
    h2, h3 {
        font-size: 1.6em;  /* Medium font size for H2 and H3 */
    }
    h5 {
        font-size: 1.3em;  /* Slightly larger font size for H5 */
    }
    p {
        font-size: 1.2em;  /* Larger paragraph text */
    }
    .project-section {
        margin-bottom: 40px;
    }
    .github-button {
        display: inline-block;
        padding: 10px 20px;
        font-size: 16px;
        color: red;
        background-color: #333;
        text-decoration: none;
        border-radius: 5px;
        text-align: center;
    }
    .github-button:hover {
        background-color: #444;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Portfolio Title and Profile Image
theme_image = Image.open('DIL_0037-01-01-removebg-preview.jpg')  # Replace with your image file name
st.image(theme_image, width=250, caption="Md Rashid", use_column_width=False)

# B.Tech info
st.markdown("<h5 style='text-align: left;'>B.Tech, Haldia Institute of Technology, 8.17 CGPA</h5>",<span style='color: red;'> unsafe_allow_html=True)

# Welcome Heading
st.markdown("<h1 style='text-align: center; color: #3498db;'>HI There 👋 </h1>", unsafe_allow_html=True)

# About Me Section
st.header("About Me")
st.markdown(
    """
    I am Md Rashid, a Computer Science graduate specializing in Data Science with expertise in Python, Java, and Problem Solving.
    Developed various projects in Data Science and Machine Learning, and built AI-driven web interfaces using Streamlit. 
    Solved 150+ programming challenges, showcasing strong problem-solving skills. Eager to apply hands-on
    experience to real-world projects and deliver impactful results in a tech-focused role.
    """
)

# Skills Section
st.header("Skills")
st.write("""
- 🐍 **Python**: Proficient in core programming concepts, data manipulation, exploratory data analysis (EDA), and building web-based applications using Python.
- 🖥️ **Java**: Strong in Object-Oriented Programming (OOP) and solving coding challenges.
- 📊 **Machine Learning**: Experienced in building supervised models like classification and regression for predictive analytics.
- 📉 **Statistics**: Strong understanding of statistical concepts such as hypothesis testing, probability, regression analysis, and data distribution.
- 🗃️ **DBMS**: Knowledgeable in database management systems, data modeling, and normalization techniques.
- 🗄️ **MySQL**: Skilled in relational database management, writing efficient queries, and working with **SQLAlchemy** to integrate Python with database objects.
- 📈 **Python Libraries**: Adept at creating insightful visualizations and Manipulation using **Matplotlib**, **Seaborn**, and **Pandas & Numpy**.
- ⚙️ **Tools**:  **MS Excel** for data management, familiar with **Streamlit** for building web applications, **GitHub** for version control, and **Jupyter Notebooks** for data exploration and analysis.
""")

# Projects Section
st.header("Projects")

# Project 1: Image Captioning and Sentiment Analysis
col1, col2 = st.columns(2)
with col1:
    st.subheader("1. Image Captioning & Sentiment Analysis using Hugging Face")
    st.write("""
    A project combining NLP and Computer Vision pre-trained model to generate image captions 
    and perform sentiment analysis by generating text descriptions from images using Hugging Face.
    Tools: **Python, Hugging Face pre-trained model, Streamlit for web interface**.
    """)
    st.write("[[Click for the Demo]](https://emotionn.streamlit.app/)")
    theme_image = Image.open('screen happy.png')  # Replace with your image file name
    st.image(theme_image, use_column_width=True)
    st.markdown(
        """
        <a href="https://github.com/rasit147/Image-to-text-detecting-analysing-sentiment" class="github-button" target="_blank">View on GitHub</a>
        """, unsafe_allow_html=True
    )

# Project 2: Movie Recommender System
with col2:
    st.subheader("2. Movie Recommender System")
    st.write("""
    Built a personalized movie recommendation system using collaborative filtering techniques recommend movies by user prefrences.
    Tools: **Python, Scikit-learn, cosine similarities, Pandas**.
    """)
    image_movie = Image.open('Moviedemoss.png')  # Replace with your image file name
    st.image(image_movie, use_column_width=True)
    st.markdown(
        """
        <a href="https://github.com/rasit147/Movie_Recommender" class="github-button" target="_blank">View on GitHub</a>
        """, unsafe_allow_html=True
    )

# Project 3: Potato Disease Classification
with col2:
    st.subheader("3. Potato Disease Classification")
    theme_image = Image.open('Screenshot (320).png')  # Replace with your image file name
    st.image(theme_image, use_column_width=True)
    st.write("""
    Developed a Deep Learning model for early disease detection in potato crops, 
    helping farmers minimize crop loss and optimize resources.
    """)
    st.markdown(
        """
        <a href="https://github.com/rasit147/Potato-Disease-Classification" class="github-button" target="_blank">View on GitHub</a>
        """, unsafe_allow_html=True
    )

# Project 4: Data Science Internship at Afame Technology
with col1:
    st.subheader("4. Data Science Internship at Afame Technology")
    theme_image = Image.open('Screenshot (382).png')  # Replace with your image file name
    st.image(theme_image, use_column_width=True)
    st.write("""
    Created a regression model to forecast sales based on historical data. Applied feature engineering 
    and model evaluation techniques during the internship.
    """)
    st.markdown("[View Certificate](https://drive.google.com/file/d/19A3JFOoS4kCEXPXyMtofn4FpGHRT_29D/view)")

# Contact Me Section
st.header("Contact Me")
st.write("I am actively looking for opportunities. Feel free to reach out to me:")
st.write("- 📧 Email: mdrashid1549@gmail.com")
st.write("- 📞 Phone: 9006597147")
st.write("- 🌐 [LinkedIn](https://www.linkedin.com/in/mdrashid1472/)")
st.write("- 🌐 [GitHub](https://github.com/rasit147)")

# Footer Section
st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #3498db;
            color: white;
            text-align: center;
            padding: 10px;
        }
    </style>
    <div class="footer">
        <p>Developed by Md Rashid | 2024</p>
    </div>
    """,
    unsafe_allow_html=True
)


