from django.urls import path
from myapp import views


urlpatterns = [
    path('',views.indexHandler, name = "index"),
    #path('all_blogs',views.showAllBlogs ,name= 'all_blogs' ),
    #path('delete', views.delete, name = 'delete'),
    #path('add_blog', views.addBlog, name='add_blog'),
    path('form_add_blog', views.formAddBlog, name= "form-add-blog"),
    path("form_save", views.formSave, name = "form-save"),
    path("all_blogs", views.viewOnlyBlogs, name= "all_blogs"),
    path('a-delete/<id>', views.aDelete, name = 'a-delete'),
    path('update-form/<id>', views.updateForm, name = 'update-form'),
    path('update_data', views.updateData, name='updatedata'),
    path('view_blog/<id>', views.viewBlog, name = 'view_blog'),
    path('add_comment/', views.addComment, name= "addComment")
]

