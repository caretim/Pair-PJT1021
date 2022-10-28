from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Review, Comment
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model
from django.db.models import Q

# Create your views here.
headers = [
    (1, "모집합니다"),
    (2, "참여합니다"),
]

games = [
    "덕몽어스",
    "리그 오브 레전드",
    "오버워치2",
    "어몽어스",
    "폴가이즈",
]

@login_required
def create(request):
    if request.method == "POST":
        forms = PostForm(request.POST)
        if forms.is_valid():
            review = forms.save(commit=False)
            review.user = request.user
            review.save()
            if review.header_tag == 1:
                review.join_member.add(request.user)
                return redirect("reviews:index")
            else:
                return redirect("reviews:index")
    else:
        forms = PostForm()
    context = {
        "forms": forms,
    }
    return render(request, "reviews/create.html", context)


def index(request):
    all_data = Review.objects.order_by("-pk")
    all_user = get_user_model().objects.order_by("-pk")
    all_comment = Comment.objects.order_by("-pk")
    
    context = {
        "all_data": all_data,
        "all_user": all_user,
        "all_comment": all_comment,
    }
    return render(request, "reviews/index.html", context)



def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    header = headers[review.header_tag-1][1]
    members = review.join_member.all()
    comment_form = CommentForm()
    game = games[review.game_name-1]
    context = {
        "review": review,
        "comment_form": comment_form,
        "members": members,
        "header" : header,
        "game": game,
    }
    return render(request, "reviews/detail.html", context)


def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == "POST":
        forms = PostForm(request.POST, instance=review)
        if forms.is_valid():
            forms.save()
            return redirect("reviews:detail", review_pk)

    else:
        forms = PostForm(instance=review)
    context = {
        "forms": forms,
    }
    return render(request, "reviews/update.html", context)


def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if review.user == request.user:
        review.delete()
        return redirect("reviews:index")

    else:
        return HttpResponseForbidden()


def comments(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.review = review
            comment.save()
            return redirect("reviews:detail", review_pk)


def comments_delete(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if comment.user == request.user:
        comment.delete()
        return redirect("reviews:detail", review_pk)
    else:
        return HttpResponseForbidden()


@login_required
def join_member(request, review_pk):
    # if request.method == "POST":
        review = get_object_or_404(Review, pk=review_pk)
        # review = Review.objects.get(pk=review_pk)
        if len(review.join_member.all()) < review.member:
            if review.join_member.filter(pk=request.user.pk).exists():
                review.join_member.remove(request.user)
            else:
                review.join_member.add(request.user)
            return redirect("reviews:detail", review_pk)
        # return HttpResponseForbidden()
        
        else:
            # 모집인원이 꽉 찼는데 이미 참여하고 있는 상태라면,
            if review.join_member.filter(pk=request.user.pk).exists():
                review.join_member.remove(request.user)
            # 메시지 처리(나중에)
            return redirect("reviews:detail", review_pk)
                
            


def pick_game(request, game_pk):
    pick_game = Review.objects.filter(game_name=game_pk)
    context = {
        "all_data": pick_game,
    }
    return render(request, "reviews/index.html", context)


def search(request):
    all_data = Review.objects.all()
    search_data = request.GET.get("search", "")

    if search_data:
        return_data = all_data.filter(
            Q(title__icontains=search_data) | Q(content__icontains=search_data)
        )
    if len(search_data) == 0:
        none_info = "공백을 입력하셨습니다."
        context = {
            "none_info": none_info,
        }

    elif len(return_data) == 0:
        none_info = "검색 결과가 없습니다."
        context = {
            "none_info": none_info,
        }
        return render(request, "reviews/index.html", context)


# def update_comment(request,comment_pk,article_pk):
#     comment = Comment.objects.get(pk = comment_pk)
#     if comment.user == request.user:
#         if request.method == "POST":
#             forms = CommentForm(request.POST, instance=comment)
#             if forms.is_valid():
#                 forms.save()
#                 return redirect ("reviews:detial",article_pk)


#     return redirect("reviews:detail" ,article_pk)
