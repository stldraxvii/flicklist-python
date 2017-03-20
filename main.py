import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        movielist = ["Touch of Evil", "Rashomon", "The Night of the Hunter", "The Manchurian Candidate", "The Battle of Algiers",
        "Psycho", "2001: A Space Odyssey", "Solaris", "El Topo", "F for Fake", "Do the Right Thing", "Raging Bull", "La Haine",
        "Boogie Nights", "Mangolia", "Hard-Boiled", "Heat", "Lost in Translation", "28 Days Later...", "Pan's Labyrinth",]

        selectedmovie = movielist[random.randrange(len(movielist))]

        return selectedmovie

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        #Tomorrow's movie
        nextmovie = ""
        equality = True
        while equality is True:
            nextmovie = self.getRandomMovie()
            if nextmovie != movie:
                equality = False

        content +="<h1>Tomorrow's Movie</h1>"
        content +="<p>" + nextmovie + "</p>"


        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
