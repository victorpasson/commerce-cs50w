from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import User, Action, Bid, Comment, Categorie
from .forms import ActionForm, CommentForm

def index(request):
    return render(request, "auctions/index.html",{
        "auctions": Action.objects.filter(win__isnull = True).order_by('-created'),
        "title": "Active Auction"
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def auction(request, auction_id):
    auction = Action.objects.get(pk=auction_id)
    commentform = CommentForm()

    # Lista de desejo e lance
    if request.user.id:
        watch = User.objects.get(pk=request.user.id).mywatchs.filter(id=auction_id).first()
        if request.method == "POST":
            lance = float(request.POST["lance"])
            max = auction.bids.first()

            if max:
                if (lance > auction.initial_bid) and (lance > max.bid):
                    newbid = Bid(user=request.user, action=auction, bid=lance)
                    newbid.save()
                    return render(request, "auctions/auction.html", {
                        'auction': auction,
                        'commentform': commentform,
                        'watch': watch,
                        'message': "Successfully given bid."
                    })
                else:
                    return render(request, "auctions/auction.html", {
                        'auction': auction,
                        'commentform': commentform,
                        'watch': watch,
                        'message': "Bid needs to be higher than current."
                    })
            else:
                if (lance > auction.initial_bid):
                    newbid = Bid(user=request.user, action=auction, bid=lance)
                    newbid.save()
                    return render(request, "auctions/auction.html", {
                        'auction': auction,
                        'commentform': commentform,
                        'watch': watch,
                        'message': "Successfully given bid."
                    })
                else:
                    return render(request, "auctions/auction.html", {
                        'auction': auction,
                        'commentform': commentform,
                        'watch': watch,
                        'message': "Bid needs to be higher than current."
                    })
        else:
            return render(request, "auctions/auction.html", {
                'auction': auction,
                'commentform': commentform,
                'watch': watch
            })


    return render(request, "auctions/auction.html", {
        'auction': auction,
        'commentform': commentform
    })

def categories(request, cat_id=None, format=None):
    if cat_id is not None:
        auctions = Action.objects.filter(categorie=cat_id).order_by('-created')
        cat = Categorie.objects.get(pk=cat_id)
        return render(request, "auctions/categories.html", {
            'auctions': auctions,
            'title': cat
        })
    else:
        cats = Categorie.objects.order_by('categorie')
        return render(request, "auctions/categories.html", {
            'categories': cats,
            'title': "All Categories"
        })

@login_required(login_url="/login")
def create(request):
    if request.method == 'POST':
        form = ActionForm(request.POST)
        if form.is_valid():
            auction = form.save(commit=False)
            auction.user = request.user
            auction.save()
            return HttpResponseRedirect(reverse("auction", args=(auction.id,)))

    form = ActionForm()
    return render(request, 'auctions/create.html', {
        'form': form
    })

@login_required(login_url="/login")
def watch(request):
    if request.method == "POST":
        auctionid = request.POST["auctionid"]
        auctions = User.objects.get(pk=request.user.id).mywatchs.filter(id=auctionid).first()
        if auctions:
            User.objects.get(pk=request.user.id).mywatchs.remove(Action.objects.get(id=auctionid))
            return HttpResponseRedirect(reverse("auction", args=(auctionid,)))
        else:
            User.objects.get(pk=request.user.id).mywatchs.add(Action.objects.get(id=auctionid))
            return HttpResponseRedirect(reverse("auction", args=(auctionid,)))

    auctions = User.objects.get(pk=request.user.id).mywatchs.all()
    return render(request, "auctions/index.html",{
        "auctions": auctions,
        "title": "My Watch List"
        })

@login_required(login_url="/login")
def comment(request, auction_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.action = Action.objects.get(pk=auction_id)
            comment.save()
        return HttpResponseRedirect(reverse("auction", args=(auction_id,)))
    return HttpResponseRedirect(reverse("auction", args=(auction_id,)))

@login_required(login_url="/login")
def close(request):
    if request.method == "POST":
        auctionid = request.POST["auctionid"]
        auction = Action.objects.get(pk=auctionid)
        auction.finish()
        return HttpResponseRedirect(reverse("auction", args=(auctionid,)))