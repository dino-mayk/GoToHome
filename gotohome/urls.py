from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(
        '',
        include(
            'homepage.urls',
        ),
        name='homepage',
    ),
    path(
        'auth/',
        include(
            'users.urls',
        ),
        name='users',
    ),
    path(
        'posts/',
        include(
            'posts.urls',
        ),
        name='posts',
    ),
    path(
        'chat/',
        include(
            'chat.urls',
        ),
        name='chat',
    ),
    path(
        'admin/',
        admin.site.urls,
        name='admin',
    ),
    path(
        'grappelli/',
        include(
            'grappelli.urls',
        ),
        name='grappelli',
    ),
    path(
        'tinymce/',
        include(
            'tinymce.urls',
        ),
    ),
    path(
        'ckeditor/',
        include(
            'ckeditor_uploader.urls',
        ),
    ),
    path(
        'djeym/',
        include(
            'djeym.urls',
            namespace='djeym',
        ),
    ),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path(
            '__debug__/',
            include(
                debug_toolbar.urls,
            ),
        ),
    ]
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
