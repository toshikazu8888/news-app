import streamlit as st
import feedparser

st.set_page_config(page_title="自分専用ニュース", layout="wide")

st.title("📰 自分専用ニュースアプリ")
st.caption("複数メディア × キーワード抽出")

rss_list = {
    "NHK": "https://www.nhk.or.jp/rss/news/cat0.xml",
    "Yahoo": "https://news.yahoo.co.jp/rss/topics/top-picks.xml",
    "日経": "https://www.nikkei.com/rss/news/major.xml",
    "ITmedia": "https://rss.itmedia.co.jp/rss/2.0/news_bursts.xml"
}

keywords = [
    # 政治・行政
    "政府","国会","首相","大臣","政策","予算","税制",
    "外交","安全保障","防衛","自治体","行政","議員","憲法",

    # 経済・金融
    "経済","景気","物価","インフレ","株価","為替","円安","円高","プラチナ",
    "金利","市場","投資","金融","企業","決算","業績","倒産",

    # 仕事・働き方
    "雇用","賃金","年収","副業","働き方","労働","人手不足",
    "採用","転職","就職",

    # IT・テクノロジー
    "AI","人工知能","IT","DX","デジタル","システム","データ",
    "クラウド","サイバー","セキュリティ","自動化","半導体","技術",

    # 社会・生活
    "医療","健康","病院","年金","社会保障","高齢化","少子化",
    "教育","物価高","生活",

    # 災害・安全
    "地震","震度","台風","大雨","豪雨","災害","避難","防災"
]



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

for media, url in rss_list.items():
    if media not in selected_media:
        continue

    feed = feedparser.parse(url)
    for entry in feed.entries:
        if any(word in entry.title for word in selected_keywords):
            st.subheader(f"【{media}】{entry.title}")
            st.link_button("記事を読む", entry.link)
            st.write("---")
