import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Fetch news data
def fetch_news():
    api_key = "6b84c4256d1b4adb9c6a3cfe369f03cc"
    url = f"https://newsapi.org/v2/everything?q=bitcoin&apiKey={api_key}"
    response = requests.get(url)
    return response.json()

def display_news(index, articles):
    article = articles[index]
    
    st.image(article["urlToImage"] or 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg', width=700)
    st.title(article["title"])
    st.write(article["description"])
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if index > 0:
            if st.button("Prev"):
                st.session_state.index = index - 1
    
    with col2:
        if st.button("Read More"):
            st.write(f"[Read More]({article['url']})")

    with col3:
        if index < len(articles) - 1:
            if st.button("Next"):
                st.session_state.index = index + 1

def main():
    st.title("QuickNews")
    
    if 'index' not in st.session_state:
        st.session_state.index = 0
    
    data = fetch_news()
    articles = data.get("articles", [])
    
    if articles:
        display_news(st.session_state.index, articles)
    else:
        st.write("No news available")

if __name__ == "__main__":
    main()
