from django.db import migrations, models


# class VideoCardManager(models.Manager):
#     def create_videocard(self, vctitle, vcurl):
#         card = self.create(title=vctitle, url=vcurl)
#         # do something
#         return card
#
#
# class SearchModelManager(models.Manager):
#     def create_searchmodel(self, smtitle, smchatid):
#         search = self.create(title=smtitle, chatid=smchatid)
#         # do something
#         return search


class VideoCard(models.Model):
    """
    From django db.models.base
    """
    title = models.CharField(max_length=20)
    url = models.TextField(max_length=20)

    def __str__(self):
        return self.title


class SearchModel(models.Model):
    title = models.CharField(max_length=20)
    chatid = models.CharField(max_length=20)

    def __str__(self):
        return self.title


# init_db():
