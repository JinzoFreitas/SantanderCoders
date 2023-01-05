import csv
from collections import defaultdict

class locadora:
    def __init__(self, table = 'collection.csv') -> None:

        def __read_csv(table : csv) -> dict:

            '''
            Opens movie collection .csv file
            '''

            with open(table) as csv_file:
                reader = csv.reader(csv_file)

                #sorts in an alphabetical fashion
                reader = sorted(reader, key=lambda row: row[0], reverse=False)

                #.csv to dict
                dicio = dict(reader)
            return dicio

        self.table = table
        self.collection = __read_csv(table)

    def __write_csv(self) -> None:

        '''
        Writes the collection to .csv file
        '''

        with open(self.table, 'w') as csvfile:
            writer = csv.writer(csvfile)

            #gets key and value from the collection and writes .csv row by row
            for key, value in self.collection.items():
                    writer.writerow([key, value])

    def show_collection(self) -> None:

        '''
        Shows all the movies in the collection
        '''

        #checks if collection exists (converts to boolean)
        if bool(self.collection):
            aesthetic_collection = str(self.collection).replace(', ', ',\n').replace("'", "")\
                # .replace('{', '').replace('}','').replace(': ', ':\t')
            print(f'Current collection:\n{aesthetic_collection}', end='\n')
        else:
            print('No movies registered...', end='\n')

    def reset_collection(self) -> None:

        '''
        Resets the collection to 0 movies registered
        '''

        #reassures the user's desire
        answer = input('Are you sure you want to clear the collection?')
        if (answer == 'y' or answer == 'yes'):
            
            #creates a empty dict from scratch
             self.collection = defaultdict()
             self.__write_csv()
             print(f'Your collection was reseted.', end='\n')
        else:
            print(f'Your collection was not reseted.\
                \n{self.show_collection()}', end='\n')

    def register(self, movies : list) -> None:

        '''
        Register n* movies in the collection
        '''

        for movie in movies:

            #adds a movie always as 'Available'
            self.collection[movie] = 'Available'
            self.__write_csv()

    def remove(self, movies : list) -> None:

        '''
        Removes n* movies from the collection
        '''

        for movie in movies:
            if self.search:

                # uses search function and deletes the movie key, if found
                del self.collection[movie]
                self.__write_csv()
            else:
                print('Not found for removal', end='\n')

    def update(self, movie : str, new_name: str) -> None:

        '''
        Updates n* movies titles in the collection
        '''

        #creates a new movie key with the status of the movie to be updated
        self.collection[new_name] = self.collection.pop(movie)
        self.__write_csv()

    def set_status(self, movie : str, status : str) -> None:

        '''
        Sets the status of n* movies in the collection
        (allocated, unavailable, available etc.)
        '''

        #gets the status to be updated to show the user
        old_status = str(self.collection.get(movie)).lower()

        #if the movie is not available, it cannot be allocated
        if old_status != 'available' and status.lower() == 'allocated':
            print(f'Impossible to allocate:\
                \nThe {movie} disc in {old_status}', end='\n')
        else:
            self.collection[movie] = status.capitalize()
            self.__write_csv()

    def search(self, query : str) -> bool:

        '''
        Searches for movies in the collection containing the query
        '''

        movies = []

        #creates a list of all the movies that contains the query
        for movie in self.collection.keys():
            if query.lower() in movie.lower():
                movies += [movie]
        if len(movies) != 0:
            for movie in movies:

                #prints the movies found with their status
                print({movie: self.collection.get(movie)})
            return True
        else:
            print(f'No movie containing "{query}" listed', end='\n')
            return False