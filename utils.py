import json

class Review:
    def __init__(self, id, reviewText, rating, date):
        self.id = id
        self.reviewText = reviewText
        self.rating = rating
        self.date = date

def load_reviews():
    """
    Reads the json file and returns a list of
    Review objects and a raw json data
    """
    parsed = []
    with open('reviews.json', encoding='utf-8-sig') as f:
        json_data = json.load(f)
        for review in json_data:
            parsed.append(Review(review['id'], review['reviewText'], review['rating'], review['reviewCreatedOnTime']))

    return (json_data, parsed)

def sort_reviews(reviews, prioritizeByText, orderByDateNewest, orderByRatingHighest):
    """
    Sorts the reviews starting with the least important criteria first
    to match the required priority order
    """

    # order by date
    reviews.sort(key=lambda x: x.date, reverse=orderByDateNewest)
    
    # order by rating
    reviews.sort(key=lambda x: x.rating, reverse=orderByRatingHighest)
        
    # prioritize those with reviewText after applying the other filters
    if prioritizeByText:
       reviews.sort(key=lambda x: x.reviewText == "")

    return reviews

def filter_reviews(sorted_reviews, minimumRating):
    """
    Returns a list of ids of reviews that have a rating >= minimumRating
    """
    filtered_ids = []
    for review in sorted_reviews:
        if review.rating >= minimumRating:
            filtered_ids.append(review.id)
    return filtered_ids