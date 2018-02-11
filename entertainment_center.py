import media
import fresh_tomatoes

toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

harry_potter = media.Movie(
    "Harry Potter and the Deathly Hallows",
    ("2010 fantasy film directed by David Yates "
     "and distributed by Warner Bros."),
    ("https://upload.wikimedia.org/wikipedia/en/2/2d/"
     "Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_1.jpg"),
    "https://www.youtube.com/watch?v=9hXH0Ackz6w")

fresh_tomatoes.open_movies_page([toy_story, harry_potter])
