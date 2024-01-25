# -*- coding: UTF-8 -*-
from setuptools import setup
import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

alllist = [
        ('', ['algorithmLib/DLLs/p563.dll']),
        ('', ['algorithmLib/DLLs/g160.dll']),
        ('', ['algorithmLib/DLLs/cygwin1.dll']),
        ('', ['algorithmLib/DLLs/peaqb.exe']),
        ('', ['algorithmLib/DLLs/PY_PESQ.dll']),
        ('', ['algorithmLib/DLLs/matchsig.dll']),
        ('', ['algorithmLib/DLLs/snr_music.dll']),
        ('', ['algorithmLib/DLLs/snr_transient.dll']),
        ('', ['algorithmLib/DLLs/agcDelay.dll']),
        ('', ['algorithmLib/DLLs/attackrelease.dll']),
        ('', ['algorithmLib/DLLs/gaintable.dll']),
        ('', ['algorithmLib/DLLs/musicStability.dll']),
        ('', ['algorithmLib/DLLs/matchsig_aec.dll']),
        ('', ['algorithmLib/DLLs/ERLE_estimation.dll']),
        ('', ['algorithmLib/DLLs/pcc.dll']),
        ('', ['algorithmLib/DLLs/p563.dylib']),
        ('', ['algorithmLib/DLLs/g160.dylib']),
        ('', ['algorithmLib/DLLs/PY_PESQ.dylib']),
        ('', ['algorithmLib/DLLs/matchsig.dylib']),
        ('', ['algorithmLib/DLLs/snr_music.dylib']),
        ('', ['algorithmLib/DLLs/snr_transient.dylib']),
        ('', ['algorithmLib/DLLs/agcDelay.dylib']),
        ('', ['algorithmLib/DLLs/attackrelease.dylib']),
        ('', ['algorithmLib/DLLs/gaintable.dylib']),
        ('', ['algorithmLib/DLLs/musicStability.dylib']),
        ('', ['algorithmLib/DLLs/matchsig_aec.dylib']),
        ('', ['algorithmLib/DLLs/ERLE_estimation.dylib']),
        ('', ['algorithmLib/DLLs/pcc.dylib']),
        ('', ['algorithmLib/DLLs/p563.so']),
        ('', ['algorithmLib/DLLs/g160.so']),
        ('', ['algorithmLib/DLLs/matchsig.so']),
        ('', ['algorithmLib/DLLs/snr_music.so']),
        ('', ['algorithmLib/DLLs/snr_transient.so']),
        ('', ['algorithmLib/DLLs/agcDelay.so']),
        ('', ['algorithmLib/DLLs/attackrelease.so']),
        ('', ['algorithmLib/DLLs/gaintable.so']),
        ('', ['algorithmLib/DLLs/musicStability.so']),
        ('', ['algorithmLib/DLLs/matchsig_aec.so']),
        ('', ['algorithmLib/DLLs/ERLE_estimation.so']),
        ('', ['algorithmLib/DLLs/pcc.so']),
        ('', ['algorithmLib/DLLs/SC_res_retrain_220316_185754125621__ep_007.tar']),
        ('', ['algorithmLib/DLLs/silero_vad.jit']),
]
setup(
    name='AlgorithmLib',
    version='4.0.35',
    packages=setuptools.find_packages(),
    url='https://github.com/pypa/sampleproject',
    license='MIT',
    author=' MA JIANLI',
    author_email='majianli@corp.netease.com',
    description='audio algorithms to compute and test audio quality of speech enhencement',
    long_description="""
        Audio test libs to compute audio quality and 3A performance by objective metrics
    pcm,wav inputfiles is allowed,support different samplerate (invalid params are simply corrected to valid ones)
    
    # How to install ?
    #Install with pip:
    
    simply use pip to install this toolkit
    
    "pip install algorithmLib"
    
    # How to use?
    
        #just see ./demos/ 	
    
    #  PESQ example
    src = "a.pcm"
    test = "b.pcm"
    
    score = compute_audio_quality('PESQ',testFile=test,refFile=src,samplerate=16000)
    
    or
    
    src = "a.wav"
    test = "b.wav"
    
    score = compute_audio_quality('PESQ',testFile=test,refFile=src)
    #  G160 example
    src = "a.wav"
    test = "b.wav"
    cle = "c.wav"
    tnlr,nplr,snri,dsn  = compute_audio_quality("G160",testFile=test,refFile=src,cleFile=cle)
    or 
    src = "a.pcm"
    test = "b.pcm"
    cle = "c.pcm"
    tnlr,nplr,snri,dsn  = compute_audio_quality("G160",testFile=test,refFile=src,cleFile=cle,samplerate=48000)
    #p563 example
    test = "a.wav"
    Mos,SpeechLevel,Snr,NoiseLevel = compute_audio_quality('P563',testFile=test)
    :param metrics: G160/P563/POLQA/PESQ/STOI/STI/PEAQ/SDR/SII/LOUDNESS/MUSIC/MATCH/
                    TRANSIENT/GAINTABLE/ATTACKRELEASE/MUSICSTA/AGCDELAY/MATCHAEC/
                    ERLE/SLIENCE/FORMAT/AECMOS/AIMOS/TRMS/ARMS/PRMS/SRMS/LRATE/NOISE/CLIP/DELAY/ECHO/SPEC/PITCH/EQ，必选项
    # G160 无采样率限制；  WAV/PCM输入 ；三端输入: clean、ref、test；无时间长度要求；
    # P563 8000hz(其他采样率会强制转换到8khz)；  WAV/PCM输入 ；单端输入: test；时长 < 20s；
    # POLQA 窄带模式  8k  超宽带模式 48k ；WAV/PCM输入 ；双端输入：ref、test；时长 < 20s；
    # PESQ 窄带模式  8k   宽带模式 16k ；WAV/PCM输入 ；双端输入：ref、test；时长 < 20s；
    # STOI 无采样率限制; 双端输入：ref、test；无时间长度要求；
    # STI >8k(实际会计算8khz的频谱)； WAV/PCM输入 ；双端输入：ref、test；时长 > 20s
    # PEAQ 无采样率限制；WAV/PCM输入 ；双端输入：ref、test；无时间长度要求；
    # SDR 无采样率限制; WAV/PCM输入 ; 双端输入：ref、test；无时间长度要求；
    # MATCH 无采样率限制; WAV/PCM输入;三端输入：ref、test、out； 无时间长度要求；
    # MUSIC 无采样率限制;WAV/PCM输入;双端输入：ref、test；无时间长度要求；
    # TRANSIENT 无采样率限制,WAV/PCM输入;三端输入：cle、noise、test； 无时间长度要求；
    # GAINTABLE 无采样率限制,WAV/PCM输入;双端输入：ref、test；固定信号输入；
    # ATTACKRELEASE 无采样率限制,WAV/PCM输入;双端输入：ref、test；固定信号输入；
    # MUSICSTA 无采样率限制,WAV/PCM输入;双端输入：ref、test；无时间长度要求；
    # AGCDELAY 无采样率限制,WAV/PCM输入;双端输入：ref、test；无时间长度要求；
    # MATCHAEC 无采样率限制 WAV/PCM输入;三端输入：ref、mic,test，；无时间长度要求；
    # ELRE 无采样率限制 WAV/PCM输入;三端输入：mic,ref、test；无时间长度要求；
    # SLIENCE 无采样率限制 WAV/PCM/MP4输入;单端输入：test；无时间长度要求；
    # FORMAT 无采样率限制 WAV/MP4输入;单端输入：test；无时间长度要求；
    # AECMOS 无采样率限制 WAV/PCM输入 ；三端输入：mic,ref、test；无时间长度要求；
    # AIMOS 无采样率限制 WAV/PCM输入 ；单端输入：test；无时间长度要求；
    # TRMS 无采样率限制 WAV/PCM输入 ；单端输入：test；无时间长度要求；
    # ARMS 无采样率限制 WAV/PCM输入 ；单端输入：test；无时间长度要求；
    # PRMS 无采样率限制 WAV/PCM输入 ；单端输入：test；无时间长度要求；
    # SRMS 无采样率限制 WAV/PCM输入 ；单端输入：test；无时间长度要求；
    # LRATE 无采样率限制 WAV/PCM输入 ；单端输入：test；无时间长度要求；
    # NOISE 无采样率限制 WAV/PCM输入 ；双端输入：ref、test；无时间长度要求；
    # CLIP 无采样率限制 WAV/PCM输入 ；单端输入：test；无时间长度要求；
    # DELAY 无采样率限制; WAV/PCM输入;双端输入：ref、test； 无时间长度要求；
    # ECHO 无采样率限制; WAV/PCM输入;双端输入：ref、test； 无时间长度要求；
    # SPEC 无采样率限制; WAV/PCM输入;单端输入：test； 无时间长度要求；
    # PITCH 无采样率限制；WAV/PCM输入;双端输入：ref、test； 无时间长度要求；
    # EQ 无采样率限制；WAV/PCM输入;双端输入：ref、test； 无时间长度要求；
    # MATCH2 无采样率限制; WAV/PCM输入;三端输入：ref、test、out； 无时间长度要求；
    # MATCH3 无采样率限制; WAV/PCM输入;三端输入：ref、test、out； 无时间长度要求；
    不同指标输入有不同的采样率要求，如果传入的文件不符合该指标的要求，会自动变采样到合法的区间
    :param testFile: 被测文件，必选项
    :param refFile:  参考文件，可选项，全参考指标必选，比如POLQA/PESQ/PEAQ
    :param micFile:  micIN，可选项，回声指标必选，MATCHAEC/ELRE/AECMOS
    :param cleFile:  干净语音文件，可选项，G160,TRANSIENT需要
    :param noiseFile 噪声文件，可选项，突发噪声信噪比计算需要
    :param aecCaliFile 用于做AEC对齐的校准文件  MATCHAEC专用
    :param outFile 输出文件，可选项，对齐文件可选
    :param samplerate: 采样率，可选项，pcm文件需要 default = 16000
    :param bitwidth: 比特位宽度，可选项，pcm文件需要 default = 2
    :param channel: 通道数，可选项，pcm文件需要 default = 1
    :param refOffset: ref文件的样点偏移，可选项，指标G160需要
    :param testOffset: test文件的样点偏移，可选项，指标G160需要
    :param maxComNLevel: 测试G160文件的最大舒适噪声
    :param speechPauseLevel 测试G160文件的语音间歇段的噪声
    :param audioType  输入音频的模式 0：语音 1：音乐 MATCH/GAINTABLE需要
    :param aecStartPoint  计算AECMOS，选择从第几秒开始计算
    :param aecTargetType  0:Chiness 1:English 2:Single Digit 3:Music  计算MATCHAEC/ELRE
    :param aecScenario 计算aec mos专用     0:'doubletalk_with_movement', 1:'doubletalk', 2:'farend_singletalk_with_movement', 3:'farend_singletalk', 4:'nearend_singletalk'
    :param rmsCalsection 计算rms的区间 TRMS和ARMS需要，时间单位s，比如：[1,20]
    :param polqaMode 计算polqa的模式 0:默认模式  1: 理想模式：排除小声音的影响，把声音校准到理想点平 -26db
    :param pitchLogMode 计算pitch的模式 0：线性模式，用于SetLocalVoicePitch接口; 1：对数模式,用于SetAudioMixingPitch接口；默认为1
    :param fineDelaySection 精准计算延时(MTACH3)，需要手动标出语音块的位置，比如有三段：speech_section=[[2.423,4.846],[5.577,7.411],[8,10.303]]
    :return:
    """,
    long_description_content_type="text/markdown",
    install_requires=[
    'numpy',
    'wave',
    'matplotlib',
    'datetime',
    'scipy',
    'pystoi',
    'paramiko',
    'moviepy',
    'torch',
    'torchaudio',
    'librosa',
    'requests',
    'pandas',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    data_files=[
        ('', ['algorithmLib/DLLS/p563.dll']),
        ('', ['algorithmLib/DLLS/g160.dll']),
        ('', ['algorithmLib/DLLS/cygwin1.dll']),
        ('', ['algorithmLib/DLLS/peaqb.exe']),
        ('', ['algorithmLib/DLLS/PY_PESQ.dll']),
        ('', ['algorithmLib/DLLS/matchsig.dll']),
        ('', ['algorithmLib/DLLS/snr_music.dll']),
        ('', ['algorithmLib/DLLS/snr_transient.dll']),
        ('', ['algorithmLib/DLLS/agcDelay.dll']),
        ('', ['algorithmLib/DLLS/attackrelease.dll']),
        ('', ['algorithmLib/DLLS/gaintable.dll']),
        ('', ['algorithmLib/DLLS/musicStability.dll']),
        ('', ['algorithmLib/DLLS/matchsig_aec.dll']),
        ('', ['algorithmLib/DLLS/ERLE_estimation.dll']),
        ('', ['algorithmLib/DLLS/pcc.dll']),
        ('', ['algorithmLib/DLLS/p563.dylib']),
        ('', ['algorithmLib/DLLS/g160.dylib']),
        ('', ['algorithmLib/DLLS/PY_PESQ.dylib']),
        ('', ['algorithmLib/DLLS/matchsig.dylib']),
        ('', ['algorithmLib/DLLS/snr_music.dylib']),
        ('', ['algorithmLib/DLLS/snr_transient.dylib']),
        ('', ['algorithmLib/DLLS/agcDelay.dylib']),
        ('', ['algorithmLib/DLLS/attackrelease.dylib']),
        ('', ['algorithmLib/DLLS/gaintable.dylib']),
        ('', ['algorithmLib/DLLS/musicStability.dylib']),
        ('', ['algorithmLib/DLLS/matchsig_aec.dylib']),
        ('', ['algorithmLib/DLLS/ERLE_estimation.dylib']),
        ('', ['algorithmLib/DLLS/pcc.dylib']),
        ('', ['algorithmLib/DLLS/p563.so']),
        ('', ['algorithmLib/DLLS/g160.so']),
        ('', ['algorithmLib/DLLS/matchsig.so']),
        ('', ['algorithmLib/DLLS/snr_music.so']),
        ('', ['algorithmLib/DLLS/snr_transient.so']),
        ('', ['algorithmLib/DLLS/agcDelay.so']),
        ('', ['algorithmLib/DLLS/attackrelease.so']),
        ('', ['algorithmLib/DLLS/gaintable.so']),
        ('', ['algorithmLib/DLLS/musicStability.so']),
        ('', ['algorithmLib/DLLS/matchsig_aec.so']),
        ('', ['algorithmLib/DLLS/ERLE_estimation.so']),
        ('', ['algorithmLib/DLLS/pcc.so']),
        ('', ['algorithmLib/DLLS/SC_res_retrain_220316_185754125621__ep_007.tar']),
        ('', ['algorithmLib/DLLS/silero_vad.jit'])],

    python_requires='>=3.6',
)



