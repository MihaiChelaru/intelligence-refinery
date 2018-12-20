from django.shortcuts import render, get_object_or_404, redirect
from markdownx.utils import markdownify

from .models import Review, Resource


def review_detail(request, review_id, slug):
    """
    View function for viewing an individual blog post. Redirects to the correct slug if it is improperly entered.
    :param request:
    :param post_id:
    :param slug:
    :return:
    """
    # Checks if the slug in the URL matches the database, and if not redirects to the correct slug URL
    review = get_object_or_404(Review, pk=review_id)
    if review.slug != slug:
        return redirect('reviews:review-detail', post_id=review.pk, slug=review.slug)
    author = review.review_author
    resource_type = review.resource_type
    # markdownify() content and display on page
    review.content = markdownify(review.content)
    return render(request, 'reviews/review_detail.html', {'review': review, 'author': author, 'resource_type': resource_type})


def book_list(request):
    """
    View function for viewing book reviews by category.
    """
    ml_books = Review.objects.filter(resource_type__name__exact="Book", tags="machine-learning")
    return render(request, 'reviews/book_reviews.html', {"ml_books": ml_books})


def course_list(request):
    """
    View function for viewing book reviews by category.
    """
    ml_courses = Review.objects.filter(resource_type__name__contains="Course", tags="machine-learning")
    cs_courses = Review.objects.filter(resource_type__name__contains="Course", tags="programming")
    return render(request, 'reviews/course_reviews.html', {"ml_courses": ml_courses, 'cs_courses': cs_courses})


def software_list(request):
    """
    View function for viewing book reviews by category.
    """
    ides = Review.objects.filter(resource_type__name__exact="Software", tags="ide")
    return render(request, 'reviews/software_reviews.html', {"ides": ides})


def review_list(request, resource_type):
    """
    :param request:
    :param resource_type: The type of resource to generate a review list for.
    :return: Returns a list of reviews of that particular resource_type.
    """
    resources = Review.objects.filter(resource_type__slug__exact=resource_type.lower())
    if resources:
        review_dict = None
        review_type = Resource.objects.get(slug__exact=resource_type.lower())
        if resource_type.lower() == "courses":
            ml_courses = Review.objects.filter(resource_type__name__exact="Online Course", tags="machine-learning")
            cs_courses = Review.objects.filter(resource_type__name__exact="Online Course", tags="programming")
            bd_courses = Review.objects.filter(resource_type__name__exact="Online Course", tags="big-data")
            review_dict = {"Machine Learning": ml_courses, 'Programming': cs_courses, 'Big Data': bd_courses}
        elif resource_type.lower() == "books":
            ml_books = Review.objects.filter(resource_type__name__exact="Book", tags="machine-learning")
            pd_books = Review.objects.filter(resource_type__name__exact="Book", tags="professional-development")
            review_dict = {'Machine Learning': ml_books, 'Professional Development': pd_books}
        elif resource_type.lower() == "software":
            ides = Review.objects.filter(resource_type__name__exact="Software", tags="ide")
            review_dict = {"IDEs": ides}
        return render(request, 'reviews/review_list.html', context={'review_dict': review_dict, 'review_type': review_type})
    else:
        return redirect('reviews:review-home')