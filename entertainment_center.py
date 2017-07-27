import fresh_tomatoes
import media


a_league_of_their_own = media.Movie("A League of Their Own",
                        "fictionalized account of the real-life All-American Girls Professional Baseball League (AAGPBL)",
                        "https://upload.wikimedia.org/wikipedia/en/5/5f/League_of_their_own_ver2.jpg",
                        "https://www.youtube.com/watch?v=tkZTcofj3wU")
#print (a_league_of_their_own.storyline)

the_blues_brothers = media.Movie("The Blues Brothers",
                      "A tale of redemption for paroled convict Jake and his brother Elwood, who set out on a mission from God",
                      "https://upload.wikimedia.org/wikipedia/en/a/ae/Bluesbrothersmovieposter.jpg",
                      "https://www.youtube.com/watch?v=ma-rkV6wVJM")
#print (the_blues_brothers.storyline)
#the_blues_brothers.show_trailer()

moana = media.Movie("Moana",
                      "An adventurous teenager sails out on a daring mission to save her people. ",
                      "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg",
                      "https://www.youtube.com/watch?v=LKFuXETZUsI")
#print (moana.storyline)
#moana.show_trailer()

casino = media.Movie("Casino",
                      "Ace Rothstein, a Jewish American top gambling handicapper who is called by the...",
                      "https://upload.wikimedia.org/wikipedia/en/d/d8/Casino_poster.jpg",
                      "https://www.youtube.com/watch?v=qEhuDMU868Q")
#print (casino.storyline)
#casino.show_trailer()

trolls = media.Movie("Trolls",
                      "Two trolls on a quest to save their village from destruction by the Bergens, creatures who eat trolls.",
                      "https://upload.wikimedia.org/wikipedia/en/a/ad/Trolls_%28film%29_logo.png",
                      "https://www.youtube.com/watch?v=oWgTqLCLE8k")
#print (trolls.storyline)
#trolls.show_trailer()

divergent = media.Movie("Divergent",
                      "in a dystopian and post-apocalyptic Chicago[7] where people are divided into distinct factions based on human virtues.",
                      "https://upload.wikimedia.org/wikipedia/en/d/d4/Divergent.jpg",
                      "https://www.youtube.com/watch?v=Om-jAJG-dAQ")
#print (divergent.storyline)
#divergent.show_trailer()

movies = [a_league_of_their_own, the_blues_brothers, moana, casino, trolls, divergent]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
