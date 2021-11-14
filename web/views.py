from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
# Create your views here.

from .models import Articles
from .models import My_selected
from .models import Category

from random import randrange

def NoDataError():
    return HttpResponse("no data in database")


def normalize_upload_path(article_obj):
    try:
        for i in article_obj:
            false_path = i.title_photo
            true_path = str(false_path).replace('web','')
            slug = str(i.slug)
            article = Articles.objects.filter(slug=f'{slug}')
            article.update(title_photo=str(true_path))
    except TypeError:
            false_path = article_obj.title_photo
            true_path = str(false_path).replace('web','')
            slug = str(article_obj.slug)
            article = Articles.objects.filter(slug=f'{slug}')
            article.update(title_photo=str(true_path))

def select_random_obj(data_base_name,num_for_return):
    
    article_all = Articles.objects.all()
    count = Articles.objects.count()
    numbers = []
    for i in range(0,100):
        if len(numbers) == num_for_return:
            break

        random = randrange(0,count)
        if random not in numbers:
            numbers.append(random)

    articles_select = []
    for i in numbers:
        selected =  article_all[i]
        articles_select.append(selected)

    return articles_select

def index(request):
    
    # get 4 last article for show in widget popular posts
    All_article = Articles.objects.all()
    count_article = len(All_article)
    article_1 = All_article[int(count_article)-1]
    normalize_upload_path(article_1)

    article_2 = All_article[int(count_article)-2]
    normalize_upload_path(article_2)

    article_3 = All_article[int(count_article)-3]
    normalize_upload_path(article_3)

    article_4 = All_article[int(count_article)-4]
    normalize_upload_path(article_4)

    # select random articles for top site
    articles_random = select_random_obj(Articles,6)
    # set sleceted article for starts
    my_select = My_selected.objects.first()

    all_Cats = []
    all_count_Cats = []
    Cats = Category.objects.all()
    for i in Cats:
        cat_ar = Articles.objects.filter(category_name=i).count() 
        all_count_Cats.append(cat_ar)
        all_Cats.append(i)
    
   
    context = {
        'article_1':article_1,
        'article_2':article_2,
        'article_3':article_3,
        'article_4':article_4,
        'top_one_articles':articles_random[:3],
        'top_two_articles':articles_random[3:],
        'all_cats':all_Cats,
        'all_count_cats':all_count_Cats,
        'title_name':'Home',
        'my_select':my_select,
    }
    
    return render(request,'index.html',context)




def single_post(request,slug):

    # get main article for show
    article = get_object_or_404(Articles,slug=slug)
    title_photo = str(article.title_photo).replace('web','')
    profile_photo = str(article.athoder_name.profile_photo).replace('web','')

    # get 4 last article for show in widget popular posts
    All_article = Articles.objects.all()
    count_article = len(All_article)
    article_1 = All_article[int(count_article)-1]
    normalize_upload_path(article_1)

    article_2 = All_article[int(count_article)-2]
    normalize_upload_path(article_2)

    article_3 = All_article[int(count_article)-3]
    normalize_upload_path(article_3)

    article_4 = All_article[int(count_article)-4]
    normalize_upload_path(article_4)

    # get article for Slider
    article_sliders = Articles.objects.filter(category_name=article.category_name)
    normalize_upload_path(article_sliders)

    
    context = {
        'article_sliders':article_sliders,
        'article_1':article_1,
        'article_2':article_2,
        'article_3':article_3,
        'article_4':article_4,
        'profile_photo':profile_photo,
        'title_photo':title_photo,  
        'title_name':'Post',
        'article':article,
    }
    
    return render(request,'single-post.html',context)




def search_result(request):
    All_article = Articles.objects.all()

    count_article = len(All_article)

    article_1 = All_article[int(count_article)-1]
    normalize_upload_path(article_1)

    article_2 = All_article[int(count_article)-2]
    normalize_upload_path(article_2)

    article_3 = All_article[int(count_article)-3]
    normalize_upload_path(article_3)

    article_4 = All_article[int(count_article)-4]
    normalize_upload_path(article_4)
    ##################################

    deta = request.GET

    if not deta:
        return HttpResponse('sorry input is false <br><br> True input : ?word=your word')
    
    word = deta['word']

    if word == '':
        return HttpResponse('sorry input is false <br><br> True input : ?word=your word')

    
    search_article = Articles.objects.filter(title__contains=word)


    if len(search_article) == 0:
        check_article = 'false'
        search_article_big_show = None
        search_article_other = None
    else:
        check_article = 'true'
        try:
            search_article_big_show = list(search_article[:4])
            search_article_other = list(search_article[4:])
        except Exception as ex:
            pass

    context = {
        'word':word,
        'check_article':check_article,
        'search_article':search_article,
        'search_article_big_show':search_article_big_show,
        'search_article_other':search_article_other,
        'title_name':f'search for {word}',
        'article_1':article_1,
        'article_2':article_2,
        'article_3':article_3,
        'article_4':article_4,
    }
    return render(request,'search-results.html',context)



def about(request):
    return render(request, 'about.html',context={})



def contact(request):
    return render(request,'contact.html',context={})


def categories(request):
    return render(request,'categories.html',context={})