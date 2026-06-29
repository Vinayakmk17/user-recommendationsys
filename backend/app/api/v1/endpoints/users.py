from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core import security
from app.crud import post as crud_post
from app.crud import social as crud_social
from app.crud import user as crud_user
from app.models.user import User
from app.schemas.token import TokenWithUser
from app.schemas.user import UserCreate, UserOut, UserProfile, UserUpdate
from app.api import deps

router = APIRouter()


@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(user_in: UserCreate, db: Session = Depends(deps.get_db)):
    if crud_user.get_by_username(db, username=user_in.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    if crud_user.get_by_email(db, email=user_in.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    return crud_user.create(db, user_in=user_in)


@router.post("/login", response_model=TokenWithUser)
def login(
    db: Session = Depends(deps.get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user = crud_user.get_by_login(db, login=form_data.username)
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email/username or password",
        )
    access_token = security.create_access_token(subject=user.id)
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user,
    }


@router.get("/me", response_model=UserOut)
def read_user_me(current_user: User = Depends(deps.get_current_user)):
    return current_user


@router.put("/me", response_model=UserOut)
def update_user_me(
    updates: UserUpdate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
):
    return crud_user.update(db, user=current_user, updates=updates)


@router.get("/{username}", response_model=UserProfile)
def get_user_profile(
    username: str,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
):
    user = crud_user.get_by_username(db, username=username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    post_cnt = crud_post.count_user_posts(db, user_id=user.id)
    follower_cnt = crud_social.follower_count(db, user_id=user.id)
    following_cnt = crud_social.following_count(db, user_id=user.id)
    is_foll = crud_social.is_following(db, follower_id=current_user.id, following_id=user.id)
    is_me = current_user.id == user.id

    return UserProfile(
        id=user.id,
        username=user.username,
        full_name=user.full_name,
        bio=user.bio,
        avatar_url=user.avatar_url,
        created_at=user.created_at,
        post_count=post_cnt,
        follower_count=follower_cnt,
        following_count=following_cnt,
        is_following=is_foll,
        is_me=is_me,
    )
