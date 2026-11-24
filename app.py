import streamlit as st
from gtts import gTTS
import io

# 1. 設定網頁基本資訊
st.set_page_config(page_title="專屬三語學習空間", page_icon="🎓", layout="centered")
st.title("🎓 專屬三語學習空間")

# 語音生成函式
def text_to_speech(text, lang_code):
    tts = gTTS(text=text, lang=lang_code)
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes

# 側邊欄：選擇語言模組
st.sidebar.header("📚 選擇學習模組")
mode = st.sidebar.radio(
    "請選擇想練習的語言：",
    ["🇰🇷 韓文：零基礎發音拼音", "🇹🇭 泰文：零基礎發音拼音", "🇺🇸 英文：情境對話練習"]
)

# ==========================================
# 模組一：韓文零基礎發音拼音
# ==========================================
if mode == "🇰🇷 韓文：零基礎發音拼音":
    st.header("🇰🇷 韓文零基礎：40音拼讀入門")
    st.info("💡 韓文字就像積木，是由「子音（左/上）」＋「母音（右/下）」組合而成的！")

    tab1, tab2 = st.tabs(["1️⃣ 基礎母音 (母音)", "2️⃣ 子音＋母音 拼讀練習"])

    with tab1:
        st.subheader("先認識最基礎的 6 個單母音")
        korean_vowels = [
            {"char": "ㅏ", "sound": "아", "roman": "a (啊)", "tip": "嘴巴張大，舌頭放平"},
            {"char": "ㅓ", "sound": "어", "roman": "eo (喔)", "tip": "嘴巴自然張開，比「啊」小一點"},
            {"char": "ㅗ", "sound": "오", "roman": "o (歐)", "tip": "嘴唇向前嘟圓"},
            {"char": "ㅜ", "sound": "우", "roman": "u (屋)", "tip": "嘴唇嘟得比 ㅗ 更小"},
            {"char": "ㅡ", "sound": "으", "roman": "eu (呃)", "tip": "嘴角向兩側拉開，上下牙齒微合"},
            {"char": "ㅣ", "sound": "이", "roman": "i (衣)", "tip": "嘴角向兩側拉開，像微笑"},
        ]
        for idx, v in enumerate(korean_vowels):
            with st.container(border=True):
                c1, c2 = st.columns([3, 1])
                with c1:
                    st.markdown(f"### {v['char']}  （讀音：{v['roman']}）")
                    st.write(f"發音嘴型：{v['tip']}")
                with c2:
                    if st.button("🔊 聽發音", key=f"kv_{idx}"):
                        st.audio(text_to_speech(v['sound'], "ko"), format="audio/mp3", autoplay=True)

    with tab2:
        st.subheader("子音 ㄱ (g/k) 搭配母音的拼讀")
        korean_combos = [
            {"formula": "ㄱ (g) + ㅏ (a)", "result": "가", "roman": "ga", "word": "가수 (歌手)"},
            {"formula": "ㄱ (g) + ㅓ (eo)", "result": "거", "roman": "geo", "word": "거울 (鏡子)"},
            {"formula": "ㄱ (g) + ㅗ (o)", "result": "고", "roman": "go", "word": "고기 (肉)"},
            {"formula": "ㄱ (g) + ㅜ (u)", "result": "구", "roman": "gu", "word": "구두 (皮鞋)"},
            {"formula": "ㄱ (g) + ㅣ (i)", "result": "기", "roman": "gi", "word": "기차 (火車)"},
        ]
        for idx, item in enumerate(korean_combos):
            with st.container(border=True):
                c1, c2 = st.columns([3, 1])
                with c1:
                    st.markdown(f"### {item['formula']} ＝ **{item['result']}** ({item['roman']})")
                    st.caption(f"延伸單字範例：{item['word']}")
                with c2:
                    if st.button("🔊 唸拼讀", key=f"kc_{idx}"):
                        st.audio(text_to_speech(item['result'], "ko"), format="audio/mp3", autoplay=True)

# ==========================================
# 模組二：泰文零基礎發音拼音
# ==========================================
elif mode == "🇹🇭 泰文：零基礎發音拼音":
    st.header("🇹🇭 泰文零基礎：字母與拼讀入門")
    st.info("💡 泰文是由「子音」當主角，母音會寫在子音的「左、右、上、下」四個方向！")

    tab1, tab2 = st.tabs(["1️⃣ 常見基礎子音", "2️⃣ 子音＋母音 拼讀練習"])

    with tab1:
        st.subheader("先認識幾個最常見的中子音")
        thai_consonants = [
            {"char": "ก", "name": "ก ไก่ (Gor Gai)", "sound": "กอ", "meaning": "雞 (發音接近不送氣的 g/k)"},
            {"char": "จ", "name": "จ จาน (Jor Jaan)", "sound": "จอ", "meaning": "盤子 (發音接近 j/zh)"},
            {"char": "ด", "name": "ด เด็ก (Dor Dek)", "sound": "ดอ", "meaning": "小孩 (發音接近 d)"},
            {"char": "ต", "name": "ต เต่า (Tor Tao)", "sound": "ตอ", "meaning": "烏龜 (發音接近不送氣的 t/d)"},
            {"char": "บ", "name": "บ ใบไม้ (Bor Bai-mai)", "sound": "บอ", "meaning": "樹葉 (發音接近 b)"},
            {"char": "ป", "name": "ป ปลา (Por Plaa)", "sound": "ปอ", "meaning": "魚 (發音接近不送氣的 p/b)"},
        ]
        for idx, c in enumerate(thai_consonants):
            with st.container(border=True):
                c1, c2 = st.columns([3, 1])
                with c1:
                    st.markdown(f"### {c['char']} — {c['name']}")
                    st.write(f"代表單字與發音提示：{c['meaning']}")
                with c2:
                    if st.button("🔊 聽字母音", key=f"tc_{idx}"):
                        st.audio(text_to_speech(c['sound'], "th"), format="audio/mp3", autoplay=True)

    with tab2:
        st.subheader("中子音 ก (g) 搭配不同位置母音的拼讀")
        thai_combos = [
            {"formula": "ก + า (長音 aa，寫在右邊)", "result": "กา", "roman": "gaa", "meaning": "烏鴉 / 茶壺"},
            {"formula": "ก + ี (長音 ii，寫在上面)", "result": "กี", "roman": "gii", "meaning": "拼讀練習音"},
            {"formula": "ก + ู (長音 uu，寫在下面)", "result": "กู", "roman": "guu", "meaning": "拼讀練習音"},
            {"formula": "เ (長音 ee，寫在左邊) + ก", "result": "เก", "roman": "gee", "meaning": "歪斜"},
            {"formula": "โ (長音 oo，寫在左邊) + ก", "result": "โก", "roman": "goo", "meaning": "拼讀練習音"},
        ]
        for idx, item in enumerate(thai_combos):
            with st.container(border=True):
                c1, c2 = st.columns([3, 1])
                with c1:
                    st.markdown(f"### {item['formula']} ＝ **{item['result']}** ({item['roman']})")
                    st.caption(f"字義參考：{item['meaning']}")
                with c2:
                    if st.button("🔊 唸拼讀", key=f"tcombo_{idx}"):
                        st.audio(text_to_speech(item['result'], "th"), format="audio/mp3", autoplay=True)

# ==========================================
# 模組三：英文情境對話練習
# ==========================================
elif mode == "🇺🇸 英文：情境對話練習":
    st.header("🇺🇸 英文情境對話模擬器")
    st.write("選擇一個生活場景，試著用英文回覆對方，並點擊喇叭聽聽看道地的發音！")

    scenarios = {
        "☕ 咖啡廳點餐 (Ordering Coffee)": [
            {"role": "assistant", "text": "Hi there! Welcome to Star Cafe. What can I get started for you today?", "hint": "試著回答你想喝什麼，例如：Hi, I would like an iced latte, please."},
            {"role": "assistant", "text": "Sure! Would you like that for here or to go? And what size would you like?", "hint": "回答內用(for here)或外帶(to go)，以及大小杯(medium/large)。"},
            {"role": "assistant", "text": "Got it. Anything else for you today, maybe a croissant or a muffin?", "hint": "回答是否還需要其他餐點，例如：No, that's all. Thank you!"},
            {"role": "assistant", "text": "Alright, your total is $4.50. You can tap your card right here. Have a great day!", "hint": "禮貌道謝結束對話，例如：Thank you, you too!"}
        ],
        "✈️ 機場與飯店入住 (Hotel Check-in)": [
            {"role": "assistant", "text": "Good afternoon! Welcome to Grand Hotel. How may I help you?", "hint": "表達你要辦理入住，例如：Hi, I have a reservation under [你的名字]."},
            {"role": "assistant", "text": "Let me check... Yes, I see your booking for three nights. May I see your passport, please?", "hint": "遞出護照並回答，例如：Sure, here you go."},
            {"role": "assistant", "text": "Thank you. Here is your room key. Breakfast is served from 7 to 10 AM on the second floor. Enjoy your stay!", "hint": "道謝並詢問 Wi-Fi 或道別，例如：Thank you so much!"}
        ]
    }

    selected_scene = st.selectbox("選擇練習場景：", list(scenarios.keys()))
    
    # 初始化對話紀錄
    if "scene" not in st.session_state or st.session_state.scene != selected_scene:
        st.session_state.scene = selected_scene
        st.session_state.step = 0
        st.session_state.chat_history = [scenarios[selected_scene][0]]

    # 顯示重置按鈕
    if st.button("🔄 重新開始這段對話"):
        st.session_state.step = 0
        st.session_state.chat_history = [scenarios[selected_scene][0]]
        st.rerun()

    # 渲染對話氣泡
    for idx, msg in enumerate(st.session_state.chat_history):
        with st.chat_message(msg["role"]):
            st.write(msg["text"])
            if msg["role"] == "assistant":
                # 提供發音按鈕與回覆提示
                col_a, col_b = st.columns([1, 3])
                with col_a:
                    if st.button("🔊 聽對方說", key=f"chat_audio_{idx}"):
                        st.audio(text_to_speech(msg["text"], "en"), format="audio/mp3", autoplay=True)
                with col_b:
                    if "hint" in msg:
                        st.caption(f"💡 回覆提示：{msg['hint']}")

    # 使用者輸入框
    user_input = st.chat_input("在這裡輸入你的英文回覆...")
    if user_input:
        # 紀錄使用者的話
        st.session_state.chat_history.append({"role": "user", "text": user_input})
        st.session_state.step += 1
        
        # 如果劇本還有下一句，加入 AI 回覆
        scene_script = scenarios[selected_scene]
        if st.session_state.step < len(scene_script):
            st.session_state.chat_history.append(scene_script[st.session_state.step])
        else:
            st.session_state.chat_history.append({
                "role": "assistant", 
                "text": "🎉 太棒了！你已經完成這個場景的對話練習！可以點擊上方的「重新開始」或切換其他場景繼續練習。"
            })
        st.rerun()
