from django.shortcuts import render

# Create your views here.
djangoprojects=[
                {'title':'Notes','image':'Notes/Notes1.png','tags':['#Python','#Django','#user_authentication','#user_password_reset'],'link':'https://web-production-ee01.up.railway.app/'},
                {'title':'News','image':'News/News2.jpeg','tags':['#Python','#Django','#user_authentication','#user_password_reset','#personalized_results'],'link':'https://news-app-django-final-production.up.railway.app/'},
                {'title':'Blog','image':'Blog/Blog1.jpeg','tags':['#Python','#Django','#user_authentication','#user_password_reset'],'link':'https://web-production-9a4f.up.railway.app/'},
                ]
pythonprojects=[
                {'title':'Snake','image':'Snake/Snake.jpeg','tags':['#Python','#Tkinter'],'link':'https://github.com/Jeman1997/Snake-Game'},
                {'title':'Pong','image':'Pong/Pong.jpeg','tags':['#Python','#Tkinter'],'link':'https://github.com/Jeman1997/Pong'},
                {'title':'Spotify Top 100 Songs','image':'SpotifyScrape/spotifytop100.jpeg','tags':['#Python','#Tkinter','#WebScraping'],'link':''}
                ]
def home(request):
    cont={'req':'All','proj':djangoprojects+pythonprojects}
    if request.method=='POST':
        cont={'req':request.POST['button']}
        btn =request.POST['button']
        if btn=='All':
            cont['proj']=djangoprojects+pythonprojects
        elif btn=='Django':
            cont['proj']=djangoprojects
        elif btn=='Python':
            cont['proj']=pythonprojects
    return render(request,'home.html',cont)
