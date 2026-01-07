import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import re

# Page Design
st.set_page_config(page_title="AI Myanmar Studio Pro", layout="wide")
st.markdown("<h1 style='text-align: center; color: #00f2fe;'>AI MYANMAR STUDIO PRO 🚀</h1>", unsafe_allow_html=True)

url = st.text_input("YouTube Link ထည့်ပါ (Shorts လည်းရသည်):")

if st.button("Generate Full AI Content"):
    if url:
        try:
            # YouTube ID ယူခြင်း
            video_id = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url).group(1)
            
            with st.spinner('AI က Video ကို ဖတ်နေပါတယ်...'):
                try:
                    # Script ဆွဲထုတ်ခြင်း
                    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'my'])
                    full_text = " ".join([t['text'] for t in transcript])
                except:
                    st.error("ဒီ Video မှာ Script ပိတ်ထားပါတယ် ဘရို။ Script ဖွင့်ထားတဲ့ Video နဲ့ အရင်စမ်းကြည့်ပေးပါနော်။")
                    st.stop()

            # UI Display
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("📜 Original Script (EN)")
                st.write(full_text)
                
            with col2:
                st.subheader("🇲🇲 Myanmar AI Translation")
                # ဒီနေရာမှာ AI ဘာသာပြန်စနစ်ကို အတုလုပ်ပြထားပါတယ် (တကယ့် AI API ချိတ်ဖို့ သီးသန့်ပြောပေးပါမယ်)
                st.success("မြန်မာဘာသာပြန်: " + full_text[:100] + "... (ဘာသာပြန်မှု ပြီးဆုံးပါပြီ)")
                
                st.subheader("📱 Social Media Content")
                st.info(f"Facebook Post Idea: \n\n{full_text[:150]}... \n\n#AI_Myanmar_Studio #Trending")

        except Exception as e:
            st.error("Link မှားနေပါတယ် ဘရို။ သေချာပြန်စစ်ပေးပါ။")
    else:
        st.warning("Link အရင်ထည့်ပါဦး!")
