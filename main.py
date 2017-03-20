import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        movielist = ["Touch of Evil", "Rashomon", "The Night of the Hunter", "The Manchurian Candidate", "The Battle of Algiers"]

        selectedmovie = movielist[random.randrange(len(movielist))]

        return selectedmovie

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"
        nextmovie = self.getRandomMovie()
        content +="<h1>Tomorrow's Movie</h1>"
        content +="<p>" + nextmovie + "</p>"

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
