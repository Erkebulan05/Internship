# Internship

# Restaurant Booking API

## 📌 Description
A simple RESTful API to manage restaurant table reservations.

## 🚀 Setup
1. Clone this repo
2. Run `pip install -r requirements.txt`
3. Set your PostgreSQL credentials in `database.py` and `app.py`
4. Run `python database.py` to initialize the table
5. Run `python app.py` to start the server

## 🔗 Endpoints
### GET `/reservations`
Returns a list of all reservations.

### POST `/reservations`
Creates a new reservation.
```json
{
  "name": "John Doe",
  "date": "2025-07-10",
  "time": "18:30",
  "guests": 4
}
