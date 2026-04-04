import sys
from pathlib import Path

# Add the src directory to the Python path to allow imports
src_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(src_dir))


def run_server():
    """Run the uvicorn server with configured settings."""
    import uvicorn
    from lms_backend.settings import settings

    uvicorn.run(
        app="lms_backend.main:app",
        host=settings.address,
        port=settings.port,
        reload=settings.reload,
        reload_dirs=[str(src_dir)],
    )


if __name__ == "__main__":
    run_server()
