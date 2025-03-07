import streamlit as st
from backend import ChatbotBackend

st.set_page_config(page_title='Nana Chatbot', page_icon="https://cdn.discordapp.com/attachments/1277618316986552414/1346137000008486953/na1.png?ex=67c71746&is=67c5c5c6&hm=bee9236443834d230d9e8fb3fd037d0460856bbd50c8c389cd0f9d8ae01b02aa&", layout="wide")


st.markdown('''
            <style>
                @keyframes gradientAnimation {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
                .div_head {
                font-size: 60px;
                font-weight: bold;
                background: linear-gradient(45deg,white, #ffc41a, #ff551a);
                background-size: 300% 300%;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                animation: gradientAnimation 3s infinite linear;
                text-align: center;
                
            }




                .more_detail{
                        border: 2px solid white;
                        width: 20%; 
                        position: fixed;
                        text-align: center;
                        background-color: #e75b00;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        height: 100px;
                        font-size: 40px;
                        transition: ease-in-out 0.3s, border-radius 0.3s;
                        }
                .more_detail:hover{
                            border-radius: 40px
                            
            
                            }
                .left_down{
                            border: 2px solid blue;
                            width: 20%; 
                           
                            position: fixed;
                            top:200px;
                            display: flex;

                            justify-content: center;
                            align-items: center;
                            transition: ease 0.3s, transform 0.3s, border 0.1s, background 0.3s, border-radius 0.3s;
                            }
                .left_down:hover{
                            transform: scale(1.1);
                            border: 2px solid #03f0ff;
                            background-color: blue;
                            border-radius: 30px;
                            }
                .ollama_border{
                        width: 80%;
                          
                        display: flex;
                        justify-content: space-between;
                        height: auto;
            
                        }
                .ollama-name{
                            
                            width: 35%;
                            font-size: 30px;
                            display: flex;
                            align-items: center;  
                            justify-content: center;
                            
                            
                            }
                .ollama-name:hover{
                           

            
            
                            }
                .ollama-image{
                            width: 65%;
                            padding: 20px;
                            border: 2px solid transparent;
                            }
                .contact{
                        border-width: 4px;
                        border-style: solid;
                        border-image: linear-gradient(to right, #e70000 50%, #0022e7 50%)1;          
            
                        position: fixed;
                        display: flex;
                        align-items: center;
                        justify-content: space-around;
                        width: 20%;
                        top: 410px;
                        background: linear-gradient(to right, #6d1717 50%, #18176d 50%);
                        transition: ease 0.3s, transform 0.3s;            
            }      
                .contact:hover{
                    transform: scale(1.1);
                    
            }


                .youtube{
                        width: 50%;
                        transition: ease 0.3s, transform 0.3s;
                        }      
                .youtube:hover{
                        transform: scale(1.3);
            }

                .facebook{
                        width: 50%;
                        transition: ease 0.3s, transform 0.3s;
                }
                .facebook:hover{
                        transform: scale(1.3);
            }
                .header{
                    display: flex;
                    justify-content: space-around;
                    width: 100%;
                    height: auto;
                    align-items: center;
                    
                    
                    }
                .header-text{
                   
            }
                .nana-main{
                    width: 170px;
                    
                }
                .user_his {
                display: flex;
                justify-content: flex-end;
                align-items: center;
                margin: 10px 0;
                padding-right: 3%;
                transition: ease 0.3s, transform 0.3s;
                
                }
                
                .img-user{
                    width:50px;
                    border-radius: 100%;
                    border: 2px solid white;
                    background-color: #5b5b5b;
                    margin-right: 3.5%;
                }
                .text-user{
                    color: white;
                    background-color: #5b5b5b;
                    padding: 10px;
                    border: 2px solid transparent;
                    border-radius: 10px;
                    max-width: 60%; 
                    text-align: right;
                    right: 20px;
                    margin-right: 3.5%;
                    transition: ease 0.3s, transform 0.3s, border 0.3s;
                }
                .text-user:hover{
                    transform: scale(1.1);
                    border: 2px solid white;
                    }
                .bot_his {
                        display: flex;
                        justify-content: flex-start;
                        align-items: center;
                        margin: 10px 0;
                        padding-left: 3%;
                        

                        }
                .img-bot{
                        width:50px;
                        border-radius: 100%;
                        border: 2px solid white;
                        background-color: #df6c16;
                        }
                .text-bot {
                    color: white;
                    background-color: #df6c16;
                    padding: 10px;
                    border-radius: 10px;
                    border: 2px solid transparent;
                    max-width: 60%;
                    text-align: left;
                    margin-left: 3.5%;
                    transition: ease 0.3s,transform 0.3s, border 0.3s; 
                }
                .text-bot:hover{
                    transform: scale(1.1);
                    border: 2px solid white;
                    }

                .main{
                    border: 2px solid red;
                    padding: 10px;
                    height: auto;
                    width: 90%;
                    }
            </style>
            '''
            ,unsafe_allow_html=True)    



if "chatbot" not in st.session_state:
    st.session_state.chatbot = ChatbotBackend("phi3")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
with st.sidebar:
    st.markdown('''
                    <div class="more_detail" >
                            More details
                    </div>
                ''',unsafe_allow_html=True)
    st.markdown('''
                    <div class="left_down">
                        <div class="ollama_border">
                            <div class="ollama-name" >
                                Model Phi3 :
                            </div>
                            <div class="ollama-image" >
                                <a href="https://ollama.com/library/phi3"> 
                                    <img src="https://media.licdn.com/dms/image/v2/D5612AQEOULWgnVbBRA/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1713098774047?e=2147483647&v=beta&t=ci_6MctI3jG8VK_mPNiyGuno_3ePW_IEJKCjACj2gCg">
                                </a>
                            </div>
                        </div>
                    </div>
                    <div class="contact" >
                            <div class="youtube"> 
                                <a href="https://www.youtube.com/channel/UC8xdysF9v4nd3y85mVDUz5Q/">
                                    <img  src="https://cdn.discordapp.com/attachments/1277618316986552414/1346842777350307891/1.png?ex=67c9a895&is=67c85715&hm=972e025eadf5f2f4c170d5b8b9a989a5d83f991796e6f324a9ef008f37093c47&">
                                </a>
                            </div>
                            <div class="facebook">
                                <a href="https://www.facebook.com/kaythip.kritsanadacha/about">
                                    <img  src="https://cdn.discordapp.com/attachments/1277618316986552414/1346842680247980092/f0e39958d12df7df.png?ex=67c9a87e&is=67c856fe&hm=a1f40e39cbabdcd12b5756e37acd21f70de2391d2b9622dd7a0fb166ef58d6f5&">
                                </a>
                            </div>
                    </div>
                ''' ,unsafe_allow_html=True)

 
with st.container():
    st.markdown(f'''
                    <div class="header">
                        <div style="header-text">
                        <span class="div_head">
                            Welcome to Nana Chatbot!
                        </span>
                        </div>
                        <div class="nana-main">
                            <img src="https://cdn.discordapp.com/attachments/1277618316986552414/1346137000008486953/na1.png?ex=67c91186&is=67c7c006&hm=f35e888217e56b5f6b2a087bad15676734e8342e85a1dd0ea77ed0073414ed17&">
                        </div>
                    </div>
                ''',unsafe_allow_html=True)
for sender, message in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f'''
            <div class="user_his">
                <img class="img-user" src="https://cdn.discordapp.com/attachments/1277618316986552414/1346146752855801897/ki1.png?ex=67c7205c&is=67c5cedc&hm=677587b6745e816cbd3f9897c37c560dc0293431aa5f014a7c7e6a41d1c5bf91&">
                <div class="text-user"> You: {message}</div>
            </div>
    ''', unsafe_allow_html=True)
    else:
        st.markdown(f'''
            <div class="bot_his">
                <img class="img-bot" src="https://cdn.discordapp.com/attachments/1277618316986552414/1346137000008486953/na1.png?ex=67c91186&is=67c7c006&hm=f35e888217e56b5f6b2a087bad15676734e8342e85a1dd0ea77ed0073414ed17&">
                <div class="text-bot"> Nana: {message}</div>
            </div>
        ''', unsafe_allow_html=True)    
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message:", key="user_input")
    submitted = st.form_submit_button('Send')

if submitted and user_input:
    chatbot = st.session_state.chatbot
    response = chatbot.get_resoponse(user_input)  # ดึงคำตอบจาก backend
    # บันทึกประวัติแชท
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", response))
    # อัปเดต UI ทันที
    st.rerun()