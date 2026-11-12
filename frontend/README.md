# Frontend

From this directory, run `uv run streamlit run main.py` using the existing environment.
`API_BASE_URL` defaults to `http://127.0.0.1:8000`. All data operations call FastAPI.
Start PostgreSQL, apply the backend migration and start FastAPI before using the page.

Register and look up snakes by ID. The page displays demo identity BR001 and marks
morph descriptions as breeder-provided, without laboratory certification. Database
storage does not mean blockchain registration or verified certificates.

Run page tests with `uv run python -m unittest discover -s tests -v`.
These use Streamlit AppTest and mocked HTTP responses.
