from django.db import models
from parler.models import TranslatableModel, TranslatedFields

class Post(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=100),
        content=models.TextField(),
        # Add more translated fields as needed
    )

    # Other non-translated fields specific to the Post model

    def __str__(self):
        return self.title
