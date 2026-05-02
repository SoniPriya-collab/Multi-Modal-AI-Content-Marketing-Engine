def detect_category(topic):

    topic = topic.lower()

    if any(word in topic for word in [
        "ai",
        "machine learning",
        "deep learning",
        "data science",
        "python",
        "technology",
        "robot"
    ]):

        return "technology"

    elif any(word in topic for word in [
        "fitness",
        "health",
        "gym",
        "yoga",
        "nutrition"
    ]):

        return "health"

    elif any(word in topic for word in [
        "travel",
        "tourism",
        "vacation",
        "trip"
    ]):

        return "travel"

    elif any(word in topic for word in [
        "food",
        "cooking",
        "restaurant",
        "pizza",
        "burger"
    ]):

        return "food"

    elif any(word in topic for word in [
        "business",
        "marketing",
        "startup",
        "finance"
    ]):

        return "business"

    return "general"


def generate_blog(topic):

    category = detect_category(topic)

    if category == "technology":

        return f"""
        {topic} is revolutionizing the technology industry by introducing
        smarter automation, intelligent systems, and modern digital solutions.

        Companies are using {topic} to improve productivity,
        reduce manual work, and build innovative applications.

        Students and developers are actively learning {topic}
        because it offers strong career opportunities and future growth.
        """

    elif category == "health":

        return f"""
        {topic} plays an important role in maintaining
        a healthy and balanced lifestyle.

        Experts recommend learning about {topic}
        to improve physical fitness, mental wellness,
        and overall quality of life.

        Many people today are adopting {topic}
        as part of their daily routines.
        """

    elif category == "travel":

        return f"""
        {topic} helps people explore beautiful destinations,
        experience new cultures, and create unforgettable memories.

        Travel enthusiasts enjoy {topic}
        because it provides relaxation, adventure,
        and exciting experiences around the world.

        Tourism industries are rapidly growing
        because of increasing interest in {topic}.
        """

    elif category == "food":

        return f"""
        {topic} is loved by food enthusiasts around the world
        because of its delicious taste and unique flavors.

        Restaurants and food businesses continue
        to innovate using {topic} to attract more customers.

        Food lovers enjoy exploring different varieties
        and creative recipes related to {topic}.
        """

    elif category == "business":

        return f"""
        {topic} is helping businesses improve growth,
        marketing strategies, and customer engagement.

        Modern companies are investing heavily in {topic}
        to increase profits and build stronger brands.

        Entrepreneurs believe {topic}
        plays a major role in future business success.
        """

    else:

        return f"""
        {topic} is becoming increasingly popular
        because of its importance in modern society.

        People are actively learning and exploring {topic}
        to improve knowledge, skills, and innovation.

        Experts believe {topic}
        will continue to grow rapidly in the future.
        """


def generate_tweets(topic):

    category = detect_category(topic)

    if category == "technology":

        return [

            f"🚀 {topic} is shaping the future of technology!",

            f"💻 Learn {topic} to build innovative projects.",

            f"🔥 {topic} skills are highly demanded today."

        ]

    elif category == "health":

        return [

            f"💪 {topic} helps maintain a healthy lifestyle.",

            f"🥗 Start your wellness journey with {topic}.",

            f"🏋 {topic} improves both physical and mental health."

        ]

    elif category == "travel":

        return [

            f"✈ Explore the world with {topic} adventures!",

            f"🌍 {topic} creates unforgettable memories.",

            f"🏖 Travel lovers enjoy amazing {topic} experiences."

        ]

    elif category == "food":

        return [

            f"🍕 {topic} is loved by foodies everywhere!",

            f"😋 Delicious flavors make {topic} special.",

            f"🍔 Try exciting recipes related to {topic}."

        ]

    elif category == "business":

        return [

            f"📈 {topic} helps businesses grow faster.",

            f"💼 Smart companies invest in {topic}.",

            f"🚀 {topic} is transforming modern business."

        ]

    return [

        f"🔥 {topic} is trending worldwide.",

        f"🚀 Learn more about {topic} today.",

        f"💡 {topic} is creating exciting opportunities."

    ]


def generate_image(topic):

    topic = topic.replace(" ","+")

    return f"https://loremflickr.com/600/400/{topic}"