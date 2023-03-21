from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    CHOICES = (
    ("ADMIN", "ADMIN"),
    ("USER", "USER")
    )

    user = models.OneToOneField(User, on_delete= models.CASCADE)
    type = models.CharField(max_length=150, choices = CHOICES, default ='USER')

# class Task(models.Model):
#     title = models.CharField(max_length=50)
#     start_date =  models.DateTimeField(auto_now_add=True)
#     end_date =  models.DateTimeField(auto_now=True)
#     deadline = models.DateTimeField(auto_now=True)
#     completionstatus = models.TextField(max_length=255)
#     description = models.TextField(max_length=400)
#     userid = models.IntegerField(max_length=50)

# class Category(models.Model):
#     all =  models.CharField(max_length=400)
#     work =  models.CharField(max_length=400)
#     personal =  models.CharField(max_length=400)
#     whishlist =  models.CharField(max_length=400)
#     birthday =  models.CharField(max_length=400)
#     habits =  models.CharField(max_length=400)
#     learing =  models.CharField(max_length=400)




# from django.db import models
# from django.contrib.auth.models import AbstractUser, BaseUserManager
# from django.db.models.signals import post_save
# from django.dispatch import receiver



# class User(AbstractUser):
#     class Role(models.TextChoices):
#         ADMIN = "ADMIN", 'Admin'
#         STUDENT = "STUDENT", 'Student'
#         TEACHER = "TEACHER", 'Teacher'
#     base_role = Role.ADMIN

#     role = models.CharField(max_length=20,choices=Role.choices)

#     def save(self, *args, **kwargs):
#         if not self.pk:
#             self.role = self.base_role
#             return super().save(args,*kwargs)
        

# class StudentManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(role=User.Role.STUDENT)

        
# class Student(User):

#     base_role = User.Role.STUDENT

#     teacher = StudentManager()


#     class Meta:
#         proxy = True


# @receiver(post_save, sender=Student)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created and instance.role == "STUDENT":
#         StudentProfile.objects.create(user=instance)


# class StudentProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     student_id = models.IntegerField(null=True, blank=True)


# class TeacherManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(role=User.Role.TEACHER)


# class Teacher(User):

#     base_role = User.Role.TEACHER

#     teacher = TeacherManager()

#     class Meta:
#         proxy = True


# class TeacherProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     teacher_id = models.IntegerField(null=True, blank=True)


# @receiver(post_save, sender=Teacher)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created and instance.role == "TEACHER":
#         TeacherProfile.objects.create(user=instance)