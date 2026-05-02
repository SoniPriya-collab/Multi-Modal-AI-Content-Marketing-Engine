from workers.celery_worker import celery
from services.text_generator import generate_blog
from services.image_generator import generate_image

@celery.task
def generate_campaign(topic):

    blog = generate_blog(topic)

    tweets = [
        f"{topic} is amazing!",
        f"Learn more about {topic}",
        f"AI generated content for {topic}"
    ]

    image = generate_image(topic)

    return {
        "blog": blog,
        "tweets": tweets,
        "image": image
    }