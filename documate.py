import streamlit as st
import google.generativeai as genai 

api_key = ""
genai.configure(api_key=api_key)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

def add_comments_with_spinner(code):
    """Fetches comments from Gemini AI and displays a spinner during processing.

    This function simulates fetching comments from Gemini AI. You'll need
    to replace this logic with the actual API call to Gemini AI.

    Args:
        code: The code snippet to be commented.

    Returns:
        The commented code snippet (placeholder for now).
    """
    with st.spinner('Adding comments to your code...'):
        prompt = f"add comments to following code snippet: {code}"

        response = genai.generate_text(prompt=prompt)

        # Replace this with your actual Gemini AI API call
        # time.sleep(5)  # Simulate processing time (adjust as needed)
        # commented_code = process_code_with_gemini_ai(code)
        commented_code = response  # Placeholder

    return commented_code

def main():
    st.title("DocuMate")

    # Create two columns for side-by-side layout
    col1, col2 = st.columns(2)

    # Input area in the first column
    with col1:
        code_input = st.text_area("Enter your Python code snippet:", placeholder="Enter your Python code snippet:", height= 400, label_visibility="collapsed")

        if st.button("Add Comments"):
            with col2:
                    commented_code = add_comments_with_spinner(code_input)
                    # with st.container(height=400, border=None):
                    st.markdown(commented_code.result)
    # Comment display in the second column


if __name__ == "__main__":
    main()
