from main import BooksCollector
import pytest

class TestBooksCollector:

    # добавление книги
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # книга не добавляется повторно 
    def test_add_new_book_not_added_dublicate_book(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 1

    # проверка корректного жанра для книги
    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_add_valid_genre(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', genre)
        assert collector.get_book_genre('Шерлок Холмс') == genre

    # получение жанра для книги, которая есть в словаре
    def test_get_book_genre_show_valid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Ревизор')
        collector.set_book_genre('Ревизор', 'Комедии')
        assert collector.get_book_genre('Ревизор') == 'Комедии'

    # проверка пустого списка, если у книги не указан жанр
    def test_get_book_genre_empty_list_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Боевик')
        assert collector.get_book_genre('Боевик') == ''

    # получение списка книг по жанру
    def test_get_books_with_specific_genre_list_book_by_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        result = collector.get_books_with_specific_genre('Фантастика')
        assert result == ['Дюна']

     # получение словаря с одной книгой
    def test_get_books_genre_with_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Звёздные войны')
        collector.set_book_genre('Звёздные войны','Фантастика')
        assert collector.get_books_genre() == {'Звёздные войны': 'Фантастика'}

    # получение книг, которые подходят детям
    @pytest.mark.parametrize('name, genre, access_for_children', [['Оно', 'Ужасы', False], ['Шерлок Холмс', 'Детективы', False], ['Один дома', 'Комедии', True], ['Ну, погоди!', 'Мультфильмы', True]])
    def test_get_books_for_children_(self, name, genre, access_for_children):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        children_books = collector.get_books_for_children()
        assert (name in children_books) == access_for_children

    # нельзя добавить книгу, которой нет в списке
    def test_add_book_in_favorites_book_not_add_if_not_in_list(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Неизбранная книга')
        assert collector.get_list_of_favorites_books() == []

    # удаляет книгу из избранного если она там есть
    def test_delete_book_from_favorites_remove_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert collector.get_list_of_favorites_books() == []

    # получение пустого списка, если в списке избранного не добавлены книги
    def test_get_list_of_favorites_books_empty_list_if_favorites_empty(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []