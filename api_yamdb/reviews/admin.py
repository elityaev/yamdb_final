from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title


class TitleAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'category', 'show_genres']

    def show_genres(self, obj):
        return ", \n".join([a.name for a in obj.genre.all()])


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'show_titles']

    def show_titles(self, obj):
        return "\n".join([a.name for a in obj.titles.all()])


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title_id', 'text', 'author', 'score', 'pub_date')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('review_id', 'text', 'author', 'pub_date')


admin.site.register(Title, TitleAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Genre, GenreAdmin)

admin.site.register(Review, ReviewAdmin)

admin.site.register(Comment, CommentAdmin)
