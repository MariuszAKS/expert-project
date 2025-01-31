from experta import Fact, KnowledgeEngine, DefFacts, Rule, NOT, W, MATCH
from numpy import arange
from pandas import read_csv
from skfuzzy.control import Antecedent
from skfuzzy import trimf, interp_membership


class Movie(Fact):
    title = str
    genre = list
    imdb_rating = float
    release_year = int
    runtime = int


class GoodGenre(Fact):
    pass


class MovieRecommender(KnowledgeEngine):
    best_movie_index = [-1, -1, -1]
    best_movie_score = [0, 0, 0]

    @DefFacts()
    def initial_facts(self):
        yield Fact(action="recommend_movie")

    # @Rule(Fact(action='recommend_movie'), NOT(Fact(imdb_rating=W())), NOT(Fact(release_year=W())), NOT(Fact(genre=W())))
    # def ask_for_preferences(self):
    #     self.declare(Fact(imdb_rating=input("Enter desired IMDb rating (poor, average, good): ")))
    #     self.declare(Fact(release_year=input("Enter desired release year (very_old, old, new): ")))
    #     self.declare(Fact(runtime=input("Enter desired runtime (short, average, long): ")))
    #     self.declare(Fact(genre=input("Enter desired genre: ")))

    @Rule(Movie(title=MATCH.title, genre=MATCH.genre), Fact(genre=MATCH.genre))
    def PasujacyGatunek(self, title, genre):
        # print(title, genre, "]]]")
        self.declare(GoodGenre(title=title))

    @Rule(Fact(imdb_rating='good'), Fact(release_year='new'), Fact(runtime='long'), GoodGenre(title=MATCH.title))
    def recommend_GNL(self, title):
        movie_score, index = self.calculate_movie_score(title, 'good', 'new', 'long')
        self.update_best_movies(movie_score, index)

    @Rule(Fact(imdb_rating='average'), Fact(release_year='new'), Fact(runtime='long'), GoodGenre(title=MATCH.title))
    def recommend_ANL(self, title):
        movie_score, index = self.calculate_movie_score(title, 'average', 'new', 'long')
        self.update_best_movies(movie_score, index)

    @Rule(Fact(imdb_rating='good'), Fact(release_year='old'), Fact(runtime='long'), GoodGenre(title=MATCH.title))
    def recommend_GOL(self, title):
        movie_score, index = self.calculate_movie_score(title, 'good', 'old', 'long')
        self.update_best_movies(movie_score, index)

    @Rule(Fact(imdb_rating='average'), Fact(release_year='old'), Fact(runtime='long'), GoodGenre(title=MATCH.title))
    def recommend_AOL(self, title):
        movie_score, index = self.calculate_movie_score(title, 'average', 'old', 'long')
        self.update_best_movies(movie_score, index)

    @Rule(Fact(imdb_rating='good'), Fact(release_year='new'), Fact(runtime='average'), GoodGenre(title=MATCH.title))
    def recommend_GNA(self, title):
        movie_score, index = self.calculate_movie_score(title, 'good', 'new', 'average')
        self.update_best_movies(movie_score, index)

    @Rule(Fact(imdb_rating='average'), Fact(release_year='new'), Fact(runtime='average'), GoodGenre(title=MATCH.title))
    def recommend_ANA(self, title):
        movie_score, index = self.calculate_movie_score(title, 'average', 'new', 'average')
        self.update_best_movies(movie_score, index)

    @Rule(Fact(imdb_rating='good'), Fact(release_year='old'), Fact(runtime='average'), GoodGenre(title=MATCH.title))
    def recommend_GOA(self, title):
        movie_score, index = self.calculate_movie_score(title, 'good', 'old', 'average')
        self.update_best_movies(movie_score, index)

    @Rule(Fact(imdb_rating='average'), Fact(release_year='old'), Fact(runtime='average'), GoodGenre(title=MATCH.title))
    def recommend_AOA(self, title):
        movie_score, index = self.calculate_movie_score(title, 'average', 'old', 'average')
        self.update_best_movies(movie_score, index)

    @Rule(Fact(imdb_rating='good'), Fact(release_year='new'), Fact(runtime='short'), GoodGenre(title=MATCH.title))
    def recommend_GNS(self, title):
        movie_score, index = self.calculate_movie_score(title, 'good', 'new', 'short')
        self.update_best_movies(movie_score, index)

    @Rule(Fact(imdb_rating='average'), Fact(release_year='new'), Fact(runtime='short'), GoodGenre(title=MATCH.title))
    def recommend_ANS(self, title):
        movie_score, index = self.calculate_movie_score(title, 'average', 'new', 'short')
        self.update_best_movies(movie_score, index)

    @Rule(Fact(imdb_rating='good'), Fact(release_year='old'), Fact(runtime='short'), GoodGenre(title=MATCH.title))
    def recommend_GOS(self, title):
        movie_score, index = self.calculate_movie_score(title, 'good', 'old', 'short')
        self.update_best_movies(movie_score, index)

    @Rule(Fact(imdb_rating='average'), Fact(release_year='old'), Fact(runtime='short'), GoodGenre(title=MATCH.title))
    def recommend_AOS(self, title):
        movie_score, index = self.calculate_movie_score(title, 'average', 'old', 'short')
        self.update_best_movies(movie_score, index)

    def reset_best_movies(self):
        self.best_movie_index = [-1, -1, -1]
        self.best_movie_score = [0, 0, 0]

    def declare_preferences(self, movie_year, movie_runtime, movie_imdb, movie_genre):
        self.declare(Fact(imdb_rating=movie_imdb))
        self.declare(Fact(release_year=movie_year))
        self.declare(Fact(runtime=movie_runtime))
        self.declare(Fact(genre=movie_genre))

    def return_best_movies_index_list(self):
        return self.best_movie_index

    def calculate_movie_score(self, title_, imdb_rating_, release_year_, runtime_):
        movie = data.loc[data['Series_Title'] == title_]
        p_release = calculate_membership_release_year(release_year_, movie['Released_Year'].iloc[0])
        p_imdb = calculate_membership_imdb_rating(imdb_rating_, movie['IMDB_Rating'].iloc[0])
        p_time = calculate_membership_runtime(runtime_, movie['Runtime'].iloc[0])

        movie_score = p_release + p_imdb + p_time

        return movie_score, movie.index[0]

    def update_best_movies(self, movie_score, index):
        if movie_score > self.best_movie_score[0]:
            self.best_movie_score[2] = self.best_movie_score[1]
            self.best_movie_index[2] = self.best_movie_index[1]
            self.best_movie_score[1] = self.best_movie_score[0]
            self.best_movie_index[1] = self.best_movie_index[0]
            self.best_movie_score[0] = movie_score
            self.best_movie_index[0] = index
        elif movie_score > self.best_movie_score[1]:
            self.best_movie_score[2] = self.best_movie_score[1]
            self.best_movie_index[2] = self.best_movie_index[1]
            self.best_movie_score[1] = movie_score
            self.best_movie_index[1] = index
        elif movie_score > self.best_movie_score[2]:
            self.best_movie_score[2] = movie_score
            self.best_movie_index[2] = index

    # znajdz wszystkie filmy typu "drama" i info o nich
    @Rule(Movie(genre='Drama', title=MATCH.title, release_year=MATCH.release_year, imdb_rating=MATCH.imdb_rating))
    def testowy_drama(self, title, release_year, imdb_rating):
        # print("Test", title, release_year, imdb_rating)
        pass


def calculate_membership_release_year(selected_release_year, movie_release_year):
    return interp_membership(release_year.universe, release_year[selected_release_year].mf, movie_release_year)


def calculate_membership_imdb_rating(selected_imdb_rating, movie_imdb_rating):
    return interp_membership(imdb_rating.universe, imdb_rating[selected_imdb_rating].mf, movie_imdb_rating)


def calculate_membership_runtime(selected_runtime, movie_runtime):
    return interp_membership(runtime.universe, runtime[selected_runtime].mf, movie_runtime)


def declare_movies_from_data():
    # for _, row in first_100_rows_testing.iterrows():
    for _, row in data.iterrows():
        genres = row['Genre'].split(", ")
        for g in genres:
            engine.declare(Movie(imdb_rating=row['IMDB_Rating'],
                                 release_year=row['Released_Year'],
                                 genre=g,
                                 title=row['Series_Title'],
                                 runtime=row['Runtime']))


def run_engine(movie_year, movie_runtime, movie_imdb, movie_genre):
    engine.reset()
    engine.reset_best_movies()

    declare_movies_from_data()
    engine.declare_preferences(movie_year, movie_runtime, movie_imdb, movie_genre)

    engine.run()

    movie_runtimes = []
    movie_titles = []
    movie_years = []

    for i in range(3):
        if engine.best_movie_index[i] > -1:
            movie_runtimes.append(data.loc[engine.best_movie_index[i], 'Runtime'])
            movie_titles.append(data.loc[engine.best_movie_index[i], 'Series_Title'])
            movie_years.append(data.loc[engine.best_movie_index[i], 'Released_Year'])

    return movie_runtimes, movie_titles, movie_years


# Read data from file
data = read_csv('imdb_top_1000.csv', sep=',')


# Define the range for release years (e.g., from 1900 to 2025)
release_year = Antecedent(arange(1920, 2020, 1), 'release_year')
imdb_rating = Antecedent(arange(0, 10.1, 0.1), 'imdb_rating')
runtime = Antecedent(arange(0, 200, 1), 'runtime')

# Define fuzzy sets
release_year['old'] = trimf(release_year.universe, [1920, 1920, 2000])
release_year['new'] = trimf(release_year.universe, [1990, 2020, 2020])

# Define fuzzy sets
imdb_rating['poor'] = trimf(imdb_rating.universe, [0, 0, 5])
imdb_rating['average'] = trimf(imdb_rating.universe, [4, 6, 8])
imdb_rating['good'] = trimf(imdb_rating.universe, [5, 10, 10])

# Define fuzzy sets
runtime['short'] = trimf(runtime.universe, [0, 0, 100])
runtime['average'] = trimf(runtime.universe, [50, 100, 150])
runtime['long'] = trimf(runtime.universe, [100, 200, 200])


# Initialize the engine
engine = MovieRecommender()
