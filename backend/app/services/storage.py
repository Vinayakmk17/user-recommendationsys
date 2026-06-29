import os
import uuid

from fastapi import HTTPException, UploadFile, status

from app.core.config import settings

ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/gif", "image/webp"}
ALLOWED_VIDEO_TYPES = {"video/mp4", "video/mpeg", "video/ogg", "video/quicktime", "video/webm"}

# Initialize Supabase client if using supabase backend
supabase_client = None
if settings.STORAGE_BACKEND == "supabase":
    if settings.SUPABASE_URL and settings.SUPABASE_KEY:
        from supabase import create_client
        supabase_client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)


async def upload_media(
    file: UploadFile,
    folder: str,
    allowed_types: set[str],
) -> str:
    content_type = file.content_type
    if content_type not in allowed_types:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File type {content_type} not allowed.",
        )

    # Generate unique filename
    ext = os.path.splitext(file.filename or "")[1] or ".jpg"
    unique_filename = f"{uuid.uuid4()}{ext}"
    file_path = f"{folder}/{unique_filename}".strip("/")

    file_content = await file.read()

    if settings.STORAGE_BACKEND == "supabase":
        if not supabase_client:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Supabase storage is not configured.",
            )
        try:
            # Upload file to Supabase Bucket
            supabase_client.storage.from_(settings.SUPABASE_STORAGE_BUCKET).upload(
                path=file_path,
                file=file_content,
                file_options={"content-type": content_type},
            )
            # Get public URL
            public_url = supabase_client.storage.from_(settings.SUPABASE_STORAGE_BUCKET).get_public_url(file_path)
            return public_url
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to upload to Supabase: {str(e)}",
            )
    else:
        # Local storage backend
        local_dir = os.path.join(settings.MEDIA_ROOT, folder)
        os.makedirs(local_dir, exist_ok=True)
        local_file_path = os.path.join(local_dir, unique_filename)

        try:
            with open(local_file_path, "wb") as f:
                f.write(file_content)

            # Return local public URL
            relative_url = f"/media/{folder}/{unique_filename}".replace("\\", "/")
            public_url = f"{settings.BACKEND_PUBLIC_URL.rstrip('/')}{relative_url}"
            return public_url
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to save file locally: {str(e)}",
            )
