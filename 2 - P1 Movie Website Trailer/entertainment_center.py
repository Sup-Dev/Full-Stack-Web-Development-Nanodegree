import fresh_tomatoes
import media

wall_e = media.Movie("Wall-E", 
					"In the distant future, a small waste collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.",
					98,
					"27 June 2008",
					"Andrew Stanton",
					"G",
					"https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
					"https://www.youtube.com/watch?v=ZisWjdjs-gM")

#print(toy_story.storyline)						

avatar = media.Movie("Avatar",
					"A marine on an alien planet",
					162,
					"18 December 2009",
					"James Cameron",
					"PG-13",
					"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					"https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)					
#avatar.show_trailer()

fight_club = media.Movie("Fight Club",
						"An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more",
						139,
						"15 October 1999",
						"David Fincher",
						"R",
						"https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
						"https://www.youtube.com/watch?v=BdJKm16Co6M")

ratatouille = media.Movie("Ratatouille",
						"A rat is a chef in Paris",
						111,
						"29 June 2007",
						"Brad Bird, Jan Pinkava",
						"G",
						"https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
						"https://www.youtube.com/watch?v=c3sBBRxDAqk")			

george_of_the_jungle = media.Movie("George of the Jungle",
								"George grows up in the jungle raised by apes. Based on the Cartoon series.",
								92,
								"16 July 1997",
								"Sam Weisman",
								"PG",
								"https://upload.wikimedia.org/wikipedia/en/f/f8/George_Of_The_Jungle.jpg",
								"https://www.youtube.com/watch?v=opqC7DhdaTM")

the_dark_knight = media.Movie("The Dark Knight", 
							"When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.",
							152,
							"18 July 2008",
							"Christopher Nolan",
							"PG-13",
							"https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
							"https://www.youtube.com/watch?v=EXeTwQWrcwY")

movies = [wall_e, avatar, fight_club, ratatouille, george_of_the_jungle, the_dark_knight]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)