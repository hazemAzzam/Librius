from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    date_of_birth = models.DateField(null=True)
    country = models.CharField(max_length=255, null=True)
    books = models.ManyToManyField("Book")
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.country})"
    
class Publisher(models.Model):
    name = models.CharField(max_length=255, null=False)
    country = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.name} - {self.country}"
    
class Member(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    phone_number = models.CharField(max_length=11, null=False)
    address = models.CharField(max_length=255, null=True)

    membership_start_date = models.DateField(null=False)
    membership_end_date = models.DateField(null=True)
    membership_status = models.BooleanField(null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.membership_status})"

class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name='Book Title', null=False)
    isbn = models.CharField(max_length=13, null=False, unique=True)
    publication_date = models.DateField(null=False)
    authors = models.ManyToManyField(Author)
    def __str__(self):
        return f"{self.title}"
    
class BorrowedBook(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrow_date = models.DateField(null=False)
    return_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.book_id} - {self.member_id} ({self.return_date})"
