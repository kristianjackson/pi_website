from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, FriendRequest
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from feed.models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.conf import settings
from django.http import HttpResponseRedirect
import random

# Create your views here.

User = get_user_model()

@login_required
def user_list(request):
    users = Profile.objects.exclude(user=request.user)