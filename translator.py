from numba import jit, cuda
from googletrans import Translator
from bs4 import BeautifulSoup
import time
import os

from timeit import default_timer as timer


@jit(target_backend='cuda')						
def translator(listHtml):
    translator = Translator()
    count = 0
    for ht in listHtml:
        html_file = open(ht,"r")
        soup = BeautifulSoup(html_file.read(), features='html.parser')
        html_file.close()
        b = []
        test1 = ['h3','h4','h5','h6','a']
        test2 = ['p','i','strong','small','b']
        test3 = ['em','abbr','address','bdo','blockquote']
        test4 = ['q',"code","ins","del","dfn"]
        test5 = ['pre','samp','var','br','h2']
        test6 = ['p','u','cite','kbd']
        test7 = ['li','span','title','button','h1']
        test8 = ['div','label']
        for i in test1:            
            for j in soup.find_all(i):                
                b.append(j)

        for i in test2:
            for j in soup.find_all(i):
                b.append(j)
        for i in test3:
            for j in soup.find_all(i):
                b.append(j)
        for i in test4:
            for j in soup.find_all(i):
                b.append(j)
        for i in test5:
            for j in soup.find_all(i):
                b.append(j)
        for i in test6:
            for j in soup.find_all(i):
                b.append(j)

        for i in test7:
            for j in soup.find_all(i):
                b.append(j)
        for i in test8:
            for j in soup.find_all(i):
                b.append(j)
    
        html_file = open(ht, "w")
        for tag in b:
            if(tag.string is not None):
                translation = translator.translate(tag.string, dest='hi')
                #time.sleep(60)
                print(tag.string)
                print(translation.text)
                tag.string.replace_with(translation.text)
            

     
            else:
                pass
        count += 1
    

        new_text = soup.prettify()
        html_file.write(new_text)
        html_file.close()
        time.sleep(30) 



        print("--------------------------------------")
        print("-----------End of {} Round-----------------".format(count))
        print("--------------------------------------")



if __name__=="__main__":

    listHtml = [
        '/home/volki/Downloads/tmp/www.classcentral.com/collections.html',
        '/home/volki/Downloads/tmp/www.classcentral.com/index.html',
        '/home/volki/Downloads/tmp/www.classcentral.com/institutions.html',
        '/home/volki/Downloads/tmp/www.classcentral.com/lists.html',
        '/home/volki/Downloads/tmp/www.classcentral.com/login.html',
        '/home/volki/Downloads/tmp/www.classcentral.com/most-popular-courses.html',
        '/home/volki/Downloads/tmp/www.classcentral.com/new-online-courses.html',
        '/home/volki/Downloads/tmp/www.classcentral.com/providers.html',
        '/home/volki/Downloads/tmp/www.classcentral.com/rankings.html',
        '/home/volki/Downloads/tmp/www.classcentral.com/signup.html',
        '/home/volki/Downloads/tmp/www.classcentral.com/starting-this-month.html',
        '/home/volki/Downloads/tmp/www.classcentral.com/subjects.html',
        '/home/volki/Downloads/tmp/www.classcentral.com/universities.html'
    ]
             




    subject = os.listdir('/home/volki/Downloads/tmp/www.classcentral.com/subject/')
    for i in subject:
        tmp = '/home/volki/Downloads/tmp/www.classcentral.com/subject/{}'.format(i)
        listHtml.append(tmp)

    collection = os.listdir('/home/volki/Downloads/tmp/www.classcentral.com/collection/')
    for i in collection:
        tmp1 = '/home/volki/Downloads/tmp/www.classcentral.com/collection/{}'.format(i)
        listHtml.append(tmp1)
    
    course = os.listdir('/home/volki/Downloads/tmp/www.classcentral.com/course/')
    for i in course:
        tmp2 = '/home/volki/Downloads/tmp/www.classcentral.com/course/{}'.format(i)
        listHtml.append(tmp2)
    
    helpp = os.listdir('/home/volki/Downloads/tmp/www.classcentral.com/help/')
    for i in helpp:
        tmp3 = '/home/volki/Downloads/tmp/www.classcentral.com/helpp/{}'.format(i)
        listHtml.append(tmp3)
    
    institution = os.listdir('/home/volki/Downloads/tmp/www.classcentral.com/institution/')
    for i in institution:
        tmp4 = '/home/volki/Downloads/tmp/www.classcentral.com/institution/{}'.format(i)
        listHtml.append(tmp4)
    
    provider = os.listdir('/home/volki/Downloads/tmp/www.classcentral.com/provider/')
    for i in provider:
        tmp5 = '/home/volki/Downloads/tmp/www.classcentral.com/provider/{}'.format(i)
        listHtml.append(tmp5)
    
    report = os.listdir('/home/volki/Downloads/tmp/www.classcentral.com/report/')
    for i in report:
        tmp6 = '/home/volki/Downloads/tmp/www.classcentral.com/report/{}'.format(i)
        listHtml.append(tmp6)
    
    university = os.listdir('/home/volki/Downloads/tmp/www.classcentral.com/university/')
    for i in university:
        tmp7 = '/home/volki/Downloads/tmp/www.classcentral.com/university/{}'.format(i)
        listHtml.append(tmp7)
    
    
    start = timer()
    translator(listHtml)
    print("with GPU:", timer()-start)
