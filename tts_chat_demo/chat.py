#python3.x
#aip是百度语言识别AI库，可以到百度免费使用
from pyaudio import PyAudio,paInt16
import numpy as np
from datetime import datetime
import wave
from aip import speech
import requests
import pyttsx

#封装成类
class Chat(object):
    """docstring for Chat"""
    def __init__(self):
        pass      
    #保存二进制数据成wav文件（这里主要是对直接使用二进制还有问题）
    def save_wave_file(self,filename, data):
        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(8000)
        wf.writeframes(b"".join(data))
        wf.close()
    #获取用户输入并保存音频，主要借鉴下面网址
    #http://xbd.xao.ac.cn/sites/scipydoc/wave_pyaudio.html#id5
    def get_audio(self):
        NUM_SAMPLES = 2000
        SAMPLING_RATE = 8000
        LEVEL = 1500
        COUNT_NUM = 20
        SAVE_LENGTH = 5

        pa = PyAudio()
        stream = pa.open(format=paInt16, channels=1, rate=SAMPLING_RATE, input=True, frames_per_buffer=NUM_SAMPLES)

        save_count = 0
        save_buffer = []

        while True:
            string_audio_data = stream.read(NUM_SAMPLES)

            audio_data = np.fromstring(string_audio_data, dtype=np.short)

            large_sample_count = np.sum(audio_data>LEVEL)

            print(np.max(audio_data))

            if large_sample_count>COUNT_NUM:
                save_count = SAVE_LENGTH
            else:
                save_count -= 1

            if save_count < 0:
                save_count = 0

            if save_count > 0:
                save_buffer.append(string_audio_data)
            else:
                if len(save_buffer) > 0:
                    filename = "tmp.wav" 
                    self.save_wave_file(filename, save_buffer)
                    return
    #用百度api语音识别，这里需要填写的三个参数是在百度AI得到
    def trans_audio_to_words(self):
        s = speech.AipSpeech("参数1","参数2","参数3")
        f = open("tmp.wav","rb")
        res = s.asr(speech=f.read(),format="wav",rate=8000,options={'lan':'zh'})
        print(res)
        if res['err_no']==0:
            return res['result']
        else:
            return ""
    #获取图灵机器人的谈话交互数据，这里要写key，在图灵机器人得到
    def connect_robot(self,info):
        data = {
            "key":"参数key",
            "info":info,
            "usid":"123456",
        }
        res = requests.post("http://www.tuling123.com/openapi/api",data=data)
        res_data = res.json()
        print(res_data)
        if res_data['code']==100000:
            return res_data['text']
        else:
            return "不能识别"
    #使用tts读返回文字
    def tts(self,words):
        engine = pyttsx.init()
        engine.say(words)
        engine.runAndWait()

#类使用方法
if __name__=='__main__':
    chat = Chat()
    while True:
        chat.get_audio()
        words = chat.trans_audio_to_words()
        if words == "":
            print("error")
        else:
            rres = chat.connect_robot(words)
            chat.tts(rres)