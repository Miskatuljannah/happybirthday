import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objs as go
from PIL import Image

# CSS Styling
st.markdown("""
    <style>
        * {
            font-family: 'Times New Roman', Times, serif !important;
        }
        body {
            background-color: #1c1c1c;
            color: white;
        }
        .title {
            text-align: center;
            font-size: 3em;
            color: white;
            padding: 20px 10px;
            margin-bottom: 20px;
        }
        .section {
            margin: 20px;
            text-align: center;
            font-size: 1.5em;
            color: white;
        }
        .footer {
            text-align: center;
            font-size: 1.2em;
            color: white;
            margin-top: 50px;
        }
        .image-style {
            border: 5px solid #FF69B4;
            border-radius: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            margin: 10px;
            padding: 5px;
            transition: transform 0.3s ease;
        }
        .image-style:hover {
            transform: scale(1.05);
        }
        @keyframes slideIn {
            from {
                transform: translateX(-100%);
            }
            to {
                transform: translateX(0);
            }
        }
        .move-image {
            animation: slideIn 1.5s ease-in-out;
        }
    </style>
""", unsafe_allow_html=True)

# Judul
st.markdown('<div class="title">🎉 Happy Birthday, My Love! 🎂</div>', unsafe_allow_html=True)

# Pilihan Halaman
page = st.radio("Pilih Konten yang ingin dilihat:", ("Teks", "Video", "Foto", "Grafik"))

if page == "Teks":
    st.markdown('<div class="section">To the most amazing boyfriend in the world! 💖</div>', unsafe_allow_html=True)
    st.markdown('<div class="section">I love you more than words can say! 💖</div>', unsafe_allow_html=True)

    st.markdown("""
        <div class="love-letter">
            <h3>My Dearest Love,</h3>
            <p>
                Happy Birthday Sayangg!!
                もしkazuが生まれてなかったら、私は本当の愛とか、こんなにも誰かを愛する気持ちを知らなかったと思う! 私が永遠を過ごしたいって本気で思える人で、運命の人だって信じてる. 誰かを1年以上も待てるなんて自分でも思わなかったけど、kazuなら全然待てる!kazuがいるってだけで、毎日に楽しみができるんだよ
                会えないのは本当に辛い. でもまた会えるって考えるだけで、言葉にできないくらい心が満たされる. どれだけ時間がかかっても、私はカズの笑顔を見るために、幸せそうな顔を見るために、ずっと待つよ. その顔を見ると、世界の何もかもがどうでもよくなって、カズだけが大切なんだって思える.
                カズは、私が悲しい時も、怒ってる時も、不安な時も、どんな時でも頼れる存在.
                たとえカズが落ち込んでても、私のことを想ってくれるその優しさが、本当に嬉しい.
                カズといると、心がドキドキして、変に緊張しちゃう.
                多分、カズとの関係を絶対に大切にしたいって、心が勝手に分かってるんだと思う.
                カズが自分に自信なくて、自分を見たくないって言うたびに、なんで？って思うよ.
                だって私はカズを見るだけで、心をギュッと掴まれたような気持ちになるんだもん.
                カズの手に触れたくて、カズに触れたくて、そう思うの!
            </p>
            <p>
                Happy Birthday, kazuchannnn! May all your dreams come true, and may our love continue to grow deeper with every passing year.
            </p>
            <p>
                With all my love, <br> Your forever sweetheart 💖
            </p>
        </div>
    """, unsafe_allow_html=True)

elif page == "Video":
    st.header("Kazuchan, love u 🎥")
    video_path1 = "WhatsApp Video 2025-05-05 at 11.08.41_4434be4a.mp4"
    video_path2 = "WhatsApp Video 2025-05-05 at 11.32.29_83aa8629.mp4"

    with open(video_path1, "rb") as video_file:
        st.video(video_file.read())

    with open(video_path2, "rb") as video_file:
        st.video(video_file.read())

elif page == "Foto":
    st.header("Album Foto Kazu📸")
    images = [
        "WhatsApp Image 2025-05-05 at 11.33.52_62480946.jpg",
        "WhatsApp Image 2025-05-05 at 11.46.52_636b666e.jpg",
        "WhatsApp Image 2025-05-05 at 11.46.39_dc34f3ef.jpg",
        "WhatsApp Image 2025-05-05 at 11.46.15_e0067f66.jpg",
    ]

    for img_path in images:
        img = Image.open(img_path)
        st.image(img, caption="A Special Moment", width=300)

elif page == "Grafik":
    st.header("Grafik Cinta Kita 💖 (Love Shape)")

    t = np.linspace(0, 2 * np.pi, 100)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

    frames = [
        go.Frame(data=[go.Scatter(x=x[:i], y=y[:i], mode='lines', line=dict(color='deeppink'))])
        for i in range(1, len(t) + 1)
    ]

    layout = go.Layout(
        title="Grafik Cinta dalam Bentuk Hati 💘",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        showlegend=False,
        updatemenus=[dict(
            type="buttons",
            showactive=False,
            buttons=[dict(label="▶️ Play",
                          method="animate",
                          args=[None, {
                              "frame": {"duration": 30, "redraw": True},
                              "fromcurrent": True,
                              "transition": {"duration": 0},
                              "mode": "immediate",
                              "loop": True
                          }])]
        )],
        width=600,
        height=600
    )

    fig = go.Figure(
        data=[go.Scatter(x=[], y=[], mode='lines', line=dict(color='deeppink'))],
        layout=layout,
        frames=frames
    )

    fig.layout.sliders = [dict(active=0, steps=[], visible=False)]
    st.plotly_chart(fig)

# Footer
st.markdown('<div class="footer">You mean the world to me, and I can\'t wait for many more birthdays together! 🎉</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="footer">
        I am so grateful for every moment we share. I love you more than you'll ever know, my love! 💖
    </div>
""", unsafe_allow_html=True)

# Hiasan Penutup
st.markdown("""
    <div style="background-color: #2e2e2e; padding: 20px; border-radius: 10px; font-size: 1.2em; text-align: center; color: white;">
        Wishing you endless happiness, my love. 💕 May all your dreams come true, and may our love grow stronger with every passing day. 💫
    </div>
""", unsafe_allow_html=True)
