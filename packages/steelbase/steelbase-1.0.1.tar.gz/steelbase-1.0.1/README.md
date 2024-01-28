# SteelBase

Ex.

Creating A Simple Database

```python
# Importing steelbase (pip install steelbase)
from steelbase import SteelBase

# Creating a SteelBase instance (loading existing data if any)
steelbase_instance = SteelBase()

# Creating a table named 'books'
steelbase_instance.create_table("books")

# Adding records to the 'books' table
steelbase_instance.add_record("books", 1, {"title": "Python 101", "author": "John Doe"})
steelbase_instance.add_record("books", 2, {"title": "Web Development Basics", "author": "Jane Smith"})

# Saving the data to the file with ".steelbase" extension
steelbase_instance.save_data()

# Retrieving and printing all records in the 'books' table
print(steelbase_instance.show_records("books"))
```

# Developed by steeldev