# -*- coding: utf-8 -*-
import requests
import openai
import sys
import getpass
import os
from lxml import etree

username = getpass.getuser()
api_key = sys.argv[1]
novel_path_edit = sys.argv[2]
chapter_edit = sys.argv[3]
lang_edit = sys.argv[4]
openai.api_key = api_key
def choose(Jptext,lang):
    if(lang=="chinese"):
      return promptchinese(Jptext)
    else:
      return prompt(Jptext,lang)
        
def promptchinese(prompt):   
    response = openai.ChatCompletion.create(
       model ="gpt-3.5-turbo",
       messages=[
        {"role": "system", "content": "你是專業的輕小說翻譯員"},
        # {"role": "system", "content": "Please read the introduction and classification of this light novel:"},
        {"role": "user", "content":f"生動且有故事性的將此日文段落:'"+prompt+"'翻譯成「中文」"},
        ],
        temperature=1,
        max_tokens = 2047, 
     )
    
    return response['choices'][0]['message']['content'] 
def prompt(prompt,lang):   
    response = openai.ChatCompletion.create(
       model ="gpt-3.5-turbo",
       messages=[
        {"role": "system", "content": "You are a professional light novel translator，can translate various languages"},
        # {"role": "system", "content": "Please read the introduction and classification of this light novel:"},
        {"role": "user", "content":f"Translate this Japanese paragraph into '+{lang}+' vividly and with storytelling.:"+prompt},
        ],
        temperature=1,
        max_tokens = 2047, 
     )
    
    return response['choices'][0]['message']['content'] 

def get_text(url,key,path,lang):
    header = {
        'User-Agent': 
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        'AppleWebKit/537.36 (KHTML, like Gecko)'
        'Chrome/111.0.0.0 Safari/537.36'
    }
    
    count = 0
    Jptext = ''

    r = requests.get(url,headers=header)
    
    selector = etree.HTML(r.text.encode('utf-8'))
    
    title = selector.xpath('//*[@id="novel_color"]/p/text()')
    texts = selector.xpath('string(//*[@id="novel_honbun"])')
    
    with open(path +'\\'+str(key) + '、'+title[0],'w',encoding='UTF-8') as f:
        for i in texts:     
            Jptext+=i
            count=count+(len(i)*2)
            if(count>1450):
               storytext = choose(Jptext,lang)
               f.write(storytext)
               print(storytext)
            #    print(Jptext)
               count = 0
               Jptext=''
        if(count!=0):       
            storytext = choose(Jptext,lang)
            # f.write(Jptext)
            f.write(storytext)
            print(storytext)
            count = 0 
            Jptext=''                        
def path(address,count):
    page_counnt = address[-2]
    urls = [address[0:-2]+str(i)+'.html'.format(i) for i in range(int(page_counnt) ,int(page_counnt)+int(count))]
    return urls

if __name__ == "__main__":
    # address = input("please enter your adress: ")
    
    # storage_address = input(r"please enter your storage_adress: ")
    
    # count = input("please enter your storage_count: ")
    
    #  lang = input("please enter your lang: ")
    username = username.strip()

    storage_address = r"C:\\Users\\" + username + r"\\Desktop\\novel" 
    
    novel_path_edit = novel_path_edit.strip()  

    chapter_edit  = chapter_edit.strip()

    lang_edit  = lang_edit.strip().lower()
    
    if not os.path.isdir(storage_address):
         os.mkdir(storage_address)      
    
    urls =  path(novel_path_edit,chapter_edit) # concatenated address string
   
    key = novel_path_edit[-2]# chapter
    
    for i in urls:
        
        get_text(i,key,storage_address,lang_edit)
        
        key = str(int(key)+1)
