import streamlit as st
from gtts import gTTS
from google import genai
from google.genai import types
import io

# 1. 設定網頁基本資訊
st.set_page_config(page_title="專屬三語學習空間", page_icon="🎓", layout="centered")
st.title("🎓 專屬三語學習空間")

# 語音生成函式（快取避免重複生成相同發音）
@st.cache_data(show_spinner=False)
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
    [
        "🇰🇷 韓文：完整發音與拼讀機",
        "🇹🇭 泰文：完整字母與聲調表",
        "🇺🇸 英文：AI 自由對話家教"
    ]
)

# ==========================================
# 模組一：韓文完整發音與拼讀機
# ==========================================
if mode == "🇰🇷 韓文：完整發音與拼讀機":
    st.header("🇰🇷 韓文零基礎：完整發音表與拼讀機")
    st.info("💡 韓文字由「子音」＋「母音」拼成。先聽熟單音，再到第三個分頁玩「互動拼讀機」！")

    tab1, tab2, tab3 = st.tabs(["1️⃣ 母音表 (21個)", "2️⃣ 子音表 (19個)", "3️⃣ 互動拼讀機"])

    with tab1:
        st.subheader("基本單母音 (10個)")
        basic_vowels = [
            ("ㅏ", "아", "a (啊)", "嘴巴自然張大"),
            ("ㅑ", "야", "ya (呀)", "先發 i 再滑向 a"),
            ("ㅓ", "어", "eo (喔)", "嘴型微張、舌頭微縮"),
            ("ㅕ", "여", "yeo (唷)", "先發 i 再滑向 eo"),
            ("ㅗ", "오", "o (歐)", "嘴唇向前嘟圓"),
            ("ㅛ", "요", "yo (優)", "先發 i 再滑向 o"),
            ("ㅜ", "우", "u (屋)", "嘴唇嘟得比 ㅗ 更小"),
            ("ㅠ", "유", "yu (淤)", "先發 i 再滑向 u"),
            ("ㅡ", "으", "eu (呃)", "嘴角向兩側拉開、牙齒微合"),
            ("ㅣ", "이", "i (衣)", "嘴角向兩側拉開像微笑"),
        ]
        cols = st.columns(2)
        for idx, (char, sound, roman, tip) in enumerate(basic_vowels):
            with cols[idx % 2]:
                with st.container(border=True):
                    st.markdown(f"### {char}  `{roman}`")
                    st.caption(tip)
                    if st.button("🔊 聽發音", key=f"kbv_{idx}"):
                        st.audio(text_to_speech(sound, "ko"), format="audio/mp3", autoplay=True)

        st.subheader("複合母音 (11個)")
        comp_vowels = [
            ("ㅐ", "애", "ae", "嘴型比 ㅏ 略小"),
            ("ㅒ", "얘", "yae", "i + ae"),
            ("ㅔ", "에", "e", "現代韓語發音與 ㅐ 幾乎相同"),
            ("ㅖ", "예", "ye", "i + e"),
            ("ㅘ", "와", "wa", "ㅗ + ㅏ 快速連讀"),
            ("ㅙ", "왜", "wae", "ㅗ + ㅐ 快速連讀"),
            ("ㅚ", "외", "oe", "現代韓語多唸成 we"),
            ("ㅝ", "워", "wo", "ㅜ + ㅓ 快速連讀"),
            ("ㅞ", "웨", "we", "ㅜ + ㅔ 快速連讀"),
            ("ㅟ", "위", "wi", "ㅜ + ㅣ 快速連讀"),
            ("ㅢ", "의", "ui", "ㅡ + ㅣ 快速連讀"),
        ]
        cols2 = st.columns(2)
        for idx, (char, sound, roman, tip) in enumerate(comp_vowels):
            with cols2[idx % 2]:
                with st.container(border=True):
                    st.markdown(f"### {char}  `{roman}`")
                    st.caption(tip)
                    if st.button("🔊 聽發音", key=f"kcv_{idx}"):
                        st.audio(text_to_speech(sound, "ko"), format="audio/mp3", autoplay=True)

    with tab2:
        st.subheader("基本子音 (14個) ＋ 雙子音 (5個)")
        consonants = [
            ("ㄱ", "가", "g / k", "舌根抵住軟顎（不送氣）"),
            ("ㄴ", "나", "n", "舌尖抵住上齒齦（鼻音）"),
            ("ㄷ", "다", "d / t", "舌尖抵住上齒齦（不送氣）"),
            ("ㄹ", "라", "r / l", "舌尖輕彈上顎"),
            ("ㅁ", "마", "m", "雙唇緊閉（鼻音）"),
            ("ㅂ", "바", "b / p", "雙唇閉合後放開（不送氣）"),
            ("ㅅ", "사", "s", "舌尖接近上齒齦摩擦出氣"),
            ("ㅇ", "아", "無聲 / ng", "在字首不發音；在字尾發 ng"),
            ("ㅈ", "자", "j", "舌面抵住硬顎（不送氣）"),
            ("ㅊ", "차", "ch", "ㅈ 的送氣音（強氣流）"),
            ("ㅋ", "카", "k", "ㄱ 的送氣音（強氣流）"),
            ("ㅌ", "타", "t", "ㄷ 的送氣音（強氣流）"),
            ("ㅍ", "파", "p", "ㅂ 的送氣音（強氣流）"),
            ("ㅎ", "하", "h", "喉嚨呼氣音"),
            ("ㄲ", "까", "kk (緊音)", "聲帶緊繃用力發出，不送氣"),
            ("ㄸ", "따", "tt (緊音)", "聲帶緊繃用力發出，不送氣"),
            ("ㅃ", "빠", "pp (緊音)", "聲帶緊繃用力發出，不送氣"),
            ("ㅆ", "싸", "ss (緊音)", "比 ㅅ 更急促有力"),
            ("ㅉ", "짜", "jj (緊音)", "聲帶緊繃用力發出，不送氣"),
        ]
        cols3 = st.columns(2)
        for idx, (char, sound, roman, tip) in enumerate(consonants):
            with cols3[idx % 2]:
                with st.container(border=True):
                    st.markdown(f"### {char}  `{roman}`")
                    st.caption(f"搭配 ㅏ 唸作「{sound}」｜{tip}")
                    if st.button("🔊 聽發音", key=f"kc_{idx}"):
                        st.audio(text_to_speech(sound, "ko"), format="audio/mp3", autoplay=True)

    with tab3:
        st.subheader("🧩 互動式「子音＋母音」自由拼讀機")
        st.write("隨意挑選一個子音和一個母音，系統會幫你組合成正確的韓文字並唸出來！")
        
        c_list = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
        v_list = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
        
        col_sel1, col_sel2 = st.columns(2)
        with col_sel1:
            sel_c = st.selectbox("1. 選擇子音：", c_list)
        with col_sel2:
            sel_v = st.selectbox("2. 選擇母音：", v_list)
        
        c_idx = c_list.index(sel_c)
        v_idx = v_list.index(sel_v)
        combined_char = chr(0xAC00 + (c_idx * 21 + v_idx) * 28)
        
        with st.container(border=True):
            st.markdown(f"<h1 style='text-align: center;'>{sel_c} + {sel_v} = {combined_char}</h1>", unsafe_allow_html=True)
            if st.button("🔊 聽組合後的發音", use_container_width=True):
                st.audio(text_to_speech(combined_char, "ko"), format="audio/mp3", autoplay=True)

# ==========================================
# 模組二：泰文完整字母與聲調表
# ==========================================
elif mode == "🇹🇭 泰文：完整字母與聲調表":
    st.header("🇹🇭 泰文零基礎：字母分類與聲調入門")
    st.info("💡 泰文子音分為「中、高、低」三組（決定聲調高低），母音則會寫在子音的上下左右！")

    tab1, tab2, tab3 = st.tabs(["1️⃣ 核心子音 (中/高/低)", "2️⃣ 常用母音位置", "3️⃣ 五聲調聽力練習"])

    with tab1:
        st.subheader("中子音 (9個) — 最基礎、最常作為拼讀入門")
        mid_c = [
            ("ก", "กอ ไก่ (Gor Gai)", "雞 (g/k)"),
            ("จ", "จอ จาน (Jor Jaan)", "盤子 (j)"),
            ("ฎ", "ฎอ ชฎา (Dor Cha-daa)", "尖頂冠 (d)"),
            ("ฏ", "ฏอ ปฏัก (Tor Pa-tak)", "刺棒 (t)"),
            ("ด", "ดอ เด็ก (Dor Dek)", "小孩 (d)"),
            ("ต", "ตอ เต่า (Tor Tao)", "烏龜 (t)"),
            ("บ", "บอ ใบไม้ (Bor Bai-mai)", "樹葉 (b)"),
            ("ป", "ปอ ปลา (Por Plaa)", "魚 (p)"),
            ("อ", "ออ อ่าง (Or Aang)", "盆子 (零聲母)"),
        ]
        cols = st.columns(2)
        for idx, (char, name, desc) in enumerate(mid_c):
            with cols[idx % 2]:
                with st.container(border=True):
                    st.markdown(f"### {char} — `{desc}`")
                    st.caption(name)
                    if st.button("🔊 聽發音", key=f"tmc_{idx}"):
                        st.audio(text_to_speech(name, "th"), format="audio/mp3", autoplay=True)

        st.subheader("常見高子音 (自帶高音調)")
        high_c = [
            ("ข", "ขอ ไข่ (Khor Khai)", "蛋 (kh)"),
            ("ฉ", "ฉอ ฉิ่ง (Chor Ching)", "鈸 (ch)"),
            ("ถ", "ถอ ถุง (Thor Thung)", "袋子 (th)"),
            ("ผ", "ผอ ผึ้ง (Phor Phueng)", "蜜蜂 (ph)"),
            ("ฝ", "ฝอ ฝา (For Faa)", "蓋子 (f)"),
            ("ส", "สอ เสือ (Sor Suea)", "老虎 (s)"),
            ("ห", "หอ หีบ (Hor Heep)", "箱子 (h)"),
        ]
        cols_h = st.columns(2)
        for idx, (char, name, desc) in enumerate(high_c):
            with cols_h[idx % 2]:
                with st.container(border=True):
                    st.markdown(f"### {char} — `{desc}`")
                    st.caption(name)
                    if st.button("🔊 聽發音", key=f"thc_{idx}"):
                        st.audio(text_to_speech(name, "th"), format="audio/mp3", autoplay=True)

        st.subheader("常見低子音 (最常出現在日常單字)")
        low_c = [
            ("ค", "คอ ควาย (Khor Khwaai)", "水牛 (kh)"),
            ("ง", "งอ งู (Ngor Nguu)", "蛇 (ng)"),
            ("ช", "ชอ ช้าง (Chor Chaang)", "大象 (ch)"),
            ("ซ", "ซอ โซ่ (Sor Soo)", "鎖鏈 (s)"),
            ("ท", "ทอ ทหาร (Thor Tha-haan)", "軍人 (th)"),
            ("น", "นอ หนู (Nor Nuu)", "老鼠 (n)"),
            ("พ", "พอ พาน (Phor Phaan)", "高腳盤 (ph)"),
            ("ฟ", "ฟอ ฟัน (For Fan)", "牙齒 (f)"),
            ("ม", "มอ ม้า (Mor Maa)", "馬 (m)"),
            ("ย", "ยอ ยักษ์ (Yor Yak)", "巨人 (y)"),
            ("ร", "รอ เรือ (Ror Ruea)", "船 (r)"),
            ("ล", "ลอ ลิง (Lor Ling)", "猴子 (l)"),
            ("ว", "วอ แหวน (Wor Waaen)", "戒指 (w)"),
        ]
        cols_l = st.columns(2)
        for idx, (char, name, desc) in enumerate(low_c):
            with cols_l[idx % 2]:
                with st.container(border=True):
                    st.markdown(f"### {char} — `{desc}`")
                    st.caption(name)
                    if st.button("🔊 聽發音", key=f"tlc_{idx}"):
                        st.audio(text_to_speech(name, "th"), format="audio/mp3", autoplay=True)

    with tab2:
        st.subheader("泰文母音位置示範（以中子音 ก 為例）")
        st.write("泰文母音分「短音」與「長音」，且會出現在子音的不同方位：")
        thai_vowels = [
            ("ก + า = กา", "gaa (長音 aa)", "寫在子音【右邊】"),
            ("ก + ะ = กะ", "ga (短音 a)", "寫在子音【右邊】"),
            ("ก + ี = กี", "gii (長音 ii)", "寫在子音【上面】"),
            ("ก + ิ = กิ", "gi (短音 i)", "寫在子音【上面】"),
            ("ก + ู = กู", "guu (長音 uu)", "寫在子音【下面】"),
            ("ก + ุ = กุ", "gu (短音 u)", "寫在子音【下面】"),
            ("เ + ก = เก", "gee (長音 ee)", "寫在子音【左邊】"),
            ("แ + ก = แก", "gaae (長音 aae)", "寫在子音【左邊】"),
            ("โ + ก = โก", "goo (長音 oo)", "寫在子音【左邊】"),
            ("ไ + ก = ไก", "gai (短音 ai)", "寫在子音【左邊】"),
        ]
        for idx, (example, roman, pos) in enumerate(thai_vowels):
            with st.container(border=True):
                c1, c2 = st.columns(2)
                with c1:
                    st.markdown(f"### {example}  `{roman}`")
                    st.caption(f"位置規則：{pos}")
                with c2:
                    word_to_read = example.split("=")[-1].strip()
                    if st.button("🔊 唸拼讀", key=f"tv_{idx}"):
                        st.audio(text_to_speech(word_to_read, "th"), format="audio/mp3", autoplay=True)

    with tab3:
        st.subheader("🎵 泰文五聲調聽力對比")
        st.write("泰文共有 5 個聲調（第一聲平調、第二聲低調、第三聲降調、第四聲高調、第五聲升調）。點按鈕聽聽看差別：")
        tones = [
            ("กา", "第一聲 (平調)", "類似中文第一聲，平穩念出 gaa"),
            ("ก่า", "第二聲 (低調)", "壓低喉嚨往下沉的音調 gàa"),
            ("ก้า", "第三聲 (降調)", "從高處往下掉（類似中文第四聲）gâa"),
            ("ก๊า", "第四聲 (高調)", "音調高高揚起 gáa"),
            ("ก๋า", "第五聲 (升調)", "先低再往上揚（類似中文第二聲）gǎa"),
        ]
        for idx, (word, tone_name, desc) in enumerate(tones):
            with st.container(border=True):
                c1, c2 = st.columns(2)
                with c1:
                    st.markdown(f"### {word} — **{tone_name}**")
                    st.caption(desc)
                with c2:
                    if st.button("🔊 聽聲調", key=f"ttone_{idx}"):
                        st.audio(text_to_speech(word, "th"), format="audio/mp3", autoplay=True)

# ==========================================
# 模組三：英文 AI 自由對話家教
# ==========================================
elif mode == "🇺🇸 英文：AI 自由對話家教":
    st.header("🇺🇸 英文 AI 自由對話家教")
    st.write("用英文輸入任何你想聊的內容！AI 會用自然英文跟你聊天，並在下方附上「文法與道地說法建議」。")

    if "GEMINI_API_KEY" not in st.secrets:
        st.warning("⚠️ 尚未設定 `GEMINI_API_KEY`！請先到 Streamlit 後台的 Settings > Secrets 貼上你的免費 Google AI Studio 金鑰，才能啟動自由對話喔。")
        st.stop()

    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

    col_t1, col_t2 = st.columns(2)
    with col_t1:
        topic = st.selectbox(
            "選擇聊天主題（或直接自由輸入）：",
            [
                "☕ 日常閒聊 (Daily Chat)",
                "✈️ 出國旅遊與機場點餐 (Travel & Dining)",
                "🎬 電影、追劇與偶像文化 (Movies & Pop Culture)",
                "💼 職場與生活分享 (Work & Life)"
            ]
        )
    with col_t2:
        level = st.selectbox("AI 英文難度：", ["初級 (簡單短句)", "中級 (自然口語)"])

    if "ai_messages" not in st.session_state:
        st.session_state.ai_messages = [
            {
                "role": "assistant",
                "english": "Hi there! I'm your English conversation partner. How is your day going so far?",
                "feedback": "💡 試著用英文打字回覆我，例如：It's going pretty well, thank you! How about you?"
            }
        ]

    if st.button("🔄 清除紀錄重新開始對話"):
        st.session_state.ai_messages = [
            {
                "role": "assistant",
                "english": f"Let's chat about {topic}! Tell me anything on your mind.",
                "feedback": "💡 直接在下方輸入框打英文就可以開始聊天囉！"
            }
        ]
        st.rerun()

    for idx, msg in enumerate(st.session_state.ai_messages):
        with st.chat_message(msg["role"]):
            if msg["role"] == "user":
                st.write(msg["content"])
            else:
                st.markdown(f"**{msg['english']}**")
                if st.button("🔊 聽 AI 發音", key=f"ai_tts_{idx}"):
                    st.audio(text_to_speech(msg["english"], "en"), format="audio/mp3", autoplay=True)
                if msg.get("feedback"):
                    with st.expander("📝 查看表達建議與中文提示", expanded=True):
                        st.markdown(msg["feedback"])

    user_text = st.chat_input("輸入英文跟 AI 聊天（不會拼的單字偶爾夾雜中文也可以）...")
    if user_text:
        st.session_state.ai_messages.append({"role": "user", "content": user_text})
        
        history_text = ""
        for m in st.session_state.ai_messages[-6:]:
            if m["role"] == "user":
                history_text += f"User: {m['content']}\n"
            else:
                history_text += f"Tutor: {m['english']}\n"

        system_instruction = f"""
        你是一位親切、有耐心的英文口說家教，正在與一位母語為繁體中文的學習者進行「{topic}」主題的英文自由對話。
        目前的對話難度設定為：{level}。
        請嚴格按照以下格式回覆，並用「===SPLIT===」將兩個區塊分開：

        第一區塊（純英文自然對話）：
        用自然、生活化的英文回應學習者的話，並在結尾反問一個簡單相關的問題，引導對方繼續開口聊天。（注意：這個區塊只能有純英文，不要夾雜中文或表情符號，方便語音系統直接朗讀）。

        ===SPLIT===

        第二區塊（繁體中文學習回饋）：
        1. 【AI 英文翻譯】：將第一區塊的英文翻譯成自然繁體中文。
        2. 【你的句子健檢】：溫柔檢查學習者剛才那句英文有沒有文法錯誤；如果完全正確就給予肯定，並提供 1 句更道地、母語人士常用的替換說法（附中文解釋）。
        """

        with st.spinner("AI 家教正在思考回覆..."):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=f"最近的對話紀錄：\n{history_text}\n請根據學習者最後一句話進行回覆：",
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=0.7,
                    )
                )
                reply_raw = response.text
                if "===SPLIT===" in reply_raw:
                    eng_part, fb_part = reply_raw.split("===SPLIT===", 1)
                else:
                    eng_part, fb_part = reply_raw, ""

                st.session_state.ai_messages.append({
                    "role": "assistant",
                    "english": eng_part.strip(),
                    "feedback": fb_part.strip()
                })
                st.rerun()
            except Exception as e:
                st.error(f"連線 AI 時發生問題，請確認 Secrets 中的金鑰是否正確。錯誤細節：{e}")

# === 程式碼結束 ===
