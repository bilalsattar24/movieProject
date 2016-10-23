#Author: Bilal Sattar

import media
import freshTomatoes

#inception object
inception = media.Movie("Inception", "A movie about dreams inside of dreams", 
"http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-4.jpg", 
"https://www.youtube.com/watch?v=8hP9D6kZseM")

#jurrasic world object
jurassicWorld = media.Movie(
"Jurassic World", "A monster dinosaur escapes from its pen at a dino park", 
"http://cdn1-www.superherohype.com/assets/uploads/gallery/jurassic-world/"
"10623357_908272402550977_6384474390653526950_o.jpg", 
"https://www.youtube.com/watch?v=RFinNxS5KN4")

#now you see me object 
nowYouSeeMe = media.Movie("Now You See Me", 
"A group of magicians steal money from bad guys", 
"http://www.movietard.com/wp-content/uploads/2015/03/Watch-Now-You-See-Me-2013-online.jpg",
"https://www.youtube.com/watch?v=4OtM9j2lcUA")

#the dark knight object 
darkKnight = media.Movie("The Dark Knight", "A movie about batman and the joker",
"https://encrypted-tbn3.gstatic.com/images?"
"q=tbn:ANd9GcQnCmsSVZeqplkyNPu2CDQ8LR7X9qdoQpJZNDidNm169s6dYBQx",
"https://www.youtube.com/watch?v=EXeTwQWrcwY")

#catch me if you can object 
catchMeIfYouCan = media.Movie("Catch Me If You Can", 
"A con artist that makes fake checks and a detective trying to catch him", 
"http://www.freakingnews.com/pictures/86500/"
"Catch-Me-if-you-Can-Movie-Poster-Pictogram-86587.jpg",
"https://www.youtube.com/watch?v=71rDQ7z4eFg")

#the revenant object
revenant = media.Movie("The Revenant", 
"A man is left behind when attacked by a bear and he comes back for revenge",
"http://beacon.nwciowa.edu/wp-content/uploads/"
"2016/01/The-Revenant-2015-poster.jpg",
"https://www.youtube.com/watch?v=LoebZZ8K5N0")

#create list of movie objects
movies=[inception, jurassicWorld, nowYouSeeMe, 
        darkKnight, catchMeIfYouCan, revenant]

#call open_movies_page from freshTomatoes.py
freshTomatoes.open_movies_page(movies)
