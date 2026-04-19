import streamlit as st

# 1. Page Configuration (Must be the first Streamlit command)
st.set_page_config(layout="wide", page_title="FitSync Dashboard", page_icon="⚡")

# 2. Session State for Theme Toggle
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True # Default to Dark Mode

def toggle_theme():
    st.session_state.dark_mode = not st.session_state.dark_mode

# 3. Dynamic Design Variables based on Theme
if st.session_state.dark_mode:
    # Sleek dark mode gradients and card styling
    bg_gradient = "linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #000000)"
    sidebar_bg = "#111827" 
    text_color = "#ffffff"
    card_bg = "rgba(20, 20, 20, 0.4)"
    card_border = "rgba(255, 255, 255, 0.1)"
    hero_gradient = "-webkit-linear-gradient(45deg, #4ade80, #3b82f6)"
    btn_bg = "#374151" # Dark button background
    btn_text = "#ffffff" # Light button text
else:
    # Vibrant light mode gradients and card styling
    bg_gradient = "linear-gradient(-45deg, #fbc2eb, #a6c1ee, #fbc2eb, #e0c3fc)"
    sidebar_bg = "#ffffff" 
    text_color = "#1f2937"
    card_bg = "rgba(255, 255, 255, 0.45)"
    card_border = "rgba(255, 255, 255, 0.6)"
    hero_gradient = "-webkit-linear-gradient(45deg, #ec4899, #8b5cf6)"
    btn_bg = "#f3f4f6" # Light button background
    btn_text = "#1f2937" # Dark button text

# 4. Inject Advanced Custom CSS
custom_css = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');

/* Main Background and Font Override */
[data-testid="stAppViewContainer"] {{
    background: {bg_gradient};
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    font-family: 'Poppins', sans-serif !important;
}}

/* Sidebar Background Override */
[data-testid="stSidebar"] {{
    background-color: {sidebar_bg} !important;
}}

/* Make Streamlit Header Transparent */
[data-testid="stHeader"] {{
    background: transparent !important;
}}

/* Global Text Colors */
h1, h2, h3, p, div, span {{
    color: {text_color} !important;
    font-family: 'Poppins', sans-serif !important;
}}

/* Streamlit Button Override */
div.stButton > button {{
    background-color: {btn_bg} !important;
    color: {btn_text} !important;
    border: 1px solid {card_border} !important;
    transition: all 0.3s ease;
}}
div.stButton > button * {{
    color: {btn_text} !important;
}}
div.stButton > button:hover {{
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}}

/* Background Animation Keyframes */
@keyframes gradientBG {{
    0% {{ background-position: 0% 50%; }}
    50% {{ background-position: 100% 50%; }}
    100% {{ background-position: 0% 50%; }}
}}

/* Hero Section Styling */
.hero-text {{
    font-size: 4.5rem;
    font-weight: 800;
    background: {hero_gradient};
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-bottom: -10px;
    padding-top: 2rem;
}}

.sub-hero {{
    text-align: center;
    font-size: 1.4rem;
    font-weight: 300;
    opacity: 0.85;
    margin-bottom: 50px;
}}

/* Glassmorphism Metric Cards */
.glass-card {{
    background: {card_bg};
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-radius: 20px;
    border: 1px solid {card_border};
    padding: 30px 20px;
    text-align: center;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.15);
    transition: all 0.3s ease;
}}

.glass-card:hover {{
    transform: translateY(-8px);
    box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.25);
}}

.metric-label {{
    font-size: 1.1rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-weight: 600;
    opacity: 0.8;
}}

.metric-value {{
    font-size: 3.5rem;
    font-weight: 800;
    margin: 10px 0;
}}

.metric-trend-up {{ color: #4ade80 !important; font-weight: 600; font-size: 1.1rem; }}
.metric-trend-down {{ color: #f87171 !important; font-weight: 600; font-size: 1.1rem; }}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 5. Sidebar Options
st.sidebar.markdown("### ⚙️ Dashboard Settings")
st.sidebar.button("🌓 Switch Theme", on_click=toggle_theme, use_container_width=True)
st.sidebar.markdown("---")
st.sidebar.info("Navigate through the app using the menu above.")

# 6. Main UI Layout
# Hero Section
st.markdown('<h1 class="hero-text">FitSync</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-hero">Your intelligent, aesthetic health analytics platform.</p>', unsafe_allow_html=True)

# Glassmorphism Metric Cards Section
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f'''
    <div class="glass-card">
        <div class="metric-label">👟 Daily Steps</div>
        <div class="metric-value">12,450</div>
        <div class="metric-trend-up">↑ 12% vs yesterday</div>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown(f'''
    <div class="glass-card">
        <div class="metric-label">🔥 Calories Burned</div>
        <div class="metric-value">2,140</div>
        <div class="metric-trend-up">↑ 5% vs yesterday</div>
    </div>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown(f'''
    <div class="glass-card">
        <div class="metric-label">⏱️ Active Minutes</div>
        <div class="metric-value">84</div>
        <div class="metric-trend-down">↓ 2% vs yesterday</div>
    </div>
    ''', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Additional Information Section
with st.container():
    st.markdown("### 🚀 Quick Insights")
    st.markdown("""
    * **Activity Spike:** You were most active between 5:00 PM and 6:30 PM today.
    * **Recovery Mode:** Based on your heart rate variability, consider a lighter workout tomorrow.
    * **Goal Progress:** You are currently on track to hit your weekly step goal by Thursday!
    """)