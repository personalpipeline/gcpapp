import streamlit as st
from google.cloud import language_v1

# Initialize the Natural Language client using ADC
client = language_v1.LanguageServiceClient()
project_id = "emotionapp-456405"  # Your GCP project ID

def analyze_sentiment(text):
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    response = client.analyze_sentiment(request={"document": document})
    return response.document_sentiment

def map_sentiment_to_emotion(sentiment):
    score = sentiment.score
    magnitude = sentiment.magnitude

    if score >= 0.5 and magnitude > 0.1:
        return "Positive"
    elif score <= -0.5 and magnitude > 0.1:
        return "Negative"
    elif -0.2 <= score <= 0.2 and magnitude <= 0.5:
        return "Neutral"
    elif score > 0.2 and score < 0.5 and magnitude > 0.1:
        return "Mildly Positive"
    elif score < -0.2 and score > -0.5 and magnitude > 0.1:
        return "Mildly Negative"
    else:
        return "Uncertain"

st.title("Simple Emotion Detector")

user_input = st.text_area("Enter your sentence here:")

if st.button("Detect Emotion"):
    if user_input:
        sentiment = analyze_sentiment(user_input)
        emotion = map_sentiment_to_emotion(sentiment)
        st.subheader("Analysis Result:")
        st.write(f"Detected Emotion: **{emotion}**")
        st.write(f"Sentiment Score: {sentiment.score}")
        st.write(f"Sentiment Magnitude: {sentiment.magnitude}")
    else:
        st.warning("Please enter some text.")

# Basic error handling with page refresh (Streamlit's way)
if "error" in st.session_state and st.session_state["error"]:
    st.error("An error occurred. The page will refresh in a few seconds.")
    import time
    time.sleep(3)
    st.session_state["error"] = False
    st.rerun()

# Example of how an error might be triggered (for demonstration)
# if st.button("Trigger Error (for testing refresh)"):
#     st.session_state["error"] = True
#     st.rerun()