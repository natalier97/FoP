

class Movie:
    '''movie object w/ info on movie'''
    def __init__(self, title, genre, director, year):
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year
    
    def get_title(self):
        return self._title
    def get_genre(self):
        return self._genre 
    def get_director(self):
        return self._director
    def get_year(self):
        return self._year
    
class StreamingService:
    '''a streaming service catalog- has name of service + movies in catalog'''

    def __init__(self, name):
        self._name = name
        self._catalog = {}

    def get_name(self):
        return self._name
    def get_catalog(self):
        return self._catalog
                
    def add_movie(self, mov_obj):
        self._catalog[mov_obj.get_title()] = mov_obj
    def delete_movie(self, mov_title):
        if mov_title in self._catalog:
            del self._catalog[mov_title]

class StreamingGuide:
    '''a list of streaming services objects/catalogs'''

    def __init__(self):
        self._streamingServices_list = []
    def get_list(self):
        return self._streamingServices_list
    
    def add_streaming_service(self, StreamingService_obj):
        self._streamingServices_list.append(StreamingService_obj)
    def delete_streaming_service(self, StreamingService_name):
        for streaming_service in self._streamingServices_list:
           if streaming_service.get_name()  == StreamingService_name:
                self._streamingServices_list.remove(streaming_service)
    def where_to_watch_movie(self, movie_title):
        for streaming_service in self._streamingServices_list:
            catalog = streaming_service.get_catalog()
            result = []
            if movie_title in catalog:
                if len(result) < 1:
                    result.append(f'{movie_title} ({catalog[movie_title].get_year()})')
                    result.append(streaming_service.get_name())
                else:
                    result.append(streaming_service.get_name())
        return result if result else None
        #      for movie in streaming_service.get_catalog():
        #          if movie.get_title() == movie_title:
        #              watch_here = [f'{movie_title} ({movie.get_year})']
        #              watch_here.append(self.get_name())
        # return watch_here


movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)

stream_serv_1 = StreamingService('Netflick')
stream_serv_1.add_movie(movie_2)

stream_serv_2 = StreamingService('Hula')
stream_serv_2.add_movie(movie_1)
stream_serv_2.add_movie(movie_4)
stream_serv_2.delete_movie('The Seventh Seal')
stream_serv_2.add_movie(movie_2)

stream_serv_3 = StreamingService('Dizzy+')
stream_serv_3.add_movie(movie_4)
stream_serv_3.add_movie(movie_3)
stream_serv_3.add_movie(movie_1)

stream_guide = StreamingGuide()
stream_guide.add_streaming_service(stream_serv_1)
stream_guide.add_streaming_service(stream_serv_2)
stream_guide.add_streaming_service(stream_serv_3)
stream_guide.delete_streaming_service('Hula')
search_results = stream_guide.where_to_watch_movie('Little Women')

print(stream_serv_1.get_catalog())
print(stream_guide.where_to_watch_movie('Little Women'))