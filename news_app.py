import streamlit as st
import feedparser

st.set_page_config(page_title="ニュース", layout="wide")

st.title("📰 ニュース")
st.caption("メディア × キーワード")

# =====================
# RSS一覧
# =====================
rss_list = {
    "NHK": "https://www.nhk.or.jp/rss/news/cat0.xml",
    "ITmedia": "https://rss.itmedia.co.jp/rss/2.0/news_bursts.xml",
    "GIGAZINE": "https://gigazine.net/news/rss_2.0/",
}

# =====================
# 一般ニュース用キーワード
# =====================
keywords = [
    "政府","国会","首相","大臣","政策","予算","税制",
    "経済","景気","物価","インフレ","株価","為替","円安","円高",
    "金利","市場","投資","金融","企業","決算","業績","倒産",
    "雇用","賃金","年収","副業","働き方","転職","就職",
    "AI","人工知能","IT","DX","クラウド","半導体","セキュリティ",
    "医療","健康","年金","教育","少子化",
    "地震","台風","豪雨","災害","防災"
]

# =====================
# サイドバー
# =====================
st.sidebar.header("表示設定")

selected_media = st.sidebar.multiselect(
    "表示するメディア",
    rss_list.keys(),
    default=list(rss_list.keys())
)

selected_keywords = st.sidebar.multiselect(
    "キーワード",
    keywords,
    default=keywords
)

st.divider()

# =====================
# タブ作成
# =====================
tab1, tab2 = st.tabs(["ニュース", "サイト"])

# =====================
# 📰 ニュース
# =====================
with tab1:
    for media, url in rss_list.items():
        if media not in selected_media:
            continue

        feed = feedparser.parse(url)
        for entry in feed.entries:
            if any(word in entry.title for word in selected_keywords):
                st.subheader(f"【{media}】{entry.title}")
                st.link_button("記事を読む", entry.link)
                st.write("---")

# =====================
# 🌐 サイト
# =====================
with tab2:
    st.subheader("🔗 便利サイト")

    st.link_button(
        "📊 田中貴金属｜金・プラチナ相場を見る",
        "https://gold.tanaka.co.jp/commodity/souba/"
    )

    st.link_button(
        "🚃 阪急電車｜運行情報",
        "https://www.hankyu.co.jp/railinfo/"
    )

    st.link_button(
        "📰 日本経済新聞｜WEBトップ",
        "https://www.nikkei.com/"
    )









