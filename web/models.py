from django.db import models

# Create your models here.


class Repaly_comments(models.Model):
    '''
    repplay for comments
    '''
    text = models.TextField(max_length=1000)
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now=True, auto_now_add=False)
    repaly = models.ForeignKey("Comments", null=True ,on_delete=models.SET_NULL)
    replay_email = models.EmailField(max_length=254)
    class Meta:
        verbose_name = 'Repaly_comment'

    def __str__(self):
        return f'{self.name} : {self.repaly.name} : {self.repaly.article_commetns}'

class Comments(models.Model):
    '''
    commetns for articles 
    '''
    text = models.TextField(max_length=1000)
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now=True, auto_now_add=False)
    article_commetns = models.ForeignKey("Articles", null=True ,on_delete=models.SET_NULL)
    comment_email = models.EmailField(max_length=254)

    class Meta:
        verbose_name = 'comment'


    def __str__(self):
        return f'{self.article_commetns} : {self.name}'

class Tags(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'tag'
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Articles(models.Model):
    title = models.CharField(max_length=160)
    slug = models.SlugField()
    title_photo = models.ImageField(upload_to = './web/static/uploads/articles_photo')
    text = models.TextField()
    athoder_name = models.ForeignKey("Athoder", verbose_name=("Athoder name"), null=True, on_delete=models.SET_NULL)
    category_name = models.ForeignKey("Category", null=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now=True,)
    Tags = models.ManyToManyField("Tags", verbose_name="tag", help_text='اگر تگی وجود نداشت میتونید اضافه کنید<br>')

    class Meta:
        verbose_name = 'article'

    def __str__(self):
        return self.title


class Athoder(models.Model):
    profile_photo = models.ImageField(upload_to = './web/static/uploads/articles_photo', height_field=None, width_field=None, max_length=None)
    name = models.CharField(max_length=80)
    info = models.TextField(max_length=300)

    def __str__(self):
        return self.name

class My_selected(models.Model):
    articles_selected = models.ManyToManyField("Articles")