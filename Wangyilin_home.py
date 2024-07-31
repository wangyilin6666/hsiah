'''我的主页'''

import streamlit as st
from PIL import Image
page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

def page1():
    '''我的兴趣推荐'''
    st.title(':red[这是我的兴趣推荐]')
    st.header("这是一首好听的音乐")
    with open('oksodjsodj.mp3.mp3', 'rb') as f:
        mymp3 = f.read()
    with open("海棠不言 - 编程猫的梦想.mp3", 'rb') as f:
        mp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time = 0)
    st.audio(mp3, format='audio/mp3', start_time = 0)
    ak1, ak2 = st.tabs(['**分类一**', '**分类二**'])
    with ak1:
        st.header("这是我喜欢的一张二战地图")
        st.image("erzhan.jpg")
        st.write("我喜欢编程打篮球跑步和游泳，变成让我充盈生活，运动锻炼身体")
        st.write(":blue[我最喜欢**环太1**这部电影，我喜欢看八十天环游地球这本书非常有意思，我最难忘的一次旅行是去四川玩，非常酷，火锅很好吃。]")
        st.image("476a71397eb85426c6167097dba97c0c.jpeg")
    with ak2:
        st.header("分享一些喜欢的**宇宙**图片")
        st.image("as.jpg")
        st.image("gf.png")
        st.image("skdj.jpeg")
        st.image("3d481af78a8404ecbf3b081dc3f43ef7.jpg")
        st.image("6d2a6ab0a6def98758643ccc7729cd99.jpeg")
        st.image("10c219171d963a8fdc9d748a908be209.jpeg")
        st.image("40d94b7e2835445e14800e08bb7fb1d9.jpeg")
        st.image("ba69cf115f89708d46161e7509e4043c.jpeg")
        

def page2():
    '''我的图片处理工具'''
    st.header(":sunglasses:图片转换小程序:sunglasses:(超有用)")
    uploaded_file = st.file_uploader(':red[上传图片]', type=['png', 'jpg', 'jpeg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)

        tab1, tab2, tab3, tab4 = st.tabs([':blue[原图]', "改色1", "改色2","改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))

def page3():
    '''我的智慧词典'''
    st.write('智慧词典')
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]

    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] =times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数:', times_dict[n])
    if word == "wyl":
        st.code('''
                # 恭喜你触发菜单，这是一段python代码
                print("what a smart boy")#''')
        st.balloons()
    if word == "python":
        st.code('''
                # 你难道喜欢编程？那真是太棒了
                print("you are so good!")
                ''')
    if word == "snow":
        st.snow()

def page4():
    '''我的留言区'''
    st.write('我的留言区')
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1], ':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🍥'):
                st.text(i[1] + i[2])
    name = st.selectbox('我是.....', ['阿短','编程猫'])
    new_message = st.text_input('想要说的话....')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)


if page == '我的兴趣推荐':
    page1()
elif page == '我的图片处理工具':
    page2()
elif page == '我的智慧词典':
    page3()
elif page == '我的留言区':
    page4()