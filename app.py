import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import re

st.set_page_config(page_title="AI Myanmar Studio", layout="wide")
st.title("AI MYANMAR STUDIO PRO 🚀")

url = st.text_input("YouTube Video/Shorts Link ကို ဒီမှာ ထည့်ပါ:")

if st.button("Generate AI Content"):
    if url:
        try:
            video_id = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url).group(1)
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            full_text = " ".join([t['text'] for t in transcript])
            
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Original English Script")
                st.write(full_text)
            
            with col2:
                st.subheader("Facebook/TikTok Post Idea")
                st.info(f"Summary: {full_text[:200]}... #AI_Myanmar")
                
        except Exception as e:
            st.error("ဒီ Video မှာ Script မရှိလို့ မရနိုင်ပါဘူး ဘရို။")
    else:
        st.warning("Link ထည့်ပါဦး!")
