import streamlit as st
import speech_recognition as sr

set_language_list = {
    "日本語":"ja",
    "英語":"en-US"
}

set_language = "日本語"

def file_speech_to_text(aoudio_file, set_language):
    with sr.AudioFile(aoudio_file) as source:
        aoudio = sr.Recognizer().record(source)

    try:
        text = sr.Recognizer().recognize_google(aoudio, language="ja")
    except:
        text = "音声認識に失敗しました"
    return text 


def mic_speech_to_text(set_language):
    with sr.Microphone() as source:
        aoudio = sr.Recognizer().listen(source)

        try:
            text = sr.Recognizer().recognize_google(aoudio, language="ja")

        except:
            text = "音声認識に失敗しました"
        
        return text


st.title("文字起こしアプリ")
st.write("音声認識する言語を選んでください。")
set_language = st.selectbox("音声認識する言語を選んでください。", set_language_list.keys())
current_language_state = st.empty()
current_language_state.write("選択中の言語" + set_language)
file_upload = st.file_uploader("ここに音声認識したファイルをアップロードしてください。", type=["wav"])

if (file_upload !=None):
    st.write("音声認識結果")
    result_text = file_speech_to_text(file_upload, set_language)
    st.write(result_text)
    st.write(file_upload)

st.write("マイクでの音声認識はこちらのボタンから")

if st.button("音声認識開始"):
    state = st.empty()
    state.write("音声認識中")
    result_text = mic_speech_to_text(set_language)
    st.write("音声認識結果")
    st.write(result_text)