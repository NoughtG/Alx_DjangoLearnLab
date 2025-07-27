# Django Relationship Models

## Objective
Demonstrate Django’s ORM relationships using ForeignKey, ManyToManyField, and OneToOneField.

## Models

- **Author**
  - `name`: CharField

- **Book**
  - `title`: CharField
  - `author`: ForeignKey to Author

- **Library**
  - `name`: CharField
  - `books`: ManyToManyField to Book

- **Librarian**
  - `name`: CharField
  - `library`: OneToOneField to Library

## Sample Queries

Implemented in `query_samples.py` to:
- Query all books by a specific author.
- List all books in a library.
- Retrieve the librarian for a library.

## Notes
Run queries from Django shell using:
```python
exec(open('../relationship_app/query_samples.py').read())
