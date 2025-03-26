Data_Pipeline

Overview

This project is a real-time weather tracking pipeline built with Python, PostgreSQL, and Next.js. It automates data ingestion from the OpenWeather API, stores it in a relational database, and provides a dynamic frontend for live updates using Next.js API routes and SWR.

Architecture

[External API] → [Python Worker (cron/scheduler)] → [PostgreSQL] ↔ [Next.js API Routes] → [Next.js Frontend]
Technologies Used

Python – Handles data ingestion and scheduling.
PostgreSQL – Stores weather data for real-time tracking.
Next.js – Provides API routes and a frontend for dynamic updates.
SWR – Ensures efficient data fetching and caching.
OpenWeather API – Data source for live weather updates.
Features

✅ Automated weather data fetching via Python scheduler.
✅ RESTful API for retrieving stored weather data.
✅ Live weather updates with Next.js & SWR.
✅ Scalable architecture with a relational database.