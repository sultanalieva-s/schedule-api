# A REST API for Schedule App, Mazars Test Assignment

## How to Run

1. **Build and Run with Docker Compose:**
   ```sh
   docker-compose up --build
   ```

2. **Run Manually (without Docker):**
   ```sh
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

## .env File

Create a `.env` file in the root directory with the following environment variables:

```env
MONGO_ATLAS_URI=your_database_url
MONGO_DB_NAME=your_database_name
```
Also, see `.env.example` file

I created a test database stored on Mongo Atlas Cloud, to use it set the following env values:
```env
MONGO_ATLAS_URI='mongodb+srv://saadat:mDTA0D8WqBEarmd3@schedule.wqq3v.mongodb.net/?retryWrites=true&w=majority&appName=Schedule'
MONGO_DB_NAME='shedule'
```
## Docs URL

Open API documentation can be accessed at:

```
http://localhost:8000/docs/
```

