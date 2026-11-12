# Frontend

From this directory, run `uv run streamlit run main.py` using the existing environment.
`API_BASE_URL` defaults to `http://127.0.0.1:8000`. All data operations call FastAPI.
Start PostgreSQL, apply the backend migration and start FastAPI before using the page.

Register and look up snakes by ID. The page displays demo identity BR001 and marks
morph descriptions as breeder-provided, without laboratory certification. Database
storage does not mean blockchain registration or verified certificates. After creating
or querying a profile, use Submit local-chain registration and Refresh chain status.
The page shows current checked status and public transaction/manager evidence. A stale
deployment or unavailable RPC cannot be shown as confirmed. Chain signing is a local
server-mediated Hardhat demo; the page never asks for a key or sender address.

Run page tests with `uv run python -m unittest discover -s tests -v`.
These use Streamlit AppTest and mocked HTTP responses.

Choose the explicitly labelled Breeder, Laboratory or Buyer demo workspace; this is
not authentication. Laboratory saves the original PDF, selects V1 and submits issuance.
Buyer queries a snake profile, selects from its certificate list, previews/downloads
the platform original and clicks 核验证书 without uploading another PDF. The optional
上传外部文件核验 entry compares a seller-provided PDF and does not create/replace a
certificate or submit a transaction. Registration
evidence and match/mismatch/unable results are separate. No latest-version, revocation
or whole-snake certification check is claimed. 下载证书 PDF retrieves the stored bytes;
预览证书 PDF uses the browser's PDF viewer. Formal input requirements:
`../docs/samples/certificates/README.md`.
