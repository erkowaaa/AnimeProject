from django.db import models


class UserProfile(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.PositiveIntegerField(default=0)
    date_registered = models.DateField(auto_now=True)
    email = models.EmailField()
    phone_number = models.IntegerField()

    def __str__(self):
        return self.first_name


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name


class Genre(models.Model):
    genre_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.genre_name


class Type(models.Model):
    type_name = models.CharField(max_length=16)

    def __str__(self):
        return self.type_name


class Ozvuchka(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    director_name = models.CharField(max_length=32, unique=True)
    age = models.PositiveIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='director_img/')

    def __str__(self):
        return self.director_name


class Anime(models.Model):
    anime_name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    ozvuchka = models.ManyToManyField(Ozvuchka)
    director = models.ManyToManyField(Director)
    description = models.TextField()
    published_date = models.DateField()
    image = models.ImageField(upload_to='anime_img/')
    popular = models.BooleanField(default=True)
    STATUS_CHOICES = (
        ('ongoing', 'Ongoing'),
        ('announcement', 'Аnnouncement'),
        ('came out', 'Сame out'),
    )

    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='came out')
    duration = models.PositiveSmallIntegerField(default=0)
    studio = models.CharField(max_length=32)

    def __str__(self):
        return self.anime_name


class Review(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)], help_text="Rate the item with 0 to 6 stars.", verbose_name="Rating")

    def __str__(self):
        return f"{self.anime} - {self.user} - {self.stars} stars"


class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    anime_name = models.ForeignKey(Anime, related_name='reviews', on_delete=models.CASCADE, null=True, blank=True)
    parent_review = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
