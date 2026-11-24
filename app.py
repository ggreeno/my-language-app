import streamlit as st
from gtts import gTTS
from google import genai
from google.genai import types
import io

st.set_page_config(page_title="專屬三語學習空間", page_icon="🎓", layout="centered")
st.title("🎓 專屬三語學習空間")

@st.cache_data(show_spinner=False)
def text_to_speech(text, lang_code):
    tts = gTTS(text=text, lang=lang_code)
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes.getvalue()

st.sidebar.header("📚 選擇學習模組")
mode = st.sidebar.radio(
    "請選擇想練習的語言：",
    ["🇰🇷 韓文：完整發音與拼讀機", "🇹🇭 泰文：完整字母與聲調表", "🇺🇸 英文：AI 語音對話家教"]
)

# ==========================================
# 模組一：韓文
# ==========================================
if mode == "🇰🇷 韓文：完整發音與拼讀機":
    st.header("🇰🇷 韓文零基礎：完整發音表與拼讀機")
    st.info("💡 韓文字由「子音」＋「母音」拼成。先聽熟單音，再到第三個分頁玩「互動拼讀機」！")
    tab1, tab2, tab3 = st.tabs(["1️⃣ 母音表 (21個)", "2️⃣ 子音表 (19個)", "3️⃣ 互動拼讀機"])

    with tab1:
        st.subheader("基本單母音 (10個)")
        basic_vowels = [
            ("ㅏ", "아", "a (啊)", "嘴巴自然張大"), ("ㅑ", "야", "ya (呀)", "先發 i 再滑向 a"),
            ("ㅓ", "어", "eo (喔)", "嘴型微張、舌頭微縮"), ("ㅕ", "여", "yeo (唷)", "先發 i 再滑向 eo"),
            ("ㅗ", "오", "o (歐)", "嘴唇向前嘟圓"), ("ㅛ", "요", "yo (優)", "先發 i 再滑向 o"),
            ("ㅜ", "우", "u (屋)", "嘴唇嘟得比 ㅗ 更小"), ("ㅠ", "유", "yu (淤)", "先發 i 再滑向 u"),
            ("ㅡ", "으", "eu (呃)", "嘴角向兩側拉開、牙齒微合"), ("ㅣ", "이", "i (衣)", "嘴角向兩側拉開像微笑"),
        ]
        cols = st.columns(2)
        for idx, (char, sound, roman, tip) in enumerate(basic_vowels):
            with cols[idx % 2]:
                with st.container(border=True):
                    st.markdown(f"### {char} `{roman}`")
                    st.caption(tip)
                    if st.button("🔊 聽發音", key=f"kbv_{idx}"):
                        st.audio(text_to_speech(sound, "ko"), format="audio/mp3", autoplay=True)

        st.subheader("複合母音 (11個)")
        comp_vowels = [
            ("ㅐ", "애", "ae", "嘴型比 ㅏ 略小"), ("ㅒ", "얘", "yae", "i + ae"),
            ("ㅔ", "에", "e", "現代韓語發音與 ㅐ 幾乎相同"), ("ㅖ", "예", "ye", "i + e"),
            ("ㅘ", "와", "wa", "ㅗ + ㅏ 快速連讀"), ("ㅙ", "왜", "wae", "ㅗ + ㅐ 快速連讀"),
            ("ㅚ", "외", "oe", "現代韓語多唸成 we"), ("ㅝ", "워", "wo", "ㅜ + ㅓ 快速連讀"),
            ("ㅞ", "웨", "we", "ㅜ + ㅔ 快速連讀"), ("ㅟ", "위", "wi", "ㅜ + ㅣ 快速連讀"),
            ("ㅢ", "의", "ui", "ㅡ + ㅣ 快速連讀"),
        ]
        cols2 = st.columns(2)
        for idx, (char, sound, roman, tip) in enumerate(comp_vowels):
            with cols2[idx % 2]:
                with st.container(border=True):
                    st.markdown(f"### {char} `{roman}`")
                    st.caption(tip)
                    if st.button("🔊 聽發音", key=f"kcv_{idx}"):
                        st.audio(text_to_speech(sound, "ko"), format="audio/mp3", autoplay=True)

    with tab2:
        st.subheader("基本子音 (14個) ＋ 雙子音 (5個)")
        consonants = [
            ("ㄱ", "가", "g / k", "舌根抵住軟顎（不送氣）"), ("ㄴ", "나", "n", "舌尖抵住上齒齦（鼻音）"),
            ("ㄷ", "다", "d / t", "舌尖抵住上齒齦（不送氣）"), ("ㄹ", "라", "r / l", "舌尖輕彈上顎"),
            ("ㅁ", "마", "m", "雙唇緊閉（鼻音）"), ("ㅂ", "바", "b / p", "雙唇閉合後放開（不送氣）"),
            ("ㅅ", "사", "s", "舌尖接近上齒齦摩擦出氣"), ("ㅇ", "아", "無聲 / ng", "在字首不發音；在字尾發 ng"),
            ("ㅈ", "자", "j", "舌面抵住硬顎（不送氣）"), ("ㅊ", "차", "ch", "ㅈ 的送氣音（強氣流）"),
            ("ㅋ", "카", "k", "ㄱ 的送氣音（強氣流）"), ("ㅌ", "타", "t", "ㄷ 的送氣音（強氣流）"),
            ("ㅍ", "파", "p", "ㅂ 的送氣音（強氣流）"), ("ㅎ", "하", "h", "喉嚨呼氣音"),
            ("ㄲ", "까", "kk (緊音)", "聲帶緊繃用力發出，不送氣"), ("ㄸ", "따", "tt (緊音)", "聲帶緊繃用力發出，不送氣"),
            ("ㅃ", "빠", "pp (緊音)", "聲帶緊繃用力發出，不送氣"), ("ㅆ", "싸", "ss (緊音)", "比 ㅅ 更急促有力"),
            ("ㅉ", "짜", "jj (緊音)", "聲帶緊繃用力發出，不送氣"),
        ]
        cols3 = st.columns(2)
        for idx, (char, sound, roman, tip) in enumerate(consonants):
            with cols3[idx % 2]:
                with st.container(border=True):
                    st.markdown(f"### {char} `{roman}`")
                    st.caption(f"搭配 ㅏ 唸作「{sound}」｜{tip}")
                    if st.button("🔊 聽發音", key=f"kc_{idx}"):
                        st.audio(text_to_speech(sound, "ko"), format="audio/mp3", autoplay=True)

    with tab3:
        st.subheader("🧩 互動式「子音＋母音」自由拼讀機")
        c_list = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
        v_list = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
        col_sel1, col_sel2 = st.columns(2)
        with col_sel1:
            sel_c = st.selectbox("1. 選擇子音：", c_list)
        with col_sel2:
            sel_v = st.selectbox("2. 選擇母音：", v_list)
        combined_char = chr(0xAC00 + (c_list.index(sel_c) * 21 + v_list.index(sel_v)) * 28)
        with st.container(border=True):
            st.markdown(f"<h1 style='text-align: center;'>{sel_c} + {sel_v} = {combined_char}</h1>", unsafe_allow_html=True)
            if st.button("🔊 聽組合後的發音", use_container_width=True):
                st.audio(text_to_speech(combined_char, "ko"), format="audio/mp3", autoplay=True)

# ==========================================
# 模組二：泰文
# ==========================================
elif mode == "🇹🇭 泰文：完整字母與聲調表":
    st.header("🇹🇭 泰文零基礎：字母分類與聲調入門")
    st.info("💡 泰文子音分為「中、高、低」三組（決定聲調高低），母音則會寫在子音的上下左右！")
    tab1, tab2, tab3 = st.tabs(["1️⃣ 核心子音 (中/高/低)", "2️⃣ 常用母音位置", "3️⃣ 五聲調聽力練習"])

    with tab1:
        st.subheader("中子音 (9個)")
        mid_c = [
            ("ก", "กอ ไก่ (Gor Gai)", "雞 (g/k)"), ("จ", "จอ จาน (Jor Jaan)", "盤子 (j)"),
            ("ฎ", "ฎอ ชฎา (Dor Cha-daa)", "尖頂冠 (d)"), ("ฏ", "ฏอ ปฏัก (Tor Pa-tak)", "刺棒 (t)"),
            ("ด", "ดอ เด็ก (Dor Dek)", "小孩 (d)"), ("ต", "ตอ เต่า (Tor Tao)", "烏龜 (t)"),
            ("บ", "บอ ใบไม้ (Bor Bai-mai)", "樹葉 (b)"), ("ป", "ปอ ปลา (Por Plaa)", "魚 (p)"),
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

        st.subheader("常見高子音 (7個)")
        high_c = [
            ("ข", "ขอ ไข่ (Khor Khai)", "蛋 (kh)"), ("ฉ", "ฉอ ฉิ่ง (Chor Ching)", "鈸 (ch)"),
            ("ถ", "ถอ ถุง (Thor Thung)", "袋子 (th)"), ("ผ", "ผอ ผึ้ง (Phor Phueng)", "蜜蜂 (ph)"),
            ("ฝ", "ฝอ ฝา (For Faa)", "蓋子 (f)"), ("ส", "สอ เสือ (Sor Suea)", "老虎 (s)"),
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

        st.subheader("常見低子音 (14個)")
        low_c = [
            ("ค", "คอ ควาย (Khor Khwaai)", "水牛 (kh)"), ("ง", "งอ งู (Ngor Nguu)", "蛇 (ng)"),
            ("ช", "ชอ ช้าง (Chor Chaang)", "大象 (ch)"), ("ซ", "ซอ โซ่ (Sor Soo)", "鎖鏈 (s)"),
            ("ท", "ทอ ทหาร (Thor Tha-haan)", "軍人 (th)"), ("น", "นอ หนู (Nor Nuu)", "老鼠 (n)"),
            ("พ", "พอ พาน (Phor Phaan)", "高腳盤 (ph)"), ("ฟ", "ฟอ ฟัน (For Fan)", "牙齒 (f)"),
            ("ม", "มอ ม้า (Mor Maa)", "馬 (m)"), ("ย", "ยอ ยักษ์ (Yor Yak)", "巨人 (y)"),
            ("ร", "รอ เรือ (Ror Ruea)", "船 (r)"), ("ล", "ลอ ลิง (Lor Ling)", "猴子 (l)"),
            ("ว", "วอ แหวน (Wor Waen)", "戒指 (w)"), ("ฮ", "ฮอ นกฮูก (Hor Nok-huuk)", "貓頭鷹 (h)"),
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
        st.subheader("常用母音與書寫位置（以 อ 為子音示範）")
        thai_vowels = [
            ("-า (อา)", "อา", "aa (長音 啊)", "寫在子音【右邊】"), ("-ิ (อิ)", "อิ", "i (短音 衣)", "寫在子音【上方】"),
            ("-ี (อี)", "อี", "ii (長音 衣)", "寫在子音【上方】"), ("-ุ (อุ)", "อุ", "u (短音 屋)", "寫在子音【下方】"),
            ("-ู (อู)", "อู", "uu (長音 屋)", "寫在子音【下方】"), ("เ- (เอ)", "เอ", "ee (長音 欸)", "寫在子音【左邊】"),
            ("แ- (แอ)", "แอ", "aae (大嘴 欸)", "寫在子音【左邊】"), ("โ- (โอ)", "โอ", "oo (長音 歐)", "寫在子音【左邊】"),
            ("ใ- / ไ- (ไอ)", "ไอ", "ai (愛)", "寫在子音【左邊】"), ("-ำ (อำ)", "อำ", "am (暗)", "上方圓圈＋右邊長劃"),
        ]
        cols_v = st.columns(2)
        for idx, (pattern, sound, roman, pos) in enumerate(thai_vowels):
            with cols_v[idx % 2]:
                with st.container(border=True):
                    st.markdown(f"### {pattern}")
                    st.caption(f"發音：`{roman}` ｜ {pos}")
                    if st.button("🔊 聽發音", key=f"tv_{idx}"):
                        st.audio(text_to_speech(sound, "th"), format="audio/mp3", autoplay=True)

    with tab3:
        st.subheader("🎵 泰文五聲調聽力練習（以中子音 กา 示範）")
        tones = [
            ("1️⃣ 中平調 (สามัญ)", "กา", "gaa (烏鴉)", "無聲調符號，音高平穩（類似中文第一聲）"),
            ("2️⃣ 低調 (เอก)", "ก่า", "gàa", "符號 ่，音調低沉平穩（類似台語第3聲）"),
            ("3️⃣ 降調 (โท)", "ก้า", "gâa", "符號 ้，從高處往下滑落（類似中文第四聲）"),
            ("4️⃣ 高調 (ตรี)", "ก๊า", "gáa", "符號 ๊，音調高揚上衝"),
            ("5️⃣ 升調 (จัตวา)", "ก๋า", "gǎa", "符號 ๋，先低後往上揚（類似中文第二聲）"),
        ]
        for idx, (tone_name, word, roman, desc) in enumerate(tones):
            with st.container(border=True):
                c1, c2 = st.columns([3, 1])
                with c1:
                    st.markdown(f"#### {tone_name} — **{word}** (`{roman}`)")
                    st.caption(desc)
       		with c2:
            if st.button("🔊 聽聲調", key=f"ttone_{idx}", use_container_width=True):
                st.audio(text_to_speech(word, "th"), format="audio/mp3", autoplay=True)

# ==========================================
# 模組三：英文 AI 語音對話家教
# ==========================================
elif mode == "🇺🇸 英文：AI 語音對話家教":
    st.header("🇺🇸 英文口說與對話 AI 家教")
    st.info("💡 你可以直接「按麥克風講英文」，或「打字輸入」，AI 家教會用英文回覆並附上語音朗讀與中文小提醒！")

    api_key = st.secrets.get("GEMINI_API_KEY")
    if not api_key:
        st.error("⚠️ 找不到 `GEMINI_API_KEY`！請到 Streamlit Cloud 的 App Settings → Secrets 確認已設定金鑰。")
        st.stop()

    client = genai.Client(api_key=api_key)

    st.sidebar.divider()
    st.sidebar.subheader("🗣️ 英文家教設定")
    topic = st.sidebar.selectbox(
        "選擇練習情境：",
        ["日常輕鬆聊天 (Daily Chat)", "出國旅遊與點餐 (Travel & Food)", "基礎英文問答練習 (Beginner Q&A)"]
    )
    if st.sidebar.button("🗑️ 清除對話紀錄", use_container_width=True):
        st.session_state.en_messages = []
        st.session_state.last_audio_bytes = None
        st.rerun()

    if "en_messages" not in st.session_state:
        welcome_en = "Hi there! I'm your English tutor. What would you like to talk about today?"
        st.session_state.en_messages = [{
            "role": "assistant",
            "en_text": welcome_en,
            "zh_tip": "嗨！我是你的英文家教，今天想聊什麼呢？你可以直接按下方麥克風開口說，或打字給我喔！",
            "audio": text_to_speech(welcome_en, "en")
        }]
    if "last_audio_bytes" not in st.session_state:
        st.session_state.last_audio_bytes = None

    for msg in st.session_state.en_messages:
        with st.chat_message(msg["role"]):
            if msg["role"] == "user":
                st.write(msg["content"])
            else:
                st.markdown(f"**{msg['en_text']}**")
                if msg.get("zh_tip"):
                    st.caption(f"💡 {msg['zh_tip']}")
                if msg.get("audio"):
                    st.audio(msg["audio"], format="audio/mp3")

    system_prompt = f"""你是一位親切的英文口說家教，正在陪繁體中文學習者練習英文。情境：{topic}。
請嚴格按以下格式回覆：
[EN] 用自然簡單的英文回覆（2到3句），最後問一個簡單英文問題引導對方繼續說。
[ZH] 用繁體中文簡短翻譯剛才的英文，並給予溫柔的文法或用字建議與鼓勵。"""

    def process_tutor_reply(contents_payload, user_display_text):
        st.session_state.en_messages.append({"role": "user", "content": user_display_text})
        with st.chat_message("user"):
            st.write(user_display_text)

        with st.chat_message("assistant"):
            with st.spinner("AI 家教正在思考並生成語音..."):
                try:
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=contents_payload,
                        config=types.GenerateContentConfig(system_instruction=system_prompt, temperature=0.7)
                    )
                    raw_text = response.text.strip()
                    en_part = raw_text
                    zh_part = ""
                    if "[EN]" in raw_text and "[ZH]" in raw_text:
                        parts = raw_text.split("[ZH]")
                        en_part = parts[0].replace("[EN]", "").strip()
                        zh_part = parts[1].strip()
                    else:
                        en_part = raw_text.replace("[EN]", "").strip()

                    audio_data = text_to_speech(en_part, "en")
                    st.markdown(f"**{en_part}**")
                    if zh_part:
                        st.caption(f"💡 {zh_part}")
                    st.audio(audio_data, format="audio/mp3", autoplay=True)

                    st.session_state.en_messages.append({
                        "role": "assistant", "en_text": en_part, "zh_tip": zh_part, "audio": audio_data
                    })
                except Exception as e:
                    st.error(f"連線 AI 家教時發生錯誤：{e}")

    st.divider()
    audio_input = st.audio_input("🎤 點擊麥克風錄音說英文（錄完按停止即自動送出）")
    if audio_input is not None:
        current_bytes = audio_input.getvalue()
        if current_bytes != st.session_state.last_audio_bytes:
            st.session_state.last_audio_bytes = current_bytes
            audio_part = types.Part.from_bytes(data=current_bytes, mime_type="audio/wav")
            process_tutor_reply(
                [audio_part, "請聽我說的這段英文，先寫出你聽到的內容，再以家教身分用 [EN] 與 [ZH] 格式回覆我。"],
                "🎤 （已傳送語音訊息）"
            )

    user_text = st.chat_input("✍️ 也可以直接打字輸入英文（或用中文問怎麼說）...")
    if user_text:
        process_tutor_reply(user_text, user_text)

