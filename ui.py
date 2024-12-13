import streamlit as st

# Apply custom CSS for styling
st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif; 
        font-size: 22px;
        font-weight: 700;
        color: #091747;
    }
    .stTextInput > div:first-child {
        background-color: #ffffff;
        border: 1px solid #cccccc;
        border-radius: 5px;
        padding: 5px;
        color: black;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and description
st.title("Leig.ai 🧑‍⚕️🩺💊 ")
st.write("Faça perguntas sobre a história do curso de medicina da UFPel!")

# Input box for the question
question = st.text_input(
    "### Insira aqui sua pergunta:", placeholder="Digite sua pergunta aqui..."
)

# Button to submit the question
if st.button("Enviar"):
    if question.strip():
        # Placeholder for RAG model integration
        # You should replace the following line with the actual call to your RAG model
        answer = f"This is a mock response to the question: '{question}'"

        # Display the answer
        st.markdown("### Resposta:")
        st.write(answer)
    else:
        st.warning("Faça uma pergunta!.")

# Space for the answer
else:
    st.markdown("### Resposta:")
    st.write("Sua resposta aparecerá aqui....")
